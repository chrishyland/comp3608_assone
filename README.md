# COMP3608 Assignment 1
This code will play a game of connect four using the minimax algorithm. There will be a variant of 
the algorithm with and without alpha-beta pruning.

## Code Stack
This was built using Python 3.

## Author
Charles Christopher Hyland.

## Resources used
- https://www.youtube.com/watch?v=fInYh90YMJU&t=19s
- http://blog.gamesolver.org/solving-connect-four/01-introduction/

## TODO:
- Figure out how to represent states and see what moves are valid to make. (Numpy array? Lists of lists? List of Strings?)
- Generate node class that can generate node, nodes children, and values to store for minimax. Also have a "state" stored for each node so we know what it's like there. 
- Generate DFS algorithm
- Be able to count how many in a row for a given state
- Generate evaluation function to evaluate score based on input and above point
- Develop part that'll let AI figure out which move to take 