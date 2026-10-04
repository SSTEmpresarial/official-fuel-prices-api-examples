// Cheapest fuel stations near a point. npm install apify-client
// APIFY_TOKEN=... node cheapest-nearby.mjs 45.4642 9.19 diesel
import { ApifyClient } from 'apify-client';

const [lat, lon, fuel = 'diesel'] = process.argv.slice(2);
const client = new ApifyClient({ token: process.env.APIFY_TOKEN });
const run = await client.actor('sste/official-fuel-prices').call({
    latitude: Number(lat), longitude: Number(lon), radiusKm: 5, fuelTypes: [fuel], maxResults: 10,
});
const { items } = await client.dataset(run.defaultDatasetId).listItems();
console.table(items.map((r) => ({
    price: `${r.price} ${r.currency}/${r.unit}`, km: r.distanceKm, station: r.stationName ?? r.brand ?? r.address, updated: r.priceUpdatedAt,
})));
