''' 
This python scrpit is for geocoding and reverse geocoding using OpenCage Geocoding API.

This script allows for address to be coded to geometric lattitude and longitude i.e. geocoding 
and also geometric lattitude and longitude to address i.e. reverse geocoding.

The address is inputed into the program and the result is shown by the program.
The free tier of OpenCage Geocoding API is set to 1 api-call per second or 2,500/day
to get more upgrade to Paid plans as per your requirements.

Syed Sadiqu Hussain
28th Feb, 2023

NOTE: - Make sure to put "your api-key" before running the code. 
'''

# Packages Import
import requests

# TODO: #4 Remove the API-KEY at the end.
API_KEY = "c84c08d456004f69947f60ce5bf0fe7b"

'''
This method will accept the address to find lat and lng as String and api_key which is declared in configuration.
It returns a list with latitute and longitude i.e. [latitude, longitude]
'''
def forward_geocode_results(address, api_key = None):      
    # TODO: #1 Handle the Connction Errors of both methods.
    # Setitng up the forward geocode api url
    forward_geocode_url = "https://api.opencagedata.com/geocode/v1/json?q={}".format(address)
    if api_key is not None:
        forward_geocode_url = forward_geocode_url + "&key={}".format(api_key)
    
    # get request through api
    response = requests.get(forward_geocode_url)
    response = response.json()

    # Checking status:
    if response["status"]["code"] == 400:           # bad request; a required parameter is missing; invalid coordinates; invalid version; invalid format
        print(response["status"]["message"])
        raise ConnectionError("Invalid request - Problem with address.")
    elif response["status"]["code"] == 401:         # Unable to Validate. Invalid, Missing, or unknown API key
        print(response["status"]["message"])
        raise ConnectionError("Unable to validate. ")
    elif response["status"]["code"] == 402:         # Quota Exceeded
        print(response["status"]["message"])
        raise ConnectionError("Quota exceeded.")
    elif response["status"]["code"] == 403:         # IP address rejected OR API key disabled
        print(response["status"]["message"])
        raise ConnectionError("IP address Rejected. Wait few minutes before trying again.")
    elif response["status"]["code"] == 408:         # Timeout... Try Again
        print(response["status"]["message"])
        raise ConnectionError("Connection Timeout.")
    elif response["status"]["code"] == 410:         # Request too long
        print(response["status"]["message"])
        raise ConnectionError("Request too long. Try a Smaller Request")
    elif response["status"]["code"] == 426:         # Upgrade Required (Unsupported TLS)
        print(response["status"]["message"])
        raise ConnectionError("Upgrade Required.")
    elif response["status"]["code"] == 429:         # Too many requests (too quickly, rate limiting)
        print(response["status"]["message"])
        raise ConnectionError("Too Quick. Try again.")
    elif response["status"]["code"] == 503:         # Internal Server Error
        print(response["status"]["message"])
        raise ConnectionError("Internal Server Error.")
    
    # if no error occurs, the api-get request is successful.
    # Processing the response.
    geoCode = [];       # [Latitude, Longitude]
    result_number = len(response["results"])
    # Sorting the result on the basis of confidence
    response["results"].sort(key = lambda x: x["confidence"])
    geoCode.append(response["results"][result_number-1]["geometry"]["lat"])     # latitude with highest Confidence
    geoCode.append(response["results"][result_number-1]["geometry"]["lng"])     # longitude with highest confidence
    
    return geoCode

'''
This method will accept the latitude and Longitudes as float to find the address and api_key which is declared in configuration.
It returns a list with latitute and longitude i.e. [latitude, longitude]
'''
def reverse_geocode_results(lat, lng, api_key = None):      # TODO: Get a param to ask if they need full info or stripped.
    # Setitng up the forward geocode api url
    reverse_geocode_url = "https://api.opencagedata.com/geocode/v1/json?q={},{}".format(lat,lng)
    if api_key is not None:
        reverse_geocode_url = reverse_geocode_url + "&key={}".format(api_key)
    
    # get request through api
    response = requests.get(reverse_geocode_url)
    response = response.json()

    # Checking status:
    if response["status"]["code"] == 400:           # bad request; a required parameter is missing; invalid coordinates; invalid version; invalid format
        print(response["status"]["message"])
        raise ConnectionError("Invalid request - Problem with address.")
    elif response["status"]["code"] == 401:         # Unable to Validate. Invalid, Missing, or unknown API key
        print(response["status"]["message"])
        raise ConnectionError("Unable to validate. ")
    elif response["status"]["code"] == 402:         # Quota Exceeded
        print(response["status"]["message"])
        raise ConnectionError("Quota exceeded.")
    elif response["status"]["code"] == 403:         # IP address rejected OR API key disabled
        print(response["status"]["message"])
        raise ConnectionError("IP address Rejected. Wait few minutes before trying again.")
    elif response["status"]["code"] == 408:         # Timeout... Try Again
        print(response["status"]["message"])
        raise ConnectionError("Connection Timeout.")
    elif response["status"]["code"] == 410:         # Request too long
        print(response["status"]["message"])
        raise ConnectionError("Request too long. Try a Smaller Request")
    elif response["status"]["code"] == 426:         # Upgrade Required (Unsupported TLS)
        print(response["status"]["message"])
        raise ConnectionError("Upgrade Required.")
    elif response["status"]["code"] == 429:         # Too many requests (too quickly, rate limiting)
        print(response["status"]["message"])
        raise ConnectionError("Too Quick. Try again.")
    elif response["status"]["code"] == 503:         # Internal Server Error
        print(response["status"]["message"])
        raise ConnectionError("Internal Server Error.")
    
    # if no error occurs, the api-get request is successful.
    
    # Processing the response -- <if needed some specific component of address.>
    # geoloc = [];       # [City, Country, Continent]
    # geoloc.append(response["results"]["components"]["city"])     # city
    # geoloc.append(response["results"]["components"]["country"])     # country
    # geoloc.append(response["results"]["components"]["continent"])     # continent
    
    geoloc = response["results"][0]["formatted"]        # Pre-formatted address.
    
    return geoloc

# print(forward_geocode_results("Rairangpur", API_KEY))
# print(reverse_geocode_results(20.2215795,85.6735783, API_KEY))