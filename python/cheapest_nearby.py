"""Cheapest fuel stations near a point (France, Spain, Italy, Western Australia).

pip install apify-client
APIFY_TOKEN=... python cheapest_nearby.py 41.3874 2.1686 gasoline_95
"""
import os
import sys

from apify_client import ApifyClient

lat, lon = float(sys.argv[1]), float(sys.argv[2])
fuel = sys.argv[3] if len(sys.argv) > 3 else "diesel"

client = ApifyClient(os.environ["APIFY_TOKEN"])
run = client.actor("sste/official-fuel-prices").call(run_input={
    "latitude": lat, "longitude": lon, "radiusKm": 5, "fuelTypes": [fuel], "maxResults": 10,
})
for row in client.dataset(run["defaultDatasetId"]).iterate_items():
    name = row.get("stationName") or row.get("brand") or row.get("address")
    print(f'{row["price"]:.3f} {row["currency"]}/{row["unit"]}  {row["distanceKm"]:>5} km  {name}')
