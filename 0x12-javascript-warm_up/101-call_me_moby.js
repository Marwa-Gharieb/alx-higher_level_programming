#!/usr/bin/node
function callMeMoby (times, job) {
  for (let i = 0; i < times; i++) {
    job();
  }
}

module.exports.callMeMoby = callMeMoby;
