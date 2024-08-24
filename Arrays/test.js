// Empty array
let arr = []
console.log(arr)

// An array containing elements - numbers
let arr1 = [1,2,3,4]
console.log(arr1)

let fruits = ["melon", "apples", "pawpaws", "oranges"]
console.log(fruits)

// Accessing elements using index
console.log(arr1[1])

console.log(fruits[3])

// To get the length of the array
console.log(fruits.length)

// Accessing the last item in an array
last = fruits[fruits.length - 1]
console.log(last)

// Modifying an element at a specific address
fruits[1] = "pineapple"
console.log(fruits)

// Adding an element to the end of an array
fruits.push("berries")
console.log(fruits)

// Popping the last element
let fruit_1 = fruits.pop()

// print the popped fruit
console.log(fruit_1)

// print the remaining fruits
console.log(fruits)

// Removing an element at the beginning of an array
let fruit_2 = fruits.shift()
console.log(fruit_2)

// printing the remaining fruits
console.log(fruits)

// Adding an element at the beginning of an array
fruits.unshift("Kiwi")

// printing the new array
console.log(fruits)

// Iterating through an array
for (let i = 0; i < fruits.length; i++) {
    console.log(fruits[i])
}




