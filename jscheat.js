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
// -- How to export object:
// const myobject = {}
// export {myobject}
// ------ in index.js:
// old style (CommonJS) import
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
// generic, could be reassigned, function-scoped (when declared in function) or globally scoped
var myVariable2 = 3;

// "classical" upper-case constants: primitive types only and usually on the module scope
const PRODUCTION_ENV = false;  // upper case by convention

// destructuring
const [var1, var2] = [10, 20] // var1=10, var2=20

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
if (isNaN(myInt))
  console.log("No integer value parsed :(")
// is a valid number?
const iamNumber = !isNaN("ab10num");
// convert number to string
const num = 123;
const stringVal = num.toString();
// weird adding
const weirdResult = "7" + 1; // "71"
// object = object
Object.prototype.toString.call(myObject); // [object Null]
// rounding
Math.round(3.14)  // 3  <- round to the int
Math.floor(3.14)  // 3  <- round down to the int
Math.ceil(3.14)   // 4  <- round up to the int
Number.parseFloat(3.14).toFixed(1)   // "3.1"  <- round to the predefined digits after point - returns string!
Number.parseFloat(3.141).toPrecision(3)   // "3.14"  <- returns the predefined number of digits - returns string!
3.14.toLocaleString('cs', {maximumFractionDigits: 1}) // "3,1"  <- returns string

/*
 * Objects
 */
let myObject = {
  one: "String for first item",
  two: 2,
  toDelete: "i will be deleted"
}
myObject.three = "three"
// membership (test whether the object contains the key)
"two" in myObject  // true
delete values.toDelete
console.log("Object attribute 'one': " + myObject.one);
// print object as JSON
console.log(JSON.stringify(players))
// get keys, values and both
// iterate over the own properties (=not from superclasses)
for (const key of Object.keys(myObject))
  console.log(key)  // "one", "two", "three"
for (const values of Object.values(myObject))
  console.log(key)  // "String for first item", 2, "three"
for (const [key, value] of Object.entries(myObject))
  console.log(`${key}: ${value}`)

// print object properties - old style
for (let property in myObject) {
  if (myObject.hasOwnProperty(property)) {
      console.log("Property name: " + property + ", value: " + myObject[property]);
  }
}

// clone object - shallow copy
const shallowCopy = Object.assign({}, myObject);
// clone object - deep copy
// using JSON
const deepCopy1 = JSON.parse(JSON.stringify(myObject))
// using manual iteration
const deepCopy2 = {}
for (let prop in myObject) {
  if (myObject.hasOwnProperty(prop)) {
    deepCopy2[prop] = myObject[prop];
  }
}

 // Arrays
 let words = ['one', 'two', 'three']
 words.push("five");
 words.splice(3, 0, "four") // insert to the position 3 (and delete 0 items)
 // array size = length
 console.log(words.length)  // 5
 words = words.filter(word => word.length > 3);
 // includes (in array) function (test whether item is in array = whether array contains the item)
 words.includes('one')
 words.indexOf('two')
 // filter - created the new one array
 const shortWords = words.filter(word => word.length < 4) // ['one', 'two']
 // map - modify items
 const newWords = words.map(word => word+"s") // ['ones', 'twos', 'threes', 'fours', 'fives']
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
const initialValue = 0
[1, 2, 3, 5, 7].reduce((accumulator, item) => accumulator+item, initialValue)

 /*
  * Maps
  */
let myMap = new Map([["a", 1], ["b", 2], ["c", 3]]);
myMap.set('d', 4);
myMap.set('c', 333);
myMap.has('d')
myMap.get('d')
// iterate over map with key and value
for (let [k, v] of myMap) {
  console.log(k, v);
}
// keys to array (Map.keys() returns just iterator!)
const keysArray2 = Array.from(myMap.keys());
// keys are sorted just by insertion order => to sort
// it by sorting function, you must re-insert elements into the new Map
var myMapSorted = new Map([...map.entries()].sort());

/*
 * Set
 */
const mySet = new Set()
mySet.add(2)
mySet.has(3)
mySet.delete(2)
mySet.clear()

