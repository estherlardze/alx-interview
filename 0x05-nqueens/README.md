**N Queens**

The N Queen is the problem of placing N chess queens on an N×N chessboard so that no two queens attack each other.In chess, a queen can attack horizontally, vertically, and diagonally. How can N queens be placed on an NxN chessboard so that no two of them attack each other?

this code gives one possible solution to the N-queens problem for N = 4. No two queens are on the same row, column, or diagonal. The solution is achieved by the use of backtraking algorithm.

**backtracking** 

Backtracking is finding the solution of a problem whereby the solution depends on the previous steps taken. For example, in a maze problem, the solution depends on all the steps you take one-by-one. If any of those steps is wrong, then it will not lead us to the solution. In a maze problem, we first choose a path and continue moving along it. But once we understand that the particular path is incorrect, then we just come back and change it. This is what backtracking basically is.

In general, this is accomplished by recursion. Thus, in backtracking, we first start with a partial sub-solution of the problem and then check if we can proceed further with this sub-solution or not. If not, then we just come back and change it.

**Thus, the general steps of backtracking are:**

1. start with a sub-solution

2. check if this sub-solution will lead to the solution or not

3. If not, then come back and change the sub-solution and continue again
