from mars_api import fetch_station_data, get_station_by_index
import pandas as pd
import json

def main():
    # Fetch multiple equipment IDs
    equipment_ids = ["EQ651319", "PA1503","PA1101"]
    stations = fetch_station_data(equipment_ids)
 
    if not stations:
        return

    # Convert to pandas DataFrame
    df = pd.DataFrame(stations)
    print("=== All Station Data ===")
    print(df)

    # Example: get 2nd station
    second_station = get_station_by_index(stations, 1)
    if second_station:
        print("\n=== 2nd Station Data ===")
        print(json.dumps(second_station, indent=4))


        # Example: get 2nd station Station ID
        print("Station_ID:", df.iloc[1]["Station_ID"])
        
    # Fetch station data
    stations_all_stationID = fetch_station_data(equipment_ids)

    if not stations:
     print("No stations returned.")
    else:
        # Use list comprehension to get all Station_IDs
        station_ids = [station["Station_ID"] for station in stations_all_stationID]
        print("All Station_IDs:")
        print(station_ids)

    # Save all data to CSV
    df.to_csv("station_data.csv", index=False)
    print("\nSaved all station data to 'station_data.csv'")

if __name__ == "__main__":
    main()
