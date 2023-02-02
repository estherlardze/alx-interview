**N Queens**

The N Queen is the problem of placing N chess queens on an N×N chessboard so that no two queens attack each other.In chess, a queen can attack horizontally, vertically, and diagonally. The N-queens problem asks: How can N queens be placed on an NxN chessboard so that no two of them attack each other? Below, you can see one possible solution to the N-queens problem for N = 4. No two queens are on the same row, column, or diagonalFor example, this code is a solution for 4 Queen problem. The expected output is a binary matrix that has 1s for the blocks where queens are placed. The problem is achieved by the use of backtraking algorithm
Backtracking is finding the solution of a problem whereby the solution depends on the previous steps taken. For example, in a maze problem, the solution depends on all the steps you take one-by-one. If any of those steps is wrong, then it will not lead us to the solution. In a maze problem, we first choose a path and continue moving along it. But once we understand that the particular path is incorrect, then we just come back and change it. This is what backtracking basically is.

In backtracking, we first take a step and then we see if this step taken is correct or not i.e., whether it will give a correct answer or not. And if it doesn’t, then we just come back and change our first step. In general, this is accomplished by recursion. Thus, in backtracking, we first start with a partial sub-solution of the problem (which may or may not lead us to the solution) and then check if we can proceed further with this sub-solution or not. If not, then we just come back and change it.

**Thus, the general steps of backtracking are:**

start with a sub-solution
check if this sub-solution will lead to the solution or not
If not, then come back and change the sub-solution and continue again
