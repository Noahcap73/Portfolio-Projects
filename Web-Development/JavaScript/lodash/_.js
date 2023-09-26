//Recreating some methods from lodash.js library

const _ = {
  clamp(num, lowNum, upperNum) {
    let lowerClampedValue = Math.max(num, lowNum);
    let clampedValue = Math.min(lowerClampedValue, upperNum);
    return clampedValue;
  },

  inRange(number, start, end) {
    if (end === undefined) {
      end = start;
      start = 0;
    }
    if (start > end) {
      const temp = end;
      end = start;
      start = temp;
    }
    const isInRange = Boolean(start <= number && number < end);
    return isInRange;
  },

  words(str) {
    return str.split(" ");
  },

  pad(str, length) {
    if (length <= str.length) {
      return str;
    }
    const startPaddingLength = Math.floor((length - str.length) / 2);
    const endPaddingLength = length - str.length - startPaddingLength;
    const paddedString = `${" ".repeat(startPaddingLength)}${str}${" ".repeat(
      endPaddingLength
    )}`;
    return paddedString;
  },

  has(obj, key) {
    const hasValue = Boolean(obj[key] != undefined);
    return hasValue;
  },

  invert(obj) {
    let invertedObj = {};
    for (let key in obj) {
      orgValue = obj[key];
      invertedObj[orgValue] = key;
    }
    return invertedObj;
  },

  findKey(obj, predicate) {
    for (let key in obj) {
      value = obj[key];
      predicateReturnValue = predicate(value);
      if (predicateReturnValue) {
        return key;
      } else {
        return undefined;
      }
    }
  },

  drop(arr, num) {
    if (num === undefined) {
      num = 1;
    }
    let droppedArray = arr.slice(num);
    return droppedArray;
  },

  dropWhile(arr, predicate) {
    let dropNumber = arr.findIndex((element, index) => {
      return !predicate(element, index, arr);
    });

    let droppedArray = this.drop(arr, dropNumber);
    return droppedArray;
  },

  chunk(arr, size) {
    if (size === undefined) {
      size = 1;
    }
    const arrChunks = [];
    for (let i = 0; i < arr.length; i += size) {
      let arrChunk = arr.slice(i, i + size);
      arrChunks.push(arrChunk);
    }
    return arrChunks;
  },
};

// Do not write or modify code below this line.
module.exports = _;
