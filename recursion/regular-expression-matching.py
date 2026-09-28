class Solution:
    def isMatch(self, s: str, p: str) -> bool:

        def recursive(i, j):
            """
            Basically 2 Pointers:
                s = "aa" | p = "a*"
                     i          j
            if (j+1) is a kleene star:
                    We either skip 2 chars (a* = "")
                        OR we multiply a by a number k (a* = a*k)
                             -> check until (i+1) != j
            Time: O(2^n)
            """
            # if j is empty
            if j == len(p):
                # if i also empty -> True (p[j] == s[i])
                    # else -> False (p[j] != s[i])
                return i == len(s)

            match = (i < len(s)) and (s[i] == p[j] or p[j] == ".")
            # if there's a kleene star behind the char
            if (j + 1) < len(p) and p[j+1] == "*":
                # "*" = 0 -> Skip 2 chars
                return (recursive(i, j+2)
                    # OR "*" != 0 -> eval the the next char in s
                        # if next char in s == previous char
                            # -> True else False
                or ( match and recursive(i+1, j) ) )

            if match:
                # Evaluate next pair of chars
                return recursive(i+1, j+1)
            return False

        cache = {}
        def memoization_dp(i, j):
            if (i, j) in cache:
                return cache[(i, j)]
            if j == len(p):
                cache[(i, j)] = (i == len(s))
                return cache[(i, j)]

            match = (i < len(s)) and (s[i] == p[j] or p[j] == ".")
            if (j + 1) < len(p) and p[j+1] == "*":
                cache[(i, j)] = (
                    memoization_dp(i, j+2)
                    or ( match and memoization_dp(i+1, j) )
                )
                return cache[(i, j)]
            
            if match:
                cache[(i, j)] = memoization_dp(i+1, j+1)
                return cache[(i, j)]
            
            return False


        return memoization_dp(0, 0)