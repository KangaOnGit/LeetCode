class Solution:
    def reverse(self, x: int) -> int:
        """
        There's alot of Ideas for this:
            1. Turn to String, append to List and Reverse (Time Limit Exceeded)
            2. Use Mod and // to get the Digit and then multiply by 10 ^(number of digits in num--)
                    123 -> 3 Characters -> 3 will multiply by 10^3
                                            2 will multiply by 10^2
                                            ...
                    OR, since it will loop through all digits anyway
                        you can multiply by 10 each loop
        """
        sgn = -1 if x < 0 else 1
        x = abs(x)
        
        rev = 0
        while x != 0:
            # 123 -> 3
                # rev = 0*10 + 3
                    # 123 -> 2
                        # rev = 3*10 + 2
            digit = x % 10
            x //= 10
            rev = rev*10 + digit
        rev *= sgn
        if rev < (-2**31) or rev > (2**31 - 1):
            return 0

        return rev