// task 2: Node Redis client and basic operations
import { createClient, print } from 'redis';

function setNewSchool (schoolName, value) {
  client.set(`${schoolName}`, `${value}`, print);
}

function displaySchoolValue (schoolName) {
  client.get(`${schoolName}`, (err, value) => {
    if (err) {
      console.log('Error getting key:', err);
    } else {
      console.log(value);
    }
  });
}

const client = createClient({
  url: 'redis://localhost:6379'
});

client.on('connect', () => {
  console.log('Redis client connected to the server');
});

client.on('error', (err) => {
  console.log('Redis client not connected to the server:', err.toString());
});

displaySchoolValue('Holberton');
setNewSchool('HolbertonSanFrancisco', '100');
displaySchoolValue('HolbertonSanFrancisco');
