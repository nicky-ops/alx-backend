const kue = require('kue');

const queue = kue.createQueue();

function createPushNotificationsJobs(jobs, queue) {
  if (Array.isArray(jobs) != true) {
    console.error('Jobs is not an array');
  }
  jobs.forEach((jobData) => {
    const job = queue.create('push_notification_code_3', jobData)
    .save((err) => {
      if (!err) {
        console.log(`Notification job created: ${job.id}`);
      } else {
        console.error(`Failed to create notification job`, err);
      }
    });

    job.on('complete', () => {
      console.log(`Notification job ${job.id} completed`);
    })
    job.on('failed', () => {
      console.log(`Notification job ${job.id} failed`);
    });
    job.on('progress', (progress) => {
      console.log(`Notification job ${job.id} ${progress}% complete`);
    });
  });
}


module.exports = createPushNotificationsJobs;
