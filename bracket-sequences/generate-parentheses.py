class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        """
        Intuition:
            Starting with out = "(" there are 2 Options:
                1. Append ")" -> out = "()"
                2. Append "(" -> out = "(("
            
            For 1. there's only 1 option -> Append "(" -> out = "()("
            For 2. there's 2 options:
                1. Append ")" -> out = "(()"
                2. Append "(" -> out = "(((" if n = 3, then there's only 1 option -> out = ")))"    
        """
        if n == 1:
            return ["()"]
        out = []
        s = "("
        def recursion(s: str, count_open: int, count_close: int):
            if len(s) >= n*2 and s not in out:
                #print(s)
                out.append(s)
                return
            if (count_open == count_close):
                s += "("
                recursion(s, count_open + 1, count_close)
            elif count_open == n:
                s += ")"
                recursion(s, count_open, count_close + 1)
            else:
                s += "("
                recursion(s, count_open+1, count_close)
                #print(f"S before: {s}")
                s = s[:-1]
                #print(f"S after: {s}")
                s += ")"
                recursion(s, count_open, count_close+1)
            
        recursion(s, 1, 0)

        return out
            

            
