import requests
import json
from datetime import datetime
import sys


if __name__ == "__main__":
    i = 0
    print("Calling API...")
    events = requests.get("http://app.toronto.ca/cc_sr_v1_app/data/edc_eventcal_APR?limit=500") #Use arguments to make the max variable
    print("Call Returned")
    for event in events.json():
        event_json = event["calEvent"]
        start = datetime.strptime(event_json["startDate"], "%Y-%m-%dT%H:%M:%S.000Z")
        end = datetime.strptime(event_json["endDate"], "%Y-%m-%dT%H:%M:%S.000Z")
        current = datetime.now().isoformat(timespec='milliseconds')
        print("="*80)
        print("|| " + str(i) + ") " + event_json["eventName"])
        print("-"*80)
        print ("|| * " + event_json["description"])
        print("\n")
        i += 1
