class Solution:
    def isPalindrome(self, s: str) -> bool:
        """
        Intuition:
            Reads the same backwards and forward
                -> Same Character at the Start and Back
                -> Symmetric at 1 Center Point or 2 Center Point
        I.e: Noon (Palindrome, 2 Center) | Racecar (Palindrome, 1 Center)
        Approach:
            - Expand in the Middle
            - Contract from both ends (Left and Right Pointers)
        """
        
        def contracts():
            l = 0
            r = len(s) - 1
            while l < r:
                while not s[l].isalnum():
                    l += 1
                    if l > r:
                        return True
                while not s[r].isalnum():
                    r -= 1
                    if r < l:
                        return True
                if s[l].lower() != s[r].lower():
                    return False
                l += 1
                r -= 1
            return True
        return contracts()
