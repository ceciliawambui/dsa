// Define a Node class to represent each element in the queue
class Node {
    constructor(value) {
        this.value = value; // Assign the passed value to the node's value property
        this.next = null;   // Initialize the next property to null (indicating the end of the queue)
    }
}

// Define a Queue class to represent the queue data structure
class Queue {
    constructor() {
        this.front = null;  // Initialize the front of the queue to null (empty queue)
        this.back = null;   // Initialize the back of the queue to null (empty queue)
        this.length = 0;    // Initialize the length of the queue to 0 (no nodes yet)
    }

    // Method to add a new element to the back of the queue
    enqueue(value) {
        const newNode = new Node(value); // Create a new node with the given value
        if (this.length === 0) {         // If the queue is empty
            this.front = newNode;        // Set the new node as the front of the queue
            this.back = newNode;         // Also set the new node as the back of the queue
        } else {                         // If the queue is not empty
            this.back.next = newNode;    // Link the current back node to the new node
            this.back = newNode;         // Update the back to be the new node
        }
        this.length++;                   // Increment the length of the queue
    }

    // Method to remove an element from the front of the queue
    dequeue() {
        if (this.length === 0) return null; // If the queue is empty, return null
        const removedNode = this.front;    // Store the front node to be removed
        this.front = this.front.next;      // Update the front to the next node
        this.length--;                     // Decrement the length of the queue
        if (this.length === 0) {           // If the queue is now empty
            this.back = null;              // Set back to null
        }
        return removedNode.value;          // Return the value of the removed node
    }

    // Method to check if the queue is empty
    isEmpty() {
        return this.length === 0;          // Return true if the queue is empty, otherwise false
    }

    // Method to get the value at the front of the queue without removing it
    peek() {
        if (this.length === 0) return null; // If the queue is empty, return null
        return this.front.value;            // Return the value at the front of the queue
    }

    // Method to get the size of the queue
    size() {
        return this.length;                 // Return the length of the queue
    }

    // Method to print all values in the queue
    print() {
        let current = this.front;           // Start from the front of the queue
        while (current) {                   // Traverse the queue
            console.log(current.value);     // Print the value of the current node
            current = current.next;         // Move to the next node
        }
    }
}

// Usage:
const queue = new Queue();  // Create a new queue
queue.enqueue(1);           // Add 1 to the queue
queue.enqueue(2);           // Add 2 to the queue
queue.enqueue(3);           // Add 3 to the queue
console.log(queue)
queue.print();              // Print all values: 1 2 3
console.log(queue.dequeue()); // Remove and print the front element: 1
queue.print();              // Print remaining values: 2 3
console.log(queue.peek());  // Print the front element without removing it: 2
console.log(queue.size());  // Print the size of the queue: 2
console.log(queue.isEmpty()); // Check if the queue is empty: false
