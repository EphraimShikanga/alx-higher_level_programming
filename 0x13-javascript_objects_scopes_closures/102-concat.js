#!/usr/bin/node

const fs = require('fs');
const [, , pathFileA, pathFileB, pathFileC] = process.argv;

const contentsFileA = fs.readFileSync(pathFileA, 'utf8');
const contentsFileB = fs.readFileSync(pathFileB, 'utf8');
const bothFiles = contentsFileA + contentsFileB;

fs.writeFileSync(pathFileC, bothFiles, 'utf8');
