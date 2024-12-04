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
  const hsetOperation = new Promise((resolve, reject) => {
    client.hset("HolbertonSchools", "Portland", 50, redis.print);
    client.hset("HolbertonSchools", "Seattle", 80, redis.print);
    client.hset("HolbertonSchools", "New York", 20, redis.print);
    client.hset("HolbertonSchools", "Bogota", 50, redis.print);
    client.hset("HolbertonSchools", "Cali", 50, redis.print);
    client.hset("HolbertonSchools", "Paris", 50, redis.print);
    resolve();
  });
  hsetOperation.then(() => {
    client.hgetall('HolbertonSchools', (err, object) => { 
      console.log(object);
    })
  });
});
