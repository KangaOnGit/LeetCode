from collections import defaultdict
class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        """
        Approaches:
            Each Row, Column and 3x3 Kernel is a Dictionary
                Lookup: O(1)
                Space: O(n^2 * num_kernel)
                Time: O(n)
            
            Iterative Check for Row and Column
                Space: 0
                Time: O(n^2) and check once for each kernel
        """
        # Note: Numpy Matrix Manipulation is different from Python
        def sol1():
            # O(n) | O(3n)
            row_dict = defaultdict(list)
            col_dict = defaultdict(list) 
            kernel_dict = defaultdict(list)
            
            for r in range(len(board)):
                for c in range(len(board)):
                    val = board[r][c]
                    if val != ".":
                        if val in row_dict[r] or val in col_dict[c] or val in kernel_dict[(r//3, c//3)]:
                            return False
                    row_dict[r].append(val)
                    col_dict[c].append(val)
                    kernel_dict[(r//3, c//3)].append(val)
            return True
        return sol1()


