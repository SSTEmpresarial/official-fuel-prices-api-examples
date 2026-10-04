"""Median diesel price by brand around Madrid, with pandas.

pip install apify-client pandas
"""
import os

import pandas as pd
from apify_client import ApifyClient

client = ApifyClient(os.environ["APIFY_TOKEN"])
run = client.actor("sste/official-fuel-prices").call(run_input={
    "latitude": 40.4168, "longitude": -3.7038, "radiusKm": 15, "fuelTypes": ["diesel"], "maxResults": 300,
})
df = pd.DataFrame(client.dataset(run["defaultDatasetId"]).list_items().items)
print(df.groupby("brand")["price"].agg(["count", "min", "median"]).sort_values("median").head(15))
