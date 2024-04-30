# Lockboxes
## Implementation
1. Create an array with a list of all visited boxes initialising
with the one index 0 since it is open.
2. Create a queue holding the keys discovered in the boxes
initialising with the key of the box in index 0.
3. Iterate continuously as long as there is a key in the queue.
4. In each iteration access a box by popping the key in the 0th index
then if that box has not been visited add it to the visited array and add
its keys to the queue of keys. Otherwise do nothing and go to the next
iteration.
5. Check if the length of the visited array is the same as the number of
boxes. Return True or False depending on the result of the type check.