from googleplaces import GooglePlaces, types
from google_api_keys import API_KEY
import pdb
import pprint
import mysql.connector
from mysql.connector import errorcode
from h4h_database import user,password,database


cnx = mysql.connector.connect(user=user,password=password,database=database)
cursor = cnx.cursor()

# try:
#   cnx = mysql.connector.connect(user=user,
#                                 password=password,
#                                 database=database)
# except mysql.connector.Error as err:
#   if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
#     print("Something is wrong with your user name or password")
#   elif err.errno == errorcode.ER_BAD_DB_ERROR:
#     print("Database does not exist")
#   else:
#     print(err)
# else:
#   # print('connected successfully')
#   cnx.close()

# DB_NAME = database

# TABLES = {}
# TABLES['pharmacies'] = (
#     "CREATE TABLE `pharmacies` ("
#     "  `place_id` varchar(20) NOT NULL,"
#     "  `name` varchar(255) NOT NULL,"
#     "  `address` varchar(255) NOT NULL,"
#     "  `phone_number` varchar(255) NOT NULL,"
#     "  `website` varchar(255) NOT NULL,"
#     "  `prescribes` varchar(3) NOT NULL,"
#     "  PRIMARY KEY (`place_id`)"
#     ") ENGINE=InnoDB")


# def create_database(cursor):
#     try:
#         cursor.execute(
#             "CREATE DATABASE {} DEFAULT CHARACTER SET 'utf8'".format(DB_NAME))
#     except mysql.connector.Error as err:
#         print("Failed creating database: {}".format(err))
#         exit(1)

# try:
#     cnx.database = DB_NAME
# except mysql.connector.Error as err:
#     if err.errno == errorcode.ER_BAD_DB_ERROR:
#         create_database(cursor)
#         cnx.database = DB_NAME
#     else:
#         print(err)
#         exit(1)


# for name, ddl in TABLES.iteritems():
#     try:
#         print "Creating table {}: ".format(name),
#         cursor.execute(ddl)
#     except mysql.connector.Error as err:
#         if err.errno == errorcode.ER_TABLE_EXISTS_ERROR:
#             print("already exists.")
#         else:
#             print(err.msg)
#     else:
#         print("OK")

# cursor.close()
# cnx.close()


key = API_KEY
google_places = GooglePlaces(key)
query_result = google_places.nearby_search(
        location='San Francisco, CA',
        radius=50000, keyword='pharmacy')

# pdb.set_trace()


if query_result.has_attributions:
    print query_result.html_attributions

for place in query_result.places:
  # print place.name

  # The following method has to make a further API call.
  place.get_details()
  # Referencing any of the attributes below, prior to making a call to
  # get_details() will raise a googleplaces.GooglePlacesAttributeError.
  # pp = pprint.PrettyPrinter(indent=4)
  # pp.pprint(place.details) # A dict matching the JSON response from Google.

  print place.place_id
  print place.name
  print place.formatted_address
  print place.local_phone_number
  place_id = place.place_id
  name = place.name
  address =  place.formatted_address
  phone_number = place.local_phone_number
  website = place.website

  if name == 'CVS Pharmacy':
    # pdb.set_trace()
    add_pharmacy = ("INSERT INTO pharmacies "
               "(place_id, name, address, phone_number, website, prescribes) "
               "VALUES (%s, %s, %s, %s, %s, %s)")
    pharmacy_data = (place_id, name, address, phone_number, website, 'NO')
    cursor.execute(add_pharmacy, pharmacy_data)
    place_id = cursor.lastrowid
  # print place.geo_location

# add_pharmacy = ("INSERT INTO employees "
#                "(first_name, last_name, hire_date, gender, birth_date) "
#                "VALUES (%s, %s, %s, %s, %s)")

# pharmacy_data = (place_id, name, address, phone_number, website, '')

cnx.commit()

cursor.close()
cnx.close()







