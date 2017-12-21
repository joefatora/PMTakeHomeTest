import hug
from geo_coordinates import GeoCoordinates
import json

googleApiKey = 'AIzaSyALd50D4pz6HW6uNNpTFjQGyMSfuVGO13Q'
googleGeoApiBaseURL = 'https://maps.googleapis.com/maps/api/geocode/json?'
googleAddresSearchKeyName = 'address'

mapquestApiKey = 'Oq3m4HF21JCQdNoeVOzzKbvu9r16KdQy'
mapquestGeoApiBaseURL = 'https://www.mapquestapi.com/geocoding/v1/address?inFormat=kvp&outFormat=json&thumbMaps=false&'
mapquestAddresSearchKeyName = 'location'

Constants = {}
Constants['OK_Status'] = 200
Constants['ERROR_Status'] = 400

@hug.get(examples='address=Rue de Bouzanton 20a, Mons Belgium 7000')

def buildSuccessResponse(lat, lng):
        responseInfo = {}
        responseInfo['status'] = 200
        responseInfo['coordinates'] = {}


def submit_address(address: hug.types.multiple):
    
    """Returns Geo encoded 3rd Party API response based on address entered. One comma should separate the street component from the city state and zip components. Only street address, city and state are required."""
    googleGeoCoordinates = GeoCoordinates(googleGeoApiBaseURL, googleApiKey, googleAddresSearchKeyName, address).fetchCoordinates()
    
    if googleGeoCoordinates.status == Constants['OK_Status']:
        locationInfo = json.loads(googleGeoCoordinates.read())
        lat = responseInfo['coordinates']['lat'] = locationInfo['results'][0]['geometry']['location']['lat']
        lng = responseInfo['coordinates']['lng'] = locationInfo['results'][0]['geometry']['location']['lng']
        return buildSuccessResponse(lat, lng)
    
    mapquestGeoCoordinates = GeoCoordinates(mapquestGeoApiBaseURL, mapquestApiKey, mapquestAddresSearchKeyName, address).fetchCoordinates()
    
    if mapquestGeoCoordinates.status == Constants['OK_Status']:
        locationInfo = json.loads(mapquestGeoCoordinates.read())
        lat = responseInfo['coordinates']['lat'] = locationInfo['results'][0]['locations'][0]['latLng']['lat']
        lng = responseInfo['coordinates']['lng'] = locationInfo['results'][0]['locations'][0]['latLng']['lng']
        return buildSuccessResponse(lat, lng)
    
    else: 
        
        errorResponse = {}
        errorResponse['status'] = Constants['ERROR_Status']
        errorResponse['message'] = "Geolocation API currently unavailable. Please try your request again later."
        return errorResponse
