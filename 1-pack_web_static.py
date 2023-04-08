from fabric.api import local
from datetime import datetime
import os

def do_pack():
    '''Create a tar gzipped archive of the web_static folder'''
    try:
        if not os.path.exists('versions'):
            os.makedirs('versions')
        now = datetime.now().strftime('%Y%m%d%H%M%S')
        archive_path = 'versions/web_static_{}.tgz'.format(now)
        local('tar -czvf {} web_static'.format(archive_path))
        print('web_static packed: {} -> {}Bytes'.format(archive_path, os.path.getsize(archive_path)))
        return archive_path
    except:
        return None
