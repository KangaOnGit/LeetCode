class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        # Hard Code to make it easier and convenient
        if numRows == 1:
            return [[1]]
        elif numRows == 2:
            return [[1], [1, 1]]
        matrix = [[1], [1, 1]]

        def loop(matrix):
            for i in range(2, numRows):
                # Each Row create 1 List
                lst = [0]*(i+1)
                for j in range(i+1):
                    if j == 0  or j == i:
                        lst[j] = 1
                    else:
                        lst[j] = matrix[i-1][j-1] + matrix[i-1][j]
                matrix.append(lst)
        loop(matrix)
        return matrix