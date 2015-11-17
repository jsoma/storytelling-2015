from models import *
from time import sleep
import requests

# Run the migration
# Peewee will throw an error if it doesn't work, but we can just use
# try/except to ignore it
try:  
  db.execute_sql("ALTER TABLE schools ADD COLUMN latitude DECIMAL(9,6)")
  db.execute_sql("ALTER TABLE schools ADD COLUMN longitude DECIMAL(9,6)")
except:
  print "Already added columns, skipping that part"

# Let's get all of the schools that haven't been geocoded yet
# This is apparently how you select where latitude is null
schools = School.select().where(School.latitude >> None)

for school in schools:
  # Wait a few seconds between each of these because we'd like to pretend
  # we aren't robots and are polite
  sleep(1)
  # Wrap this in try/except because hey if it fails it fails
  # Form the URL with the address in it
  url = "http://maps.googleapis.com/maps/api/geocode/json?sensor=false&address={}".format(school.full_address())
  print school.full_address()
  # Request the URL
  response = requests.get(url)

  # Dig deep into the JSON 
  # this will give us something like
  # {u'lat': 40.7135296, u'lng': -73.9856844}
  coords = response.json()['results'][0]['geometry']['location']

  # Assign the lat/lng into the school object (the row)
  school.latitude = coords['lat']
  school.longitude = coords['lng']

  # And now save it to the database
  school.save()
  print "{} is at {}, {}".format(school.school_name, school.latitude, school.longitude)
  # except:
  #   print "Failed to query/save for {}".format(school.school_name)