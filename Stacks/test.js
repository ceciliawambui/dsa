// Define a Stack class
class Stack {
    // Constructor to initialize the stack
    constructor() {
        // Initialize the stack with an empty array
        this.items = [];
    }

    // Method to add an item to the top of the stack
    push(element) {
        // Add the element to the end of the array (top of the stack)
        this.items.push(element);
    }

    // Method to remove and return the item at the top of the stack
    pop() {
        // Remove the last element from the array (top of the stack) and return it
        // If the stack is empty, return undefined
        return this.items.pop();
    }

    // Method to view the item at the top of the stack without removing it
    peek() {
        // Return the last element in the array (top of the stack) without removing it
        // If the stack is empty, return undefined
        return this.items[this.items.length - 1];
    }

    // Method to check if the stack is empty
    isEmpty() {
        // Return true if the stack has no elements, otherwise return false
        return this.items.length === 0;
    }

    // Method to get the number of elements in the stack
    size() {
        // Return the length of the array, which represents the number of elements in the stack
        return this.items.length;
    }

    // Method to clear all elements from the stack
    clear() {
        // Set the array to a new empty array, effectively clearing the stack
        this.items = [];
    }
}

// Usage
const stack = new Stack(); // Create a new instance of Stack

console.log()
stack.push(10); // Push 10 onto the stack
stack.push(20); // Push 20 onto the stack
console.log(stack) //print the stack
console.log(stack.peek()); // View the top element (20) without removing it
console.log(stack.pop()); // Remove and return the top element (20)
console.log(stack.isEmpty()); // Check if the stack is empty (false)
console.log(stack.size()); // Get the number of elements in the stack (1)
stack.clear(); // Clear all elements from the stack
console.log(stack.isEmpty()); // Check if the stack is empty (true)
