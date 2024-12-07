// task 3: Node Redis client and async operations
import { createClient, print } from 'redis';
import { promisify } from 'util';

const client = createClient({
  url: 'redis://localhost:6379'
});

function setNewSchool (schoolName, value) {
  client.set(`${schoolName}`, `${value}`, print);
}

async function displaySchoolValue (schoolName) {
  try {
    const getAsync = promisify(client.get).bind(client);
    const value = await getAsync(schoolName);
    console.log(value);
  } catch (err) {
    console.log(err);
  }
}

async function main () {
  await displaySchoolValue('Holberton');
  setNewSchool('HolbertonSanFrancisco', '100');
  await displaySchoolValue('HolbertonSanFrancisco');
}

client.on('connect', () => {
  console.log('Redis client connected to the server');
  main();
});

client.on('error', (err) => {
  console.log('Redis client not connected to the server:', err.toString());
});
