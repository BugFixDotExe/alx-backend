import redis from 'redis';

const client = redis.createClient();

const redisConnect = new Promise((resolve, reject) => { 
  client.on('connect', () => {
    console.log('Redis client connected to the server');
      resolve();
  });
  client.on('error', err => {
    console.log(`Redis client not connected to the server: ${err}`)
    reject(err);
  });
})

function setNewSchool(schoolName, value) {
  redisConnect.then(() => { 
    client.set(schoolName, value, redis.print);
  })
}

function displaySchoolValue(schoolName) { 
  console.log(client.get(schoolName));
}

displaySchoolValue('Holberton');
setNewSchool('HolbertonSanFrancisco', '100');
displaySchoolValue('HolbertonSanFrancisco');