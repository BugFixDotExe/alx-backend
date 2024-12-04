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

function publishMessage(message, time) { 
  setTimeout(() => {
    console.log(`About to send ${message}`);
  }, time);
  client.publish('holberton school channel', message);
}

publishMessage("Holberton Student #1 starts course", 100);
publishMessage("Holberton Student #2 starts course", 200);
publishMessage("KILL_SERVER", 300);
publishMessage("Holberton Student #3 starts course", 400);