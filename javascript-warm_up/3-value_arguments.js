#!/usr/bin/node
if (ProcessingInstruction.argv[2]) {
    console.log(process.argv[2]);
}
else {
    console.log('No argument');
}