## GEO Locator

To run the program, ensure you have [hug](http://www.hug.rest/) available, along with its dependencies (esp python3)

From this directory, run `hug -f server.py`

Navigate to `localhost:8000/submit_address?`

* Determine the address you want to search.
* One comma should separate the street component from the city state and zip components.
* Only street address, city and state are required.
* Append the query to the url above. No special encoding is required.
* Search and a valid address should result in a response of the format `{"status": 200, "coordinates": {"lat": X.XXX, "lng": Y.YYY}}`

