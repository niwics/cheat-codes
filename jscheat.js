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
   console.error(error);
 }
 
 /*
  * Data types
  */
 console.log(typeof 42); // expected output: "number"
 typeof (() => {}) === 'function'; // true
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
 delete values.toDelete
 console.log("Object attribute 'one': " + myObject.one);
 // iterate through keys
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
 words.push("four");
 words = words.filter(word => word.length > 3);
 // includes (in array) function
 words.includes('one');


 /*
  * Maps
  * In JS, usually 
  */
 let myMap = new Map([["a", 1], ["b", 2], ["c", 3]]);
// iterate over map with key and value
for (let [k, v] of myMap) {
  console.log(k, v);
}


// Strings
const s = "abcdef";
let newString = s.substr(1, 2); // = "bc" (second param is length)
newString = s.slice(1, 2); // = "b" (second param is end index)
newString = s.slice(1, -1); // = "bcde" (negative index is counted from the end)
// array implode - join
const numbersArray = ["one", "two", "three"];
numbersArray.join(); // "one,two,three"
numbersArray.join(", "); // "one, two, three"
// regexps
const url="http://pes.cz";
url.match(/(https?):\/\/'/)  // [ 'http://', 'http', index: 0, input: 'http://pes.cz', groups: undefined ]
url.match(/abcd/)  // null
url.match(/\d{4}/)  // null

// Dates
const today = new Date(); // 2018-12-24T12:13:14.000Z
today.getMonth(); // 11 < minus one!
// reads in UTC
const d1 = new Date('2018-12-24');  // 2018-12-24T00:00:00.000Z
// reads in local timezone (in this example "+1:00") and stores in UTC
const d2 = new Date(2018, 11, 24);  // 2018-12-23T23:00:00.000Z
d2.toDateString();  // "Mon Dec 24 2018"

// print JSON
obj = {attr: "myattr"}
console.log(JSON.stringify(obj, null, 2))