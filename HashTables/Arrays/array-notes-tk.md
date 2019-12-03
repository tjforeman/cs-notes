What is an array? 

- A sequence of elements stored in a contiguous block of memory. 

How do you declare a new array? 

- determine how big the array needs to be

- request a block of memory that will fit the array

- receive the memory address of the reserved block

How do you add an element to the end of an array? 

- take the size of your current array and increase it by one element 

- request a block of memory of the new size 

- copy each element from the old space to the new space one at a time

- free the memory from the old array this is a 0(n) operation

How does python add an element to the end of a list? 

- Python will allocate a few empty spaces each time the array grows 

- Each time it grows, it allocates a bit more extra space that the previous

- adding an element to the end of the list is usually 0(1) but sometimes 0(n)

- on average can be considered 0(1)

How does Python add an element to the beginning of a list 

- check if there's any empty space at the end of the array 

- if not

1. allocate a new array place the first element and copy over the rest

2. Free memory from the old array

- if so

1. Starting from the back, move each element to the right one space

2. place the new element in the first position

- this is a 0(n) operation no matter what 


