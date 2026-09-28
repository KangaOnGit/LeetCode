class Solution:
    def longestPalindrome(self, s: str) -> str:
        """
        Idea:
            A palindrome is defined by symmetry around a center.
            In a string, there are only two possible types of centers:
                1) A single character center  → odd-length palindromes
                    Example: "aba", "racecar"
                    Expansion starts at (i, i)

                2) A gap between two characters → even-length palindromes
                    Example: "abba", "noon"
                    Expansion starts at (i, i+1)

                For every index i in the string, treat it as both types of centers
                and expand outward while the left and right characters match.

                Each expansion gives the longest palindrome for that center.
                Track the longest window found across all centers.
        """

        if len(s) == 1 or s == s[::-1]:
            return s

        def expand(l, r):
            # If can still expand left, right and the character at both ends matches
            while l >= 0 and r < len(s) and s[l] == s[r]:
                # Expand Window to Left Side
                l -= 1
                # Expand Window to Right Side:
                r += 1

            # Return Previous Window
            # If l = 1 and r = 3 doesn't match
                # We revert by adding 1 to l and subtracting 1 from r to get previous Window
            return l + 1, r - 1
    
        start = end = 0

        for i in range(len(s)):
            l1, r1 = expand(i, i) # Odd case "aba", "racecar" -> Expanding around 1 Character
            l2, r2 = expand(i, i+1) # Even case "abba", "noon" -> Expanding around 2 Characters

            if r1 - l1 > end - start:
                end, start = r1, l1

            if r2 - l2 > end - start:
                end, start = r2, l2

        return s[start:end + 1]


