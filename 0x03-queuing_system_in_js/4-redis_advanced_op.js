// Node Redis client and advanced operations
import { createClient, print } from 'redis';
const client = createClient({
  url: 'redis://localhost:6379'
});

client.on('connect', () => {
  console.log('Redis client connected to the server');
});

function setHash (hashKey, fieldName, fieldVal) {
  client.hset(hashKey, fieldName, fieldVal, print);
}

function printHash (hashKey) {
  client.hgetall(hashKey, (_err, value) => console.log(value));
}

const HolbertonSchools = {
  Portland: 50,
  Seattle: 80,
  'New York': 20,
  Bogota: 20,
  Cali: 40,
  Paris: '2'
};

for (const [field, value] of Object.entries(HolbertonSchools)) {
  setHash('HolbertonSchools', field, value);
}
printHash('HolbertonSchools');
