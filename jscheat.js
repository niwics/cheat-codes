/**
 * Javascript Cheat Sheet
 * Author: niwi.cz
 */

 /** Exports/imports */
// ------ in lib/MyComponent.js_
// exports.MyComponent1 = () => {}
// export const MyComponent2 = () => {}
// export function MyComponent3 () {}
// export class MyComponent4 () {}
// ------ in index.js:
// old style import
// const {MyComponent} = require('./lib/MyComponent.js');
// new style import (ES modules)
// import {MyComponent} from './lib/MyComponent.js'

/*
* Variables
* Since ES6 const and let were added.
*/
// constant (but is not immutable inside!); block-scoped
const myConstVariable = 1;
// could be reassigned; block-scoped
let myVariable = 2;
// generic, should be reassigned, function-scoped (when declared in function) or globally scoped
var myVariable2 = 3;

// "classical" constants in module scope
const PRODUCTION_ENV = false;  // upper case by convention


// shortcut for calling anonymous function
//() => myVariable

try {
  throw "My test exception!" // all object could be thrown
}
catch (error) {
  if (error instanceof SpecificError)
    console.error("Specific error: " + error);
  else
    throw(error)  // rethrow with preserved stack-trace
}
 
/*
 * Data types
 */
console.log(typeof 42); // expected output: "number"
typeof (() => {}) === 'function'; // true
// convert string to integer
const myInt = parseInt("7");
// weird adding
const weirdResult = "7" + 1; // "71"
// object = object
Object.prototype.toString.call(myObject); // [object Null]

/*
 * Objects
 */
let myObject = {
  one: "String for first item",
  two: 2,
  toDelete: "i will be deleted"
}
myObject.three = "three"
// membership
"two" in myObject  // true
delete values.toDelete
console.log("Object attribute 'one': " + myObject.one);
// print object as JSON
console.log(JSON.stringify(players))
// print object properties
for (let property in myObject) {
  if (myObject.hasOwnProperty(property)) {
      console.log("Property name: " + property + ", value: " + myObject[property]);
  }
}

// clone object - shallow copy
const shallowCopy = Object.assign({}, myObject);
// clone object - deep copy
const deepCopy = {};
for (let prop in myObject) {
  if (myObject.hasOwnProperty(prop)) {
    deepCopy[prop] = myObject[prop];
  }
}

 // Arrays
 let words = ['one', 'two', 'three'];
 words.push("five");
 words.splice(3, 0, "four") // insert to the position 3 (and delete 0 items)
 // array size = length
 console.log(words.length)  // 5
 words = words.filter(word => word.length > 3);
 // includes (in array) function (test whether item is in array)
 words.includes('one');
 words.indexOf('two')
 // merge=concat two arrays
 const moreWords = ['six', 'seven'];
 const allWords = words.concat(moreWords);
 // sorting items - non-unicode/local aware
 const sortedWordsBasic = words.sort();
 // sorting items - unicode/local aware
 const sortedWordsUnicode = words.sort((a, b) => a.localeCompare(b));
 // clone shallow copy of array
 const wordsCloned = words.slice()


// iterating the array
// 1: old-style for cycle
for (let i = 0; i < words.length; i++) {
  console.log(words[i]);
}
// 2. using forEach (and every, some, filter, map, reduce, reduceRight)
words.forEach(e => {
  console.log(e);
});
// 3. for..in - loops through the properties of an object - see Objects
// 4. for..of - ES2015+, loops through the values of an iterable objects
for (const e of words)
  console.log(e);

 /*
  * Maps
  */
let myMap = new Map([["a", 1], ["b", 2], ["c", 3]]);
// iterate over map with key and value
for (let [k, v] of myMap) {
  console.log(k, v);
}
// keys to array (Map.keys() returns just iterator!)
const keysArray = Array.from(myMap.keys());
// keys are sorted just by insertion order => to sort
// it by sorting function, you must re-insert elements into the new Map
var myMapSorted = new Map([...map.entries()].sort());


// Strings
const s = "abcdef";
const sLower = s.toLowerCase();
const sUpper = s.toUpperCase();
let newString = s.substr(1, 2); // = "bc" (second param is length)
newString = s.slice(1, 2); // = "b" (second param is end index)
newString = s.slice(1, -1); // = "bcde" (negative index is counted from the end)
// array implode - join
const numbersArray = ["one", "two", "three"];
numbersArray.join(); // "one,two,three"
numbersArray.join(", "); // "one, two, three"
// array explode - split
const splitted = "my three words".split(" "); // ["my", "three", "words"]
// string literals
const tuvData = `
Porsche 911	26	2,5
Mercedes B	39	2,6
Mercedes GLK	50	2,6
`;
// substring searching
s.indexOf("x"); // -1
s.indexOf("de"); // 3
// regexps
const url="http://pes.cz";
url.match(/(https?):\/\/'/)  // [ 'http://', 'http', index: 0, input: 'http://pes.cz', groups: undefined ]
url.match(/abcd/)  // null
url.match(/\d{4}/)  // null

// Dates (raw)
const today = new Date(); // 2018-12-24T12:13:14.000Z
today.getMonth(); // 11 < minus one!
// reads in UTC
const d1 = new Date('2018-12-24');  // 2018-12-24T00:00:00.000Z
// reads in local timezone (in this example "+1:00") and stores in UTC
const d2 = new Date(2018, 11, 24);  // 2018-12-23T23:00:00.000Z
d2.toDateString();  // "Mon Dec 24 2018"

// Dates (moment.js)
import moment from 'moment'
moment.locale('cs')
const todayM = moment() // object with actual datetime
todayM.format()
todayM.hours()
todayM.isoWeekday()
const exampleDate = moment('2020-02-03')
const todayMidnightM = moment(0, "HH");  // today midnight
moment(date).from(thisMidnight)
thisMidnight.add(numberOfDaysToAdd, 'day').format("YYYY-MM-DD")
moment(effectiveOrCreatedDate).format('llll')
// dates diff



// print JSON
obj = {attr: "myattr"}
console.log(JSON.stringify(obj, null, 2))

// reading files
const path = require('path');
const fs = require('fs');
const directoryPath = path.join(__dirname, 'mydir');
fs.readdir(directoryPath, (err, files) => {
  //handling error
  if (err) {
    console.log('Unable to scan directory: ' + err);
    return;
  }
  for (file of files) {
    console.log(file);
  }
});