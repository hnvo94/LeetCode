import collections

class Solution:
    #def isValidSudoku(self, board: List[List[str]]) -> bool:
    def isValidSudoku(board):
        rows = collections.defaultdict(set)
        cols = collections.defaultdict(set)
        squares = collections.defaultdict(set)
        for r in range(9):
            for c in range(9):
                if board[r][c] == ".":
                    continue
                if (board[r][c] in rows[r] or 
                    board[r][c] in cols[c] or 
                    board[r][c] in squares[(r//3, c // 3)]):
                    return False
                cols[c].add(board[r][c])
                rows[r].add(board[r][c])
                squares[(r // 3, c //3 )].add(board[r][c])
        return True
    
    test = [["5","3",".",".","7",".",".",".","."],["6",".",".","1","9","5",".",".","."],[".","9","8",".",".",".",".","6","."],["8",".",".",".","6",".",".",".","3"],["4",".",".","8",".","3",".",".","1"],["7",".",".",".","2",".",".",".","6"],[".","6",".",".",".",".","2","8","."],[".",".",".","4","1","9",".",".","5"],[".",".",".",".","8",".",".","7","9"]]
    print(isValidSudoku(test))

'''
problem: 36. Valid Sudoku
Time complexity: O(n^2) - we need to check every single box on the soduku board
Space complexity: O(n^2) - we need to store n^2 element to each board. 

Note: When checking for the square, we can divide the cell to 3 for example r // 3 or c // 3 to determine where that [r][c] belong to. 

'''   
                