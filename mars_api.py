
import requests
import pandas as pd
import json

# API base URL (without equipment_id)
#API_BASE = "https://mars.keysight.com/webapi/GetStationByEquipmentID"
#API_TEST = "https://mars.keysight.com/webapi/testapi"
#USER = "Upload_Infoline"
#PASSWORD = "Muckd$R7b8mHfX6t!r5a4V2G"

def fetch_station_data(API_BASE,USER,PASSWORD,equipment_ids):
    """
    Fetch station data for one or more equipment IDs.
    Args:
        equipment_ids (str or list): Single ID "EQ123" or list ["EQ123", "EQ456"]
    Returns:
        list of dicts: station data
    """
    if isinstance(equipment_ids, list):
        equipment_ids = ",".join(equipment_ids)  # Convert list to comma-separated string
        print(equipment_ids)
    url = f"{API_BASE}?user={USER}&password={PASSWORD}&equipment_id={equipment_ids}"

    try:
        response = requests.get(url)
        response.raise_for_status()
        data = response.json()
        if data.get("result") and data.get("ret"):
            return data["ret"]
        else:
            print("No station data found.")
            return []
    except requests.RequestException as e:
        print(f"API request failed: {e}")
        return []
    except Exception as e:
        print(f"Failed to parse response: {e}")
        return []

def get_station_by_index(stations, index):
    """
    Get station data by index from the list returned by fetch_station_data.
    """
    if 0 <= index < len(stations):
        return stations[index]
    else:
        print(f"Index {index} is out of range.")
        return None

def fetch_test_api():
    """Fetch raw response from test API"""
    try:
        response = requests.get(API_TEST)
        response.raise_for_status()
        return response.json()
    except requests.RequestException as e:
        print(f"Test API request failed: {e}")
        return None
