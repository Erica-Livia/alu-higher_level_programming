#!/usr/bin/node
exports.nbOccurences = function (list, searchElement) {
  return list.reduce((acc, curr) => {
    return acc + (curr === searchElement ? 1 : 0);
  }, 0);
};
