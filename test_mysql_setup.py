import os
import unittest
import MySQLdb


class TestMySQLSetup(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        try:
            conn = MySQLdb.connect(user=os.getenv('HBNB_YELP_MYSQL_USER', 'root'),
                                   passwd=os.getenv('HBNB_YELP_MYSQL_PWD', ''),
                                   db='mysql_db_test',
                                   host=os.getenv('HBNB_YELP_MYSQL_HOST', 'localhost'),
                                   port=int(os.getenv('HBNB_YELP_MYSQL_PORT', 3306)))
            cursor = conn.cursor()
            cursor.execute('SELECT 1')
            cursor.execute('DROP DATABASE IF EXISTS hbnb_dev_db')
            cursor.execute('CREATE DATABASE hbnb_dev_db')
            cursor.execute('CREATE USER IF NOT EXISTS "hbnb_dev"@"localhost" IDENTIFIED BY "hbnb_dev_pwd"')
            cursor.execute('GRANT ALL PRIVILEGES ON hbnb_dev_db.* TO "hbnb_dev"@"localhost"')
            cursor.execute('GRANT SELECT ON performance_schema.* TO "hbnb_dev"@"localhost"')
            conn.commit()
            cursor.close()
            conn.next_result() # fix for "Commands out of sync" error
            conn.close()
        except Exception as e:
            print(e)
            cls.skipTest(cls, "setup failed")

    def test_setup(self):
        try:
            conn = MySQLdb.connect(user='hbnb_dev',
                                   passwd='hbnb_dev_pwd',
                                   db='hbnb_dev_db',
                                   host='localhost',
                                   port=3306)
            cursor = conn.cursor()
            cursor.execute('SELECT 1')
            cursor.close()
            conn.close()
        except Exception as e:
            self.fail("Test setup failed: {}".format(e))


if __name__ == '__main__':
    unittest.main()
