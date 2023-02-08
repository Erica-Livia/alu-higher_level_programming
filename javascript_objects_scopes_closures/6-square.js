#!/usr/bin/node
class Square extends require('./5-square') {
    constructor (size) {
        super(size, size);
    }

    charPrint(c) {
       if (c == undefined) {
        c = 'X';
       } 
       for (let i = 0; i < this.height; i++) {
        console.log(c.repeat(this.width));
       }
    }
}
module.exports = Square;
