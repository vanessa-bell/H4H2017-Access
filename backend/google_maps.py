from googleplaces import GooglePlaces, types
from google_api_keys import API_KEY
import pdb

key = API_KEY
google_places = GooglePlaces(key)
query_result = google_places.nearby_search(
        location='94040',
        radius=20000, types=[types.TYPE_PHARMACY])

# pdb.set_trace()


for place in query_result.places:
  print place.name
  print place.place_id
  print place.geo_location
# print query_result

# gmaps = googlemaps.Client(key)
# address = 'Constitution Ave NW & 10th St NW, Washington, DC'
# lat = gmaps.geocode(address)
# print lat
