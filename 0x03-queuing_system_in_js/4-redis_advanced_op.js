import { createClient, print} from 'redis';

const client = createClient();

client.on('error', (err) => console.log('Redis client not connected to the server:', err.toString()));

client.on('connect', () => console.log('Redis client connected to the server'));

const key = 'HolbertonSchools';
const values = {
  Portland: 50,
  Seattle: 80,
  'New York': 20,
  Bogota: 20,
  Cali: 40,
  Paris: 2
};
for (const [field, value] of Object.entries(values)) {
  client.hset(key, field, value, print);
}

client.hgetall(key, (err, result) => {
  if (err) {
    console.error(`Error retrieving hash: ${err.message}`);
    return;
  }
  console.log(result);
});

