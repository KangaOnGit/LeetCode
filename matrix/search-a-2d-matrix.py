class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        """
        non-decreasing order -> increasing order

        Binary Search the Row First log(m)
            Then Binary Search the Columns log(n)
        -> Time Complexity: O(log(m*n))

        Note:
            When evaluating the Rows
                You must take the value at the END of the row
                    Because if you take the value at the START of the row
            matrix=[[1,3,5,7],[10,11,16,20],[23,30,34,60]]
            target=3
            -> It will take the middle_row as 1 although target is in row 0
                Because 1 < 3 so it will move left up by 1 making it 1
            taking the END of the row guarantees that it will
                either be INSIDE the Row (smaller) or OUTSIDE the row (larger)
        """

        l_row = 0
        r_row = len(matrix)

        while l_row <= r_row:
            mid = (r_row + l_row)//2
            if mid >= len(matrix): # Means value not inside the list
                return False
            if matrix[mid][len(matrix[0]) - 1] == target:
                return True
            elif matrix[mid][len(matrix[0]) - 1] > target:
                r_row = mid - 1
            else:
                l_row = mid + 1
        
        row = l_row
        l_col = 0
        r_col = len(matrix[0])

        while l_col <= r_col:
            mid = (l_col + r_col)//2
            if mid > len(matrix[0]):
                return False
            if matrix[row][mid] == target:
                return True
            elif matrix[row][mid] > target:
                r_col = mid - 1
            else:
                l_col = mid + 1
        return False