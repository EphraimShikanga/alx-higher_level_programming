#!/usr/bin/node

const occUserIds = require ('./101-data.js');

const userIdsOcc = {};
for (const userId in occUserIds) {
    if (userIdsOcc[occUserIds[userId]] === undefined) {
        userIdsOcc[occUserIds[userId]] = [];
    }
    userIdsOcc[occUserIds[userId]].push(userId);
}

console.log(userIdsOcc);