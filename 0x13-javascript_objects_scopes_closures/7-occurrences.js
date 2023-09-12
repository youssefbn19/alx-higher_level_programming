#!/usr/bin/node

exports.nbOccurences = function (list, searchElement) {
  let repeat = 0;
  list.forEach(element => {
    if (element === searchElement) repeat++;
  });
  return repeat;
};
