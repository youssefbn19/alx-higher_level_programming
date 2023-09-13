#!/usr/bin/node

const args = process.argv;
const fs = require('fs');

let content = fs.readFileSync(args[2], 'utf-8');
content += fs.readFileSync(args[3], 'utf-8');

fs.writeFileSync(args[4], content);
