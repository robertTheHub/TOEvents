import requests
import json
from datetime import datetime
import sys


if __name__ == "__main__":
    i = 0
    data = {
            "orgType": set(),
            "hasStartDate": 0,
            "noStartDate": 0,
            "hasAddress": 0,
            "noAddress":0,
            "hasEndDate":0,
            "noEndDate":0,
            "frequency":set(),
            "category":set(),
            "features":set(),
            "categoryString": 0,
            "noString": 0,
            "noFrequency":0,
            }
    print("Calling API...")
    events = requests.get("http://app.toronto.ca/cc_sr_v1_app/data/edc_eventcal_APR?limit=500") #Use arguments to make the max variable
    print("Call Returned")
    for event in events.json():
        event = event["calEvent"]
        try:
            for cat in event["category"]:
                data["category"].add(cat["name"])
        except Exception:
            try:
                event["categoryString"]
                data["categoryString"] +=1
            except Exception:
                data["noString"] +=1
        try:
            data["frequency"].add((event["frequency"]))
        except Exception:
            data["noFrequency"] += 1
        try:
            for feat in event["features"].keys():
                data["features"].add(feat)
        except Exception:
            None
        try:
            data["orgType"].add((event["orgType"]))
        except Exception:
            None
        try: 
            event["startDate"]
            data["hasStartDate"] += 1
        except Exception:
            data["noStartDate"] +=1
        try:
            event["endDate"]
            data["hasEndDate"] += 1
        except Exception:
            data["noEndDate"] +=1
        try:
            event["orgAddress"]
            data["hasAddress"] += 1
        except Exception:
            data["noAddress"] +=1

        #start = datetime.strptime(event["startDate"], "%Y-%m-%dT%H:%M:%S.000Z")
        #end = datetime.strptime(event["endDate"], "%Y-%m-%dT%H:%M:%S.000Z")
        #current = datetime.now().isoformat(timespec='milliseconds')
        print("="*80)
        print("|| " + str(i) + ") " + event["eventName"])
        print("-"*80)
        print ("|| * " + event["description"])
        print("\n")
        i += 1
    
    for key in data.keys():
        print(key + " : " + str(data[key]))
