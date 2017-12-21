from urllib.request import urlopen
from urllib.parse import urlencode
from urllib.error import HTTPError

class CustomError:
    def __init__(self):
        self.status = 400

class GeoCoordinates:
    'Handles calling of third party geocoding services, returns just the lat/lng part of the response.'

    def __init__(self, baseURL, key, searchKeyName, address):
        self.geoApiBaseURL = baseURL
        self.apiKey = key
        self.searchKeyName = searchKeyName
        self.address = address

    def fetchCoordinates (self):
        requestData = {}
        requestData['key'] = self.apiKey
        requestData[self.searchKeyName] = self.address
        urlEncodedRequestData = urlencode(requestData)
        request = self.geoApiBaseURL + urlEncodedRequestData
        print(request)
        try:
            return urlopen(request)
        except HTTPError as error:
            print(error.status)
            return CustomError()