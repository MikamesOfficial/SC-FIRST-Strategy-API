import functions_framework
import os
import requests as r
import json

my_key = os.getenv("api_key")
my_tba_key = os.getenv("my_tba_key")
HEADERS = {"X-TBA-Auth-Key": my_tba_key} #Missing ETag - Adding laterrrrzzz

@functions_framework.http
def general_http(request):
    request_json = request.get_json(silent=True)
    request_args = request.args
    request_method = request.method

    api_key = request.headers.get("X-SCF-API-KEY")
    if api_key != my_key:
        return {"Error": "Unauthorized Access"}, 401

    if request_method == "GET":
        if not request_args:
            return {"Error": "No arguments passed"}, 400

        

        def get_test(hds):
            url = f"https://www.thebluealliance.com/api/v3/districts/2025"
            response = r.get(url, headers=hds)
            if response.status_code != 200:
                return {str(response.text):f"Error from bluealliance"}
            return response.json()

        test = get_test(HEADERS)

        return f'{test}'

    elif request_method == "POST":
        #function that uploads data to excel based on certain args...
        return f"Populated the database (NAME) with: \"{json.dumps(request_json)}\""
