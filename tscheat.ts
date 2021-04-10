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

// type of the key
type AllowJustNumbersAsKeys = {
  [key: number]: string
};