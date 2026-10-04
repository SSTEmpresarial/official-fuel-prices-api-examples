# Official Fuel Prices API — examples (France, Spain, Italy, Western Australia)

Docs and guides: https://fuel-prices-api.pages.dev/?utm_source=github&utm_medium=referral&utm_campaign=examples

Runnable examples for **[Official Fuel Prices](https://apify.com/sste/official-fuel-prices?utm_source=github&utm_medium=referral&utm_campaign=examples)**,
an API that returns station-level petrol, diesel, LPG, CNG and hydrogen prices for ~46,000 stations from official
government open data (DGCCRF France, MITECO Spain, MIMIT Italy, FuelWatch Western Australia), normalized into one
JSON schema with coordinates, ISO timestamps, currency, unit, source and licence on every row.

| Example | What it does |
|---|---|
| [`curl/cheapest-diesel-paris.sh`](curl/cheapest-diesel-paris.sh) | One HTTP call: 10 cheapest diesel stations within 3 km of Paris |
| [`python/cheapest_nearby.py`](python/cheapest_nearby.py) | CLI: cheapest stations near any coordinates |
| [`python/brand_summary_pandas.py`](python/brand_summary_pandas.py) | Median price by brand around Madrid with pandas |
| [`javascript/cheapest-nearby.mjs`](javascript/cheapest-nearby.mjs) | Node.js: cheapest stations near a point |
| [`mcp/`](mcp/) | Claude Desktop / Cursor config and example prompts for AI agents |

## Setup
1. Get an Apify API token: https://console.apify.com/settings/integrations (free account; pay per use).
2. `export APIFY_TOKEN=...`
3. Run any example.

## MCP (AI agents)
Server URL: `https://mcp.apify.com?tools=sste/official-fuel-prices` — works with Claude, Cursor, VS Code and other
MCP clients (OAuth sign-in on first use). Local: `npx @apify/actors-mcp-server --tools sste/official-fuel-prices`.

## Pricing
$0.005 per run + $0.0005 per price row (a "10 cheapest stations" query ≈ $0.01).

## Data sources and licences
France: data.economie.gouv.fr (DGCCRF), Licence Ouverte v2.0 · Spain: Geoportal Gasolineras (MITECO), reuse under
Ley 37/2007 · Italy: MIMIT Osservaprezzi, IODL 2.0 · Western Australia: [FuelWatch](https://www.fuelwatch.wa.gov.au).
Independent project, not affiliated with these agencies. Examples are MIT-licensed.
