class Solution:
    def isPalindrome(self, x: int) -> bool:
        """
        Idea:
            1. Same approach as Problem 7 where you reverse an Integer
            2. Same approach as Problem 7 but you can stop until x < total because of symmetry
        """
        if x < 0 or (x % 10 == 0 and x != 0):
            return False
        total = 0
        while x > total:
            digit = x % 10
            x = x//10
            total = total*10 + digit
            print(total)

        return total == x or x == total//10
        