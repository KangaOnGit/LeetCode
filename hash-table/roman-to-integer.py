class Solution:
    def romanToInt(self, s: str) -> int:
        """
        The last problem was "Integer to Roman"
            And I did it by creating 10 million conditionals
            I was sick of it so i decided a dict is worth the O(7) space
        """
        roman_dict = {
            "I": 1,
            "V": 5,
            "X": 10,
            "L": 50,
            "C": 100,
            "D": 500,
            "M": 1000,
        }
        num = 0
        prev_num = 0
        for i, roman in enumerate(s):
            curr_num = roman_dict[roman]
            if curr_num > prev_num and i > 0:
                num = num - 2*prev_num + curr_num
            else:
                num = num+curr_num

            prev_num = curr_num
        print(num)
        return num