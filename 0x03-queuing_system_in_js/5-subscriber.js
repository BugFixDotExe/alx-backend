import redis from 'redis';
const client = redis.createClient();

const redisConnect = new Promise((resolve, reject) => {
  client.on('connect', () => {
    console.log('Redis client connected to the server');
    resolve();
  });
  client.on('error', (err) => {
    console.log(`Redis client not connected to the server: ${err}`);
    reject();
  });
});

redisConnect.then(() => { 
  client.subscribe('holberton school channel');
  client.on('message', (channel, message) => {
    if (message === "KILL_SERVER") {
      console.log(message); 
      client.unsubscribe('holberton school channel');
      client.quit();  // Gracefully close the connection
    } else {
      console.log(message);  // Handle other messages
    }
  });
});
