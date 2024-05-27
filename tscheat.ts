// enums
enum Direction {
  Up,
  Down,
  Left,
  Right,
}
function respond(userDirection: Direction): void {
  if (userDirection == Direction.Up)
    console.log("Going UP!")
}

// typing
// object and keys
// direct specification
const myObject: {[key: string]: string} = {}
// restrict type of the key in type
type AllowJustNumbersAsKeys = {
  [key: number]: string
};

// array
let numbers: number[] = [1, 2, 3]
// array of objects
let comments: {id: number, text: string}[] = []

// interface for objects
interface Greeter {
  name: string
  polite?: boolean
  sayHello(): string;
}
const MyGreeter: Greeter = {
  name: "My custom greeter",
  sayHello: () => `Hello!`
}
