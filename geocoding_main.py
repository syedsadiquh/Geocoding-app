"""
This python script is for geocoding and reverse geocoding using OpenCage Geocoding API.

This script allows for address to be coded to geometric latitude and longitude i.e. geocoding
and also geometric latitude and longitude to address i.e. reverse geocoding.

The address is inputted into the program and the result is shown by the program.
The free tier of OpenCage Geocoding API is set to 1 api-call per second or 2,500/day
to get more upgrade to Paid plans as per your requirements.

Syed Sadiqu Hussain
28th Feb, 2023

NOTE: - Make sure to put "your api-key" before running the code.
"""

# Packages Import
import requests

# TODO: Put your API KEY here...
API_KEY = "a0be982b19f34bbf9564b7d12237880a"

'''
This method will accept the address to find lat and lng as String and api_key which is declared in configuration.
It returns a list with latitude and longitude i.e. [latitude, longitude]
'''


class QueryError(Exception):
    def __init__(self, msg):
        self.message = msg


def forward_geocode_results(address, api_key=None):
    # Setting up the forward geocode api url
    forward_geocode_url = "https://api.opencagedata.com/geocode/v1/json?q={}".format(address)
    if api_key is not None:
        forward_geocode_url = forward_geocode_url + "&key={}".format(api_key)

    # get request through api
    response = requests.get(forward_geocode_url)
    response = response.json()

    # Checking status:
    if response["status"]["code"] == 400:  # bad request; a required parameter is missing;
        # invalid coordinates; invalid version; invalid format
        print(response["status"]["message"])
        raise ConnectionError("Invalid request - Problem with address.")
    elif response["status"]["code"] == 401:  # Unable to Validate. Invalid, Missing, or unknown API key
        print(response["status"]["message"])
        raise ConnectionError("Unable to validate. ")
    elif response["status"]["code"] == 402:  # Quota Exceeded
        print(response["status"]["message"])
        raise ConnectionError("Quota exceeded.")
    elif response["status"]["code"] == 403:  # IP address rejected OR API key disabled
        print(response["status"]["message"])
        raise ConnectionError("IP address Rejected. Wait few minutes before trying again.")
    elif response["status"]["code"] == 408:  # Timeout... Try Again
        print(response["status"]["message"])
        raise ConnectionError("Connection Timeout.")
    elif response["status"]["code"] == 410:  # Request too long
        print(response["status"]["message"])
        raise ConnectionError("Request too long. Try a Smaller Request")
    elif response["status"]["code"] == 426:  # Upgrade Required (Unsupported TLS)
        print(response["status"]["message"])
        raise ConnectionError("Upgrade Required.")
    elif response["status"]["code"] == 429:  # Too many requests (too quickly, rate limiting)
        print(response["status"]["message"])
        raise ConnectionError("Too Quick. Try again.")
    elif response["status"]["code"] == 503:  # Internal Server Error
        print(response["status"]["message"])
        raise ConnectionError("Internal Server Error.")

    # if no error occurs, the api-get request is successful.
    # Processing the response.
    geo_code = []  # [Latitude, Longitude]
    result_number = response["total_results"]
    if result_number > 0:
        # Sorting the result on the basis of confidence
        response["results"].sort(key=lambda x: x["confidence"])
        # latitude with the highest Confidence
        geo_code.append(response["results"][result_number - 1]["geometry"]["lat"])
        # longitude with the highest confidence
        geo_code.append(response["results"][result_number - 1]["geometry"]["lng"])
    else:
        raise QueryError("Not a Place")

    return geo_code


'''
This method will accept the latitude and Longitudes as float to find the address 
and api_key which is declared in configuration.
It returns a list with latitude and longitude i.e. [latitude, longitude]
'''


def reverse_geocode_results(lat, lng, api_key=None):  # TODO: Get a param to ask if they need full info or stripped.
    # Setting up the forward geocode api url
    reverse_geocode_url = "https://api.opencagedata.com/geocode/v1/json?q={},{}".format(lat, lng)
    if api_key is not None:
        reverse_geocode_url = reverse_geocode_url + "&key={}".format(api_key)

    # get request through api
    response = requests.get(reverse_geocode_url)
    response = response.json()

    # Checking status:
    if response["status"]["code"] == 400:  # bad request; a required parameter is missing;
        # invalid coordinates; invalid version; invalid format
        print(response["status"]["message"])
        raise ConnectionError("Invalid request - Problem with address.")
    elif response["status"]["code"] == 401:  # Unable to Validate. Invalid, Missing, or unknown API key
        print(response["status"]["message"])
        raise ConnectionError("Unable to validate. ")
    elif response["status"]["code"] == 402:  # Quota Exceeded
        print(response["status"]["message"])
        raise ConnectionError("Quota exceeded.")
    elif response["status"]["code"] == 403:  # IP address rejected OR API key disabled
        print(response["status"]["message"])
        raise ConnectionError("IP address Rejected. Wait few minutes before trying again.")
    elif response["status"]["code"] == 408:  # Timeout... Try Again
        print(response["status"]["message"])
        raise ConnectionError("Connection Timeout.")
    elif response["status"]["code"] == 410:  # Request too long
        print(response["status"]["message"])
        raise ConnectionError("Request too long. Try a Smaller Request")
    elif response["status"]["code"] == 426:  # Upgrade Required (Unsupported TLS)
        print(response["status"]["message"])
        raise ConnectionError("Upgrade Required.")
    elif response["status"]["code"] == 429:  # Too many requests (too quickly, rate limiting)
        print(response["status"]["message"])
        raise ConnectionError("Too Quick. Try again.")
    elif response["status"]["code"] == 503:  # Internal Server Error
        print(response["status"]["message"])
        raise ConnectionError("Internal Server Error.")

    # if no error occurs, the api-get request is successful.

    # Processing the response -- <if needed some specific component of address.>
    # geo_loc = [];       # [City, Country, Continent]
    # geo_loc.append(response["results"]["components"]["city"])     # city
    # geo_loc.append(response["results"]["components"]["country"])     # country
    # geo_loc.append(response["results"]["components"]["continent"])     # continent
    if response["total_results"] > 0:
        geo_loc = response["results"][0]["formatted"]  # Pre-formatted address.
    else:
        raise QueryError("Invalid Latitude or Longitude")

    return geo_loc

# These lines are for testing the API connectivity and response.
# print(forward_geocode_results("Gandhi Institute for Technology", API_KEY))
# print(reverse_geocode_results(20.2215795,85.6735783, API_KEY))
