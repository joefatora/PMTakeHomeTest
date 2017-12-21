import hug
from geo_coordinates import GeoCoordinates

googleApiKey = 'AIzaSyALd50D4pz6HW6uNNpTFjQGyMSfuVGO13Q'
googleGeoApiBaseURL = 'https://maps.googleapis.com/maps/api/geocode/json'

Constants = {}
Constants['OK_Status'] = 200

@hug.get(examples='address=Rue de Bouzanton 20a, Mons Belgium 7000')
def submit_address(address: hug.types.multiple):
    """Returns Lat, Lon based on address entered. One comma should separate the street component from the city state and zip components. Only street address, city and state are required."""
    googleGeoCoordinates = GeoCoordinates(googleGeoApiBaseURL, googleApiKey, address).fetchCoordinates()
    if googleGeoCoordinates.status == Constants['OK_Status']:
        return googleGeoCoordinates
    else:
        print(googleGeoCoordinates.status)
        errorResponse = {}
        errorResponse.status = 400
        errorResponse.message = "Geolocation API currently unavailable. Please try your request again later."
        return errorResponse