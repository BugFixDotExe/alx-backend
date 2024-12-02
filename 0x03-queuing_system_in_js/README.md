#  0x03. Queuing System in JS

For this project, I began practicing Queueing for my specialization into backend development by using Redis.

**Tags: |Back-end JavaScript ES6 Redis NodeJS ExpressJS Kue|**

## Tasks :page_with_curl:


* **0. Install a redis instance**
  * [ dump.rdb](./dump.rdb)

* **1. Node Redis Client**
    * [0-redis_client](./0-redis_client.js): Install node_redis using npm
    
    Using Babel and ES6, write a script named 0-redis_client.js. It should connect to the Redis server running on your machine:
    
    It should log to the console the message Redis client connected to the server when the connection to Redis works correctly
    It should log to the console the message Redis client not connected to the server: ERROR_MESSAGE when the connection to Redis does not work
    Requirements:
    
    To import the library, you need to use the keyword import


* **2. Node Redis client and basic operations**
    * [1-redis_op](./1-redis_op.js): In a file 1-redis_op.js, copy the code you previously wrote (0-redis_client.js).
    
    Add two functions:
    
    setNewSchool:
    It accepts two arguments schoolName, and value.
    It should set in Redis the value for the key schoolName
    It should display a confirmation message using redis.print
    displaySchoolValue:
    It accepts one argument schoolName.
    It should log to the console the value for the key passed as argument
    At the end of the file, call:
    
    displaySchoolValue('Holberton');
    setNewSchool('HolbertonSanFrancisco', '100');
    displaySchoolValue('HolbertonSanFrancisco');
    Requirements:
    
    Use callbacks for any of the operation, we will look at async operations later

* **3. Node Redis client and async operations**
  * [2-redis_op_async.js](./2-redis_op_async.js): In a file 2-redis_op_async.js, let’s copy the code from the previous exercise (1-redis_op.js)
  
  Using promisify, modify the function displaySchoolValue to use ES6 async / await
  
  Same result as 1-redis_op.js

