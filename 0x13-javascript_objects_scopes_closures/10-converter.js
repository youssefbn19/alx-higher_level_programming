#!/usr/bin/node

exports.converter = function (base) {
  function convertNum (number) {
    if (base === 10) return number;
    return number.toString(base);
  }
  return convertNum;
};
