#!/usr/bin/python3
""" Test link Many-To-Many Place <> Amenity
"""
from models.state   import State
from models.city    import City
from models.user    import User
from models.place   import Place
from models.amenity import Amenity

# import statement to make 'storage' available in this file
from models import storage

# create a State
state = State(name="California")
state.save()

# create a City
city = City(state_id=state.id, name="San Francisco")
city.save()

# create a User
user = User(email="john@snow.com", password="johnpwd")
user.save()

# create 2 Places
place_1 = Place(user_id=user.id, city_id=city.id, name="House 1")
place_1.save()
place_2 = Place(user_id=user.id, city_id=city.id, name="House 2")
place_2.save()

# create 3 Amenity
amenity_1 = Amenity(name="Wifi")
amenity_1.save()
amenity_2 = Amenity(name="Cable")
amenity_2.save()
amenity_3 = Amenity(name="Oven")
amenity_3.save()

# link place_1 with 2 amenities
place_1.amenities.append(amenity_1)
place_1.amenities.append(amenity_2)

# link place_2 with 3 amenities
place_2.amenities.append(amenity_1)
place_2.amenities.append(amenity_2)
place_2.amenities.append(amenity_3)

# reload the storage engine to initialize it
storage.reload()

# save changes to the database
storage.save()

print("OK")
