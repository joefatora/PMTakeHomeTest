from urllib.request import urlopen
from urllib.parse import urlencode
from urllib.error import HTTPError

class GeoCoordinates:
    'Handles calling of third party geocoding services, returns just the lat/lng part of the response.'

    def __init__(self, baseURL, key, address):
        self.geoApiBaseURL = baseURL
        self.key = key
        self.address = address

    def fetchCoordinates (self):
        requestData = {}
        requestData['key'] = self.key
        requestData['address'] = self.address
        urlEncodedRequestData = urlencode(requestData)
        request = self.geoApiBaseURL + '?' + urlEncodedRequestData
        try:
            return urlopen(request)
        except HTTPError as error:
            return error.code

