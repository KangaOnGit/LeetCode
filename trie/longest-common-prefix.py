class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        """
        Too many edge cases, strs = [""], ["aa", "aa"], ["a"]
            Just imagine the list as like a matrix
        """
        def bruteforce(matrix):
            def validate(matrix, row, col):
                """
                Check if character at current word in list
                            matches character at next word in list
                if matches -> check the next word
                    else return False
                """
                # the conditionals can be simplified if you sort
                # if [""]
                if len(matrix[row]) == 0:
                    return False
                # if not valid column
                if col + 1 > len(matrix[row]):
                    return False
                if (row + 1) < len(matrix) and col + 1 > len(matrix[row + 1]):
                    return False
                # if no more word to check
                if (row+1) >= len(matrix):
                    return True

                curr = matrix[row][col]
                nxt = matrix[row + 1][col]

                if curr == nxt:
                    return validate(matrix, row + 1, col)
                
                return False
            res = ""
            col = 0
            while True:
                # If first char doesn't match any word
                    # then there's no common prefix
                if col == 0 and not validate(matrix, row = 0, col = col):
                    return ""
                if validate(matrix, row = 0, col = col):
                    res += strs[0][col]
                    col += 1
                else:
                    return res
        return bruteforce(strs)