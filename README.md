# Snek Challenge

## Challenge Description
Algorithm and data structuresConsider a rectangular board consisting of ​n​ ​× m​ cells. There is a snake lying on some of thecells, and all of the other cells are empty. The snake consists of one or more cells such thatcells with consecutive numbers are either horizontally or vertically adjacent. The first cell isthe snake's head, and the last cell is the snake's tail.On each turn, the snake's head moves to one of the horizontally or vertically adjacent cells,the second cell of the snake moves to the cell where the head was situated, the third celltakes the former place of the second cell, etc. All these movements happen simultaneously,so the head could potentially take the place of the tail.
    
There are two configurations of thesnake's cells that are prohibited: self-intersection (meaning that after each step any pair ofsnake cells should have pairwise different coordinates), and crossing the board's border.The path is a sequence of characters L, R, D, and U(corresponding to left, right, down, and up,respectively) describing the movements of snake's head on each turn. How many distinctvalid paths of length ​p​ can the snake make on the board
### Example:
For `board = ​[4, 3]`​, `snake = ​[[2, 2], [3, 2], [3, 1], [3, 0], [2, 0], [1, 0], [0, 0]]`​, and `depth = ​3​ `, the outputshould be `numberOfAvailableDifferentPaths(board, snake, depth) = 7`
<div align="center">
    <img src="example_1.png?raw=true">
</div>

Here are all of the valid paths with a length of 3 that the snake can make:
- LLU
- LUR
- LUL
- ULL
- ULD
- LUU
- ULU

### Contract Input Output

There are 3 input argument in this challenge:

#### Input
- **board**​ as *array.integer*
The ​board​ is an array describing the dimensions of the board. ​`board[0]`​ stands for thenumber of rows, and ​`board[1]`​ corresponds to the number of columns.
Guaranteed constraints:
  - `board.length` = 2
  - 1 ≤ `board[i]` ≤ 10.

- **snake**​ as *array.array.integer*
The ​snake​ is an array that describes the configuration of the snake's body on theboard. ​`snake[0]`​ corresponds to the initial coordinates of the snake's head,​ `snake[1]` corresponds to coordinates of the second cell, etc.
It is guaranteed that ​`snake[i]`​ and `​snake[i + 1]`​ are horizontally or vertically adjacent,and that its initial configuration is valid (i.e. there are no self-intersections and thesnake's entire body lies inside the board).
Guaranteed constraints:
  - 3 ≤ `​snake.length​` ≤ 7
  - `snake[i].length​` = 2
  - 0 ≤ `​snake[i][j]`​ < `​board[j]​`

- **depth​** as *integer*
The ​depth​ is the paths depth. You have to discard all paths with a different pathlength.
Guaranteed constraints:
  - 1 ≤ n ≤ 20

#### Output as *integer*
The number of distinct valid paths of length *p* that the snake can make, modulo $10^9 + 7$ 

**Acceptance tests**

- Test 1:
  - board: `[4,3]`
  - snake: `[[2,2],  [3,2],  [3,1],  [3,0],  [2,0],  [1,0],  [0,0]]`
  - depth: `3`

  Result: 7

- Test 2:
  - board: `[2,3]`
  - snake: `[[0,2],  [0,1],  [0,0],  [1,0],  [1,1],  [1,2]]`
  - depth: `10`

  Result: 1

- Test 3:
  - board: `[10,10]`
  - snake: `[[5,5],  [5,4],  [4,4],  [4,5]]`
  - depth: `4`

  Result: 81
  
## Challenge output

The challenge has been written using ***python*** and it's compatible with version *3.6.X* or higher.

All acceptance tests are inside [***challenge_tests.py***](challenge_tests.py).

In order to run your own tests, just import the challenge function from *core* package.

Example:
```python
from core import numberOfAvailableDifferentPaths

board = [4,3]
snek = [[2,2],  [3,2],  [3,1],  [3,0],  [2,0],  [1,0],  [0,0]]
depth = 3
n_available_paths = numberOfAvailableDifferentPaths(board, snek, depth)

print(n_available_paths)
```