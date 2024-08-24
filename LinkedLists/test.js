class Node { 
    constructor(value) {
        this.value = value; // Assign the passed value to the node's value property
        this.next = null;   // Initialize the next property to null (indicating the end of the list)
    }
}

class LinkedList {
    constructor() {
        this.head = null;   // Initialize the head of the list to null (empty list)
        this.tail = null;   // Initialize the tail of the list to null (empty list)
        this.length = 0;    // Initialize the length of the list to 0 (no nodes yet)
    }

    append(value) {
        const newNode = new Node(value); // Create a new node with the given value
        if (!this.head) {                // If the list is empty (head is null)
            this.head = newNode;         // Set the new node as the head of the list
            this.tail = this.head;       // Also set the new node as the tail of the list
        } else {                         // If the list is not empty
            this.tail.next = newNode;    // Link the current tail node to the new node
            this.tail = newNode;         // Update the tail to be the new node
        }
        this.length++;                   // Increment the length of the list
    }

    prepend(value) {
        const newNode = new Node(value); // Create a new node with the given value
        if (!this.head) {                // If the list is empty (head is null)
            this.head = newNode;         // Set the new node as the head of the list
            this.tail = this.head;       // Also set the new node as the tail of the list
        } else {                         // If the list is not empty
            newNode.next = this.head;    // Link the new node to the current head
            this.head = newNode;         // Update the head to be the new node
        }
        this.length++;                   // Increment the length of the list
    }

    pop() {
        if (!this.head) return undefined; // If the list is empty, return undefined
        let current = this.head;          // Start from the head of the list
        let newTail = current;            // Initialize newTail to the current node
        while (current.next) {            // Traverse until the end of the list
            newTail = current;            // Update newTail to the current node
            current = current.next;       // Move to the next node
        }
        this.tail = newTail;              // Update the tail to the newTail
        this.tail.next = null;            // Remove the reference to the last node
        this.length--;                    // Decrement the length of the list
        if (this.length === 0) {          // If the list is now empty
            this.head = null;             // Set head to null
            this.tail = null;             // Set tail to null
        }
        return current;                   // Return the removed node
    }

    print() {
        let current = this.head;          // Start from the head of the list
        while (current) {                 // Traverse the list
            console.log(current.value);   // Print the value of the current node
            current = current.next;       // Move to the next node
        }
    }
}

//Usage:
const list = new LinkedList(); // Create a new linked list
list.append(1);                // Add 1 to the list
list.append(2);                // Add 2 to the list
list.append(3);                // Add 3 to the list
console.log(list)              //print the list
list.print();                  // Print all values: 1 2 3
console.log(list.pop().value); // Remove and print the last node's value: 3
list.print();                  // Print remaining values: 1 2