// Strings
const singleQuotes = 'mystring'
const doubleQuotes = "mystring"
// formatting
// template literals
const variable = "MYVAR"
const templateLiteralString = `This is my templated literal string with ${variable} and its first char: ${variable[0]}`
// string literals (multiline strings) with heredoc syntax
const heredocString = `
This
is a
Multiple Line
String
`
const s = "abcdef";
// normalize string - convert locale chars to ASCII chars
const normalized = s.normalize("NFD").replace(/[\u0300-\u036f]/g, "")
const sLower = s.toLowerCase()
const sLowerLocale = s.toLocaleLowerCase()
const sUpper = s.toUpperCase()
const sUpperLocale = s.toLocaleUpperCase()
// uppercase first letter (aka UCFirst)
const ucfirst = s.charAt(0).toLocaleUpperCase() + s.slice(1)
const trimmed = " abc ".trim()  // "abc"
let newString = s.substring(1, 2); // = "bc" (second param is length)
newString = s.slice(1, 2); // = "b" (second param is end index)
newString = s.slice(1, -1); // = "bcde" (negative index is counted from the end)
// array implode - join
const numbersArray = ["one", "two", "three"];
numbersArray.join(); // "one,two,three"
numbersArray.join(", "); // "one, two, three"
// array explode - split
const splitted = "my three words".split(" "); // ["my", "three", "words"]
// substring searching
s.includes("cd")  // true
s.indexOf("x"); // -1
s.indexOf("de"); // 3
// fill string - lpad/rpad
// string.padStart(targetLength [, padString = " "])
"12".padStart(5, "0") // 00012
// regexps with unicode (https://javascript.info/regexp-unicode)
const url="http://pes.cz/koření";
url.match(/(https?):\/\/'/)  // [ 'http://', 'http', index: 0, input: 'http://pes.cz/koření', groups: undefined ]
url.match(/abcd/)  // null
url.match(/\d{4}/)  // null
url.match(/cz\/\w+/)  // cuts on unicode char: ['cz/ko', index: 11, input: 'http://pes.cz/koření', groups: undefined]
url.match(/cz\/\p{L}+/) // null - no "u" flag set!
url.match(/cz\/\p{L}+/u)  // ['cz/koření', index: 11, input: 'http://pes.cz/koření', groups: undefined]
// replace
// simple replace performs the replace just on the first occurence
"abcabc".replace("b", "_")  // "a_cabc"
// replace all
"abcabc".replace(new RegExp("b", 'g'), "_") // "a_ca_c"

const pattern = '^(query|mutation) (?<queryName>\w+)\('
const match = query.match(pattern).groups.queryName

// Dates (raw)
const today = new Date(); // 2018-12-24T12:13:14.000Z
today.getMonth(); // 11 < minus one!
// reads in UTC
const d1 = new Date('2018-12-24');  // 2018-12-24T00:00:00.000Z
// reads in local timezone (in this example "+1:00") and stores in UTC
const d2 = new Date(2018, 11, 24);  // 2018-12-23T23:00:00.000Z
d2.toDateString();  // "Mon Dec 24 2018"
d2.toISOString()  // 2018-12-23T23:00:00
d2.substring(0, 10) // 2018-12-23

// Dates (luxon.js)
import {DateTime} from "luxon"
// construct
const now = DateTime.now() // object with actual datetime
const dateFromJs = DateTime.fromJSDate(d2)
const dateFromISO = DateTime.fromISO('2022-12-24T09:08:34.123')
const dateFromSQL = DateTime.fromSQL('2022-12-24')
const thisMidnight = DateTime.now().startOf('day')
now.toJSDate() // "2021-04-20T19:11:31.598Z" - JS datetime object
const pastFromLocal = DateTime.local(2021, 4, 15, 13,33)
// formatting
pastFromLocal.toISO() // '2021-04-15T13:33:00.000+02:00'
pastFromLocal.toISODate() // '2021-04-15'
pastFromLocal.toSQL() // '2021-04-15 13:33:00.000 +02:00'
pastFromLocal.toSQLDate() // '2021-04-15'
pastFromLocal.toSQLTime() // '13:33:00.000 +02:00'
pastFromLocal.toFormat('mm - yyyy') // https://moment.github.io/luxon/#/formatting?id=table-of-tokens
// display duration "...ago"
pastFromLocal.toRelative()  // ex. "two days ago"; respects locale
// date parts
pastFromLocal.hour  // 13
pastFromLocal.weekday //  4 ; Monday=1
// substracting (diffing) produces Duration object
now.diff(DateTime.fromISO(dueDate), ['days']).days // 5.178962164351852
// locale formatting
DateTime.local(2021, 4, 21, 11, 33).toLocaleString()  // '21. 4. 2021'
DateTime.local(2021, 4, 21, 11, 33).toLocaleString(DateTime.DATETIME_MED) // '21. 4. 2021 11:33'
// relative - string formatting
dateFromLocal.toRelative()  // "před 5 dny"
DateTime.local(2021, 4, 21, 13,33).toRelative() // "za 19 hodin"
DateTime.local(2021, 4, 21, 13,33).toRelativeCalendar() // "zítra"
// setting partially
const todayMidnightM = DateTime.now().set({ hour: 12, minute: 0, second: 0, millisecond: 0 })  // today noon - for midnight, use: now().startOf('day')

// wait / sleep / setTimeout
await new Promise(resolve => setTimeout(resolve, 3000))

// print JSON
obj = {attr: "myattr"}
console.log(JSON.stringify(obj, null, 2))

// reading files (in node environment, not in the browser!)
const path = require('path');
import { readFileSync, readdir } from 'fs'

// read the file at once
// encoding must be set, unless binary is returned
const myString = readFileSync('/tmp/my_file.txt', 'ascii') // encoding!
// read files from the directory
const directoryPath = path.join(__dirname, 'mydir')
import { readdir } from 'fs/promises'
try {
  const filenames = await readdir(directoryPath)
  for (const filename of filenames) {
    console.log(filename)
  }
}
catch (err) {
  console.error('Unable to scan directory: ' + err)
}

// path extraction
// const path = require('path');
const pathString = "/some/path/to/file.txt"
path.dirname(pathString)  // /some/path/to
path.basename(pathString)  // file.txt

// Math functions
Math.ceil(0.1)  // 1
Math.log10(11)  // 1.041392685158225
// generate random int from range <MIN, MAX>
const MIN = 1
const MAX = 10
Math.floor(Math.random() * (MAX - MIN + 1)) + MIN

// Knex.js SQL library
// using subqueries for JOINs - alias needed!
const subquery = knex('my_subtable').select('id', 'onecol').where('id', 123).as('subquery_alias') // <- alias!
const result = await knex('mytable').select('somecol', 'onecol')
  .leftJoin(subquery, 'mytable.id', 'subquery_alias.id')
const resultInsert = await knex('mytable2').insert({
  'id': 123,
  'time_now': knex.fn.now
})
