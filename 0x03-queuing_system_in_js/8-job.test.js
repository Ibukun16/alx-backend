#!/usr/bin/yarn test
import sinon from 'sinon';
import { expect } from 'chai';
import { createQueue } from 'kue';
import createPushNotificationsJobs from './8-jobs.js';
import { describe, it, before, after, afterEach } from 'mocha';

describe('Test createPushNotificationsJobs function', () => {
  const spyMonitor = sinon.spy(console);
  const QUEUE = createQueue({ name: 'push_notification_code_test' });

  before(() => {
    QUEUE.testMode.enter(true);
  });

  after(() => {
    QUEUE.testMode.clear();
    QUEUE.testMode.exit();
  });

  afterEach(() => {
    spyMonitor.log.resetHistory();
  });

  it('display an error message if jobs is not an array', () => {
    expect(
      createPushNotificationsJobs.bind(createPushNotificationsJobs, {}, QUEUE),
    ).to.throw(Error, 'Jobs is not an array');
  });

  it('Test if jobs are created and add jobs to the queue with the correct type', (done) => {
    expect(QUEUE.testMode.jobs.length).to.equal(0);
    const jobDetails = [
      {
        phoneNumber: '4153518780',
        message: 'Use the code 1617 to verify your account',
      },
      {
        phoneNumber: '4153518781',
        message: 'Use the code 1956 to verify your account',
      },
    ];
    createPushNotificationsJobs(jobDetails, QUEUE);
    expect(QUEUE.testMode.jobs.length).to.equal(2);
    expect(QUEUE.testMode.jobs[0].data).to.deep.equal(jobDetails[0]);
    expect(QUEUE.testMode.jobs[0].type).to.equal('push_notification_code_3');
    QUEUE.process('push_notification_code_3', () => {
      expect(
        spyMonitor.log.calledWith(
          'Notification job created:',
          QUEUE.testMode.jobs[0].id,
        ),
      ).to.be.true;
      done();
    });
  });

  it('registers the progress event handler for a job', (done) => {
    QUEUE.testMode.jobs[0].addListener('progress', () => {
      expect(
        spyMonitor.log.calledWith(
          'Notification job',
          QUEUE.testMode.jobs[0].id,
          '25% complete',
        ),
      ).to.be.true;
      done();
    });
    QUEUE.testMode.jobs[0].emit('progress', 25);
  });

  it('registers the failed event handler for a job', (done) => {
    QUEUE.testMode.jobs[0].addListener('failed', () => {
      expect(
        spyMonitor.log.calledWith(
          'Notification job',
          QUEUE.testMode.jobs[0].id,
          'failed:',
          'Failed to send',
        ),
      ).to.be.true;
      done();
    });
    QUEUE.testMode.jobs[0].emit('failed', new Error('Failed to send'));
  });

  it('registers the complete event handler for a job', (done) => {
    QUEUE.testMode.jobs[0].addListener('complete', () => {
      expect(
        spyMonitor.log.calledWith(
          'Notification job',
          QUEUE.testMode.jobs[0].id,
          'completed',
        ),
      ).to.be.true;
      done();
    });
    QUEUE.testMode.jobs[0].emit('complete');
  });
});
