# Example prompts for AI agents (tool: sste/official-fuel-prices)

- "Find the cheapest diesel near 48.8566, 2.3522." → `{"latitude":48.8566,"longitude":2.3522,"radiusKm":5,"fuelTypes":["diesel"],"maxResults":5}`
- "Get current petrol prices within 10 km of 40.4168, -3.7038." → `{"latitude":40.4168,"longitude":-3.7038,"radiusKm":10,"fuelTypes":["gasoline_95"],"maxResults":10}`
- "Compare nearby fuel stations by price around Milan Duomo." → `{"latitude":45.4642,"longitude":9.19,"radiusKm":3,"sortBy":"price","maxResults":20}`
- "Return official fuel price data for an AI travel agent planning a stop near Perth." → `{"latitude":-31.9523,"longitude":115.8613,"radiusKm":15,"fuelTypes":["gasoline_91"],"maxResults":5}`

Rules of thumb for agents: always pass coordinates (no geocoding), a fuel type and a small `maxResults`
(billing is per row: $0.005 per run + $0.0005 per row). Read `currency` and `unit` before comparing countries.
