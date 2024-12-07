// Create the job ceator
const kue = require('kue');
const queue = kue.createQueue({ name: 'push_notification_code' });
const jobData = {
  phoneNumber: '09054604494',
  message: 'Have a great day'
};

const job = queue.create('push_notification_code', jobData)
  .on('complete', () => {
    console.log('Notification job completed');
  })
  .on('failed', () => {
    console.log('Notification job failed');
  })
  .save((err) => {
    if (!err) {
      console.log('Notification job created:', job.id);
    }
  });
