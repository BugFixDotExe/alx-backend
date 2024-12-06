const kue = require('kue');

const queue = kue.createQueue();
const blackListed = ["4153518780", "4153518780"];


function sendNotification(phoneNumber, message, job, done) {
  if (blackListed.includes(phoneNumber)) {
    return done(new Error(`Phone number ${phoneNumber} is blacklisted`));
  }
  console.log(`Sending notification to ${phoneNumber}: ${message}`);
  job.progress(0, 50);
  setTimeout(() => {
    job.progress(50, 100)
    done(); // Signal job completion
  }, 1000);
}


queue.process("push_notification_code_2", 2, (job, done) => {
  const { phoneNumber, message } = job.data;
  sendNotification(phoneNumber, message, job, done)
})