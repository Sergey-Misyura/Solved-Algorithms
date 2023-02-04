"""
36. Valid Sudoku
(Medium complexity)

Determine if a 9 x 9 Sudoku board is valid. Only the filled cells need to be validated according to the following rules:

Each row must contain the digits 1-9 without repetition.
Each column must contain the digits 1-9 without repetition.
Each of the nine 3 x 3 sub-boxes of the grid must contain the digits 1-9 without repetition.

Note:
A Sudoku board (partially filled) could be valid but is not necessarily solvable.
Only the filled cells need to be validated according to the mentioned rules.
"""

class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        
        for row in board:
            if not self.isValidPattern(row): return False 
        
        for col_ind in range(9):
            col = [board[i][col_ind] for i in range(9)]
            if not self.isValidPattern(col): return False 
        
        for sub_box_row in range(0,3):
            for sub_box_col in range(0,3):
                sub_box = [board[sub_box_row*3 + (i // 3)][sub_box_col*3 +(i % 3)] for i in range(9)]
                if not self.isValidPattern(sub_box): return False
        
        return True
    
    
    def isValidPattern(self, pattern):
        pattern_of_digits = [i for i in pattern if i.isdigit()] 
        if (len(set(pattern_of_digits)) - len(pattern_of_digits)) !=0:
            return False
        return True