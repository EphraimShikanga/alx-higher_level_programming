#!/usr/bin/node

const args = process.argv[2];
const argAsInt = parseInt(args);
if (isNaN(argAsInt)) {
    console.log('Missing size');
} else {
    for (let i = 0; i < argAsInt; i++) {
        console.log('X'.repeat(argAsInt));
    }
}