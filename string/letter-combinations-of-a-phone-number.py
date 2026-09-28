class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        num_dict = {
            "2": "abc",
            "3": "def",
            "4": "ghi",
            "5": "jkl",
            "6": "mno",
            "7": "pqrs",
            "8": "tuv",
            "9": "wxyz"
        }

        res = []
        res_str = ""
        def brute_force_recursion(digit_idx, res_str):        
            if digit_idx >= len(digits):
                return
            digit = digits[digit_idx]
            str_seq = num_dict[digit]
            for i, char in enumerate(str_seq):

                # Reset Character for 1st Sequence
                if digit_idx == 0:
                    res_str = ""
                # Reset Character for digit_idx Sequence
                # "5678" -> "jmp" = "567 |"8" = "tuv"
                    # -> First Char/Idx -> "jmpt"
                        # Since len("jmpt") == len(digits) -> Append
                    # Remove the t by taking the characters from 0 to (digit_idx - 1)
                    # Append the next character u
                else:
                    res_str = res_str[0:digit_idx]
                res_str += char
                if len(res_str) == len(digits):
                    res.append(res_str)
                brute_force_recursion(digit_idx + 1, res_str)

                
        brute_force_recursion(0, res_str)
        return res 