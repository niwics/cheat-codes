/**
 * Javascript Cheat Sheet
 * Author: niwi.cz
 */

 /*
  * Variables
  * Since ES6 const and let were added.
  */
 // constant (but is not immutable inside!)
 const myConstVariable = 1;
 // could be reassigned; valid in its block only
 let myVariable = 2;
 // generic, should be reassigned, valid in the whole context
 var myVariable2 = 3;


 // shortcut for calling anonymous function
 //() => myVariable


 /*
  * Maps
  */
 let myMap = new Map([["a", 1], ["b", 2], ["c", 3]]);
// iterate over map with key and value
for (let [k, v] of myMap) {
  console.log(k, v);
}