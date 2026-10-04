#!/usr/bin/env bash
# Cheapest diesel within 3 km of central Paris (official French data, DGCCRF).
# Requires: APIFY_TOKEN (https://console.apify.com/settings/integrations)
curl -s -X POST "https://api.apify.com/v2/acts/sste~official-fuel-prices/run-sync-get-dataset-items" \
  -H "Authorization: Bearer ${APIFY_TOKEN:?set APIFY_TOKEN}" \
  -H "Content-Type: application/json" \
  -d '{"latitude":48.8566,"longitude":2.3522,"radiusKm":3,"fuelTypes":["diesel"],"maxResults":10}'