* **4. Node Redis client and advanced operations**
  * [4-redis_advanced_op](./4-redis_advanced_op.js): In a file named 4-redis_advanced_op.js, let’s use the client to store a hash value
  
  Create Hash:
  Using hset, let’s store the following:
  
  The key of the hash should be HolbertonSchools
  It should have a value for:
  Portland=50
  Seattle=80
  New York=20
  Bogota=20
  Cali=40
  Paris=2
  Make sure you use redis.print for each hset
  Display Hash:
  Using hgetall, display the object stored in Redis. It should return the following:
  
  Requirements:
  
  Use callbacks for any of the operation, we will look at async operations later

  

  * **5. Node Redis client publisher and subscriber**
    * [5-subscriber, 5-publisher](./5-subscriber.js,./5-publisher.js): In a file named 5-subscriber.js, create a redis client:
    
    On connect, it should log the message Redis client connected to the server
    On error, it should log the message Redis client not connected to the server: ERROR MESSAGE
    It should subscribe to the channel holberton school channel
    When it receives message on the channel holberton school channel, it should log the message to the console
    When the message is KILL_SERVER, it should unsubscribe and quit
    In a file named 5-publisher.js, create a redis client:
    
    On connect, it should log the message Redis client connected to the server
    On error, it should log the message Redis client not connected to the server: ERROR MESSAGE
    Write a function named publishMessage:
    It will take two arguments: message (string), and time (integer - in ms)
    After time millisecond:
    The function should log to the console About to send MESSAGE
    The function should publish to the channel holberton school channel, the message passed in argument after the time passed in arguments
    At the end of the file, call:

    
    
    * **6. Create the Job creator**
        * [6-job_creator.js](./6-job_creator.js): In a file named 6-job_creator.js:
        
        Create a queue with Kue
        Create an object containing the Job data with the following format:
        {
          phoneNumber: string,
          message: string,
        }
        Create a queue named push_notification_code, and create a job with the object created before
        When the job is created without error, log to the console Notification job created: JOB ID
        When the job is completed, log to the console Notification job completed
        When the job is failing, log to the console Notification job failed
        bob@dylan:~$ npm run dev 6-job_creator.js 
        
        > queuing_system_in_js@1.0.0 dev /root
        > nodemon --exec babel-node --presets @babel/preset-env "6-job_creator.js"
        
        [nodemon] 2.0.4
        [nodemon] to restart at any time, enter `rs`
        [nodemon] watching path(s): *.*
        [nodemon] watching extensions: js,mjs,json
        [nodemon] starting `babel-node --presets @babel/preset-env 6-job_creator.js`
        Notification job created: 1
        
        Nothing else will happen - to process the job, go to the next task!
        
        If you execute multiple time this file, you will see the JOB ID increasing - it means you are storing new job to process…
        

        * **7. Create the Job processor**
            * [6-job_processor](./6-job_processor.js): In a file named 6-job_processor.js:
            
            Create a queue with Kue
            Create a function named sendNotification:
            It will take two arguments phoneNumber and message
            It will log to the console Sending notification to PHONE_NUMBER, with message: MESSAGE
            Write the queue process that will listen to new jobs on push_notification_code:
            Every new job should call the sendNotification function with the phone number and the message contained within the job data
            Requirements:
            
            You only need one Redis server to execute the program
            You will need to have two node processes to run each script at the same time
            You muse use Kue to set up the queue

            
            

            * **8. Track progress and errors with Kue: Create the Job creator**
                * [7-job_creator](./7-job_creator.js): Create a queue with Kue
                Write a loop that will go through the array jobs and for each object:
                Create a new job to the queue push_notification_code_2 with the current object
                If there is no error, log to the console Notification job created: JOB_ID
                On the job completion, log to the console Notification job JOB_ID completed
                On the job failure, log to the console Notification job JOB_ID failed: ERROR
                On the job progress, log to the console Notification job JOB_ID PERCENTAGE% complete

                
                * **9. Track progress and errors with Kue: Create the Job processor**
                    * [7-job_processor](./7-job_processor.js): In a file named 7-job_processor.js:
                    
                    Create an array that will contain the blacklisted phone numbers. Add in it 4153518780 and 4153518781 - these 2 numbers will be blacklisted by our jobs processor.
                    
                    Create a function sendNotification that takes 4 arguments: phoneNumber, message, job, and done:
                    
                    When the function is called, track the progress of the job of 0 out of 100
                    If phoneNumber is included in the “blacklisted array”, fail the job with an Error object and the message: Phone number PHONE_NUMBER is blacklisted
                    Otherwise:
                    Track the progress to 50%
                    Log to the console Sending notification to PHONE_NUMBER, with message: MESSAGE
                    Create a queue with Kue that will proceed job of the queue push_notification_code_2 with two jobs at a time.
                    
                    Requirements:
                    
                    You only need one Redis server to execute the program
                    You will need to have two node processes to run each script at the same time
                    You muse use Kue to set up the queue
                    Executing the jobs list should log to the console the following:
                    

                    * **10. Writing the job creation function**
                        * [8-job.js](./8-job.js): In a file named 8-job.js, create a function named createPushNotificationsJobs:
                        
                        It takes into argument jobs (array of objects), and queue (Kue queue)
                        If jobs is not an array, it should throw an Error with message: Jobs is not an array
                        For each job in jobs, create a job in the queue push_notification_code_3
                        When a job is created, it should log to the console Notification job created: JOB_ID
                        When a job is complete, it should log to the console Notification job JOB_ID completed
                        When a job is failed, it should log to the console Notification job JOB_ID failed: ERROR
                        When a job is making progress, it should log to the console Notification job JOB_ID PERCENT% complete
                        
                
                        * **11. Writing the test for job creation**
                            * [8-job.test](./8-job.test.js):Now that you created a job creator, let’s add tests:
                            
                            Import the function createPushNotificationsJobs
                            Create a queue with Kue
                            Write a test suite for the createPushNotificationsJobs function:
                            Use queue.testMode to validate which jobs are inside the queue
                            etc.
                            Requirements:
                            
                            Make sure to enter the test mode without processing the jobs before executing the tests
                            Make sure to clear the queue and exit the test mode after executing the tests
                            
                            * **12. In stock?**
                                * [9-stock](./9-stock.js): In a file named 8-job.js, create a function named createPushNotificationsJobs:
                                
                                It takes into argument jobs (array of objects), and queue (Kue queue)
                                If jobs is not an array, it should throw an Error with message: Jobs is not an array
                                For each job in jobs, create a job in the queue push_notification_code_3
                                When a job is created, it should log to the console Notification job created: JOB_ID
                                When a job is complete, it should log to the console Notification job JOB_ID completed
                                When a job is failed, it should log to the console Notification job JOB_ID failed: ERROR
                                When a job is making progress, it should log to the console Notification job JOB_ID PERCENT% complete