#!/usr/bin/node

exports.converter = function (base) {
  function myConvert (num) {
    return num.toString(base);
  }
  return myConvert;
};
