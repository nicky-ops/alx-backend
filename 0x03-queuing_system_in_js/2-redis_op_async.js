import { createClient } from 'redis';
import { promisify } from 'util';

const client = createClient();

client.on('error', (err) => console.log('Redis client not connected to the server:', err.toString()));

client.on('connect', () => console.log('Redis client connected to the server'));

function setNewSchool(schoolName, value) {
  client.set(schoolName, value, (err, reply) => {
    if (err) {
      console.error('Error setting value:', err);
    } else {
      console.log('Reply:', reply);
    }
  });
}

const getAsync = promisify(client.get).bind(client);

async function displaySchoolValue(schoolName) {
  try {
    const reply = await getAsync(schoolName);
    console.log(reply);
  } catch (err) {
    console.error('Error getting value:', err);
  }
}
displaySchoolValue('Holberton');
setNewSchool('HolbertonSanFrancisco', '100');
displaySchoolValue('HolbertonSanFrancisco');
