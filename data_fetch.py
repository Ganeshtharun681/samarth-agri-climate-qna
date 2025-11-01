import requests
import pandas as pd
import time
import os

# ===============================
# CONFIGURATION
# ===============================
# Replace these with your actual API keys and resource IDs

# These are sample resource IDs — replace with the ones from data.gov.in for your chosen datasets
IMD_RESOURCE_ID = "d24d3d66-f71b-4652-8b3b-81cc5d42d3bf"
AGRI_RESOURCE_ID = "9c4eeb10-b2a4-406c-9025-aeaa3011cc48"

# ===============================
# HELPER FUNCTION
# ===============================
def fetch_data_from_datagovin(resource_id, limit=1000):
    """Fetch paginated data from data.gov.in and return as a Pandas DataFrame."""
    API_KEY = "579b464db66ec23bdd000001b366737152f347f14a9d6ff8ab457c65"

    base_url = f"https://api.data.gov.in/resource/{resource_id}?api-key={API_KEY}&format=json&limit={limit}"
    offset = 0
    all_records = []
    API_KEY = "579b464db66ec23bdd000001b366737152f347f14a9d6ff8ab457c65"

    print(f"Fetching data from resource {resource_id} ...")

    while True:
        url = f"{base_url}&offset={offset}"
        response = requests.get(url)

        if response.status_code != 200:
            print(f"❌ Error fetching data: {response.status_code}")
            break

        data = response.json()
        records = data.get("records", [])
        if not records:
            break

        all_records.extend(records)
        print(f"Fetched {len(all_records)} records so far...")
        offset += limit

        # Small delay to respect API rate limits
        time.sleep(1)

        # Stop if less than limit records (end of dataset)
        if len(records) < limit:
            break

    print(f" Done. Total {len(all_records)} records fetched.\n")

    return pd.DataFrame(all_records)

# ===============================
# FETCH DATASETS
# ===============================
if __name__ == "__main__":

    # Ensure the 'data' folder exists
    os.makedirs("data", exist_ok=True)

    # Fetch Rainfall Data (IMD)
    rainfall_df = fetch_data_from_datagovin(IMD_RESOURCE_ID)
    rainfall_df.to_csv("data/rainfall_live.csv", index=False)
    print("Saved rainfall data  data/rainfall_live.csv")

    # Fetch Crop Production Data (Agriculture)
    crop_df = fetch_data_from_datagovin(AGRI_RESOURCE_ID)
    crop_df.to_csv("data/crop_production_live.csv", index=False)
    print("Saved crop production data  data/crop_production_live.csv")
