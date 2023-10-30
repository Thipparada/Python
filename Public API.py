import requests
url = "https://api.nasa.gov/DONKI/CME?startDate=2017-01-03&endDate=2017-01-03&api_key=DEMO_KEY"

resp = requests.get(url)

## if success, OK 200
resp.status_code

## see information
resp.text
a = resp.json()[0]

## get the name of the fifth characters
import requests
import time
nasa = []
for i in range(10):
    resp = requests.get(url)
    if resp.status_code == 200:
        json_data = resp.json()[0]
        nasa.append(
            (json_data["activityID"],
            json_data["catalog"])
        )
    else :
        nasa.append("error")
    # break a second
    time.sleep(1)
