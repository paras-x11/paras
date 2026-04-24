---

# Module 17: JavaScript For Full Stack (Theory)

---

## 1. JavaScript Introduction

### Question 1: What is JavaScript? Explain the role of JavaScript in web development.

JavaScript is a high-level, interpreted programming language used to make web pages interactive and dynamic. It runs in the browser and allows developers to implement features like form validation, animations, dynamic content updates, and user interaction.

Role in web development:

* Adds interactivity to web pages
* Manipulates HTML and CSS dynamically
* Handles user events (clicks, input, etc.)
* Communicates with servers using AJAX/fetch
* Used in both frontend and backend (Node.js)

---

### Question 2: How is JavaScript different from other programming languages like Python or Java?

* JavaScript is primarily used for web development, while Python and Java are general-purpose languages.
* JavaScript runs in the browser, whereas Python and Java typically run on servers or local machines.
* JavaScript is loosely typed (dynamic typing), while Java is strongly typed.
* JavaScript uses prototypes for inheritance, while Java uses classes.
* JavaScript is event-driven and asynchronous by nature.

---

### Question 3: Discuss the use of `<script>` tag in HTML. How can you link an external JavaScript file?

The `<script>` tag is used to include JavaScript code inside an HTML document.

Ways to use:

* Internal JavaScript:

```html
<script>
  alert("Hello");
</script>
```

* External JavaScript:

```html
<script src="script.js"></script>
```

The `src` attribute links an external JavaScript file to the HTML document.

---

## 2. Variables and Data Types

### Question 1: What are variables in JavaScript? How do you declare them?

Variables are containers used to store data.

Declaration:

```javascript
var x = 10;   // function-scoped
let y = 20;   // block-scoped
const z = 30; // block-scoped, cannot be reassigned
```

---

### Question 2: Explain different data types in JavaScript.

JavaScript has the following data types:

* String → `"Hello"`
* Number → `10`, `3.14`
* Boolean → `true`, `false`
* Undefined → variable declared but not assigned
* Null → intentional empty value
* Object → `{name: "John"}`
* Array → `[1, 2, 3]`
* Symbol → unique identifier
* BigInt → large integers

---

### Question 3: Difference between undefined and null

* `undefined`: A variable declared but not assigned a value.
* `null`: A value assigned intentionally to represent "no value".

---

## 3. JavaScript Operators

### Question 1: Types of operators

**Arithmetic Operators**

* `+`, `-`, `*`, `/`, `%`

**Assignment Operators**

* `=`, `+=`, `-=`, `*=`

**Comparison Operators**

* `==`, `===`, `!=`, `>`, `<`

**Logical Operators**

* `&&` (AND), `||` (OR), `!` (NOT)

---

### Question 2: Difference between `==` and `===`

* `==` → compares values only (type conversion allowed)
* `===` → compares value and type (strict comparison)

Example:

```javascript
5 == "5"   // true
5 === "5"  // false
```

---

## 4. Control Flow

### Question 1: What is control flow? Explain if-else

Control flow determines how code executes based on conditions.

Example:

```javascript
let num = 5;

if (num > 0) {
  console.log("Positive");
} else {
  console.log("Negative or Zero");
}
```

---

### Question 2: Switch statement

The `switch` statement is used to execute code based on multiple conditions.

Example:

```javascript
switch(day) {
  case 1:
    console.log("Monday");
    break;
  default:
    console.log("Invalid");
}
```

Use switch when:

* There are multiple fixed values to compare
* It improves readability over multiple if-else

---

## 5. Loops

### Question 1: Types of loops

**For loop**

```javascript
for (let i = 0; i < 5; i++) {
  console.log(i);
}
```

**While loop**

```javascript
let i = 0;
while (i < 5) {
  i++;
}
```

**Do-while loop**

```javascript
let i = 0;
do {
  i++;
} while (i < 5);
```

---

### Question 2: Difference between while and do-while

* `while` checks condition first, then executes
* `do-while` executes at least once, then checks condition

---

## 6. Functions

### Question 1: What are functions?

Functions are reusable blocks of code.

Syntax:

```javascript
function greet() {
  console.log("Hello");
}
greet();
```

---

### Question 2: Function declaration vs expression

* Declaration:

```javascript
function add(a, b) {
  return a + b;
}
```

* Expression:

```javascript
const add = function(a, b) {
  return a + b;
};
```

---

### Question 3: Parameters and return values

* Parameters: Inputs to a function
* Return value: Output from a function

Example:

```javascript
function sum(a, b) {
  return a + b;
}
```

---

## 7. Arrays

### Question 1: What is an array?

An array is a collection of elements stored in a single variable.

```javascript
let arr = [1, 2, 3];
```

---

### Question 2: Array methods

* `push()` → adds element at end
* `pop()` → removes last element
* `shift()` → removes first element
* `unshift()` → adds element at beginning

---

## 8. Objects

### Question 1: What is an object?

An object is a collection of key-value pairs.

Difference from array:

* Array uses index
* Object uses keys

Example:

```javascript
let obj = {name: "John", age: 25};
```

---

### Question 2: Access and update properties

* Dot notation:

```javascript
obj.name
```

* Bracket notation:

```javascript
obj["name"]
```

Update:

```javascript
obj.age = 30;
```

---

## 9. JavaScript Events

### Question 1: What are events?

Events are actions like clicks, typing, or loading.

Event listeners detect and respond to events.

---

### Question 2: addEventListener()

Used to attach event handlers.

Example:

```javascript
button.addEventListener("click", function() {
  alert("Clicked!");
});
```

---

## 10. DOM Manipulation

### Question 1: What is DOM?

DOM (Document Object Model) represents the HTML structure as objects.

JavaScript interacts with DOM to:

* Change content
* Modify styles
* Handle events

---

### Question 2: DOM selection methods

* `getElementById()` → selects by ID
* `getElementsByClassName()` → selects by class
* `querySelector()` → selects first matching element

---

## 11. JavaScript Timing Events

### Question 1: setTimeout() and setInterval()

* `setTimeout()` → runs code once after delay
* `setInterval()` → runs code repeatedly after interval

---

### Question 2: Example of setTimeout()

```javascript
setTimeout(() => {
  console.log("Hello after 2 seconds");
}, 2000);
```

---

## 12. JavaScript Error Handling

### Question 1: try, catch, finally

Used to handle errors.

Example:

```javascript
try {
  let x = y; // error
} catch (error) {
  console.log("Error occurred");
} finally {
  console.log("Done");
}
```

---

### Question 2: Importance of error handling

* Prevents application crashes
* Improves user experience
* Helps debugging
* Ensures smooth execution


