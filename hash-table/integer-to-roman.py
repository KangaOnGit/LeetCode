class Solution:
    def intToRoman(self, num: int) -> str:
        def ugly_solution(num):
            res = ""
            i = 0
            while num > 0:
                digit = num%10*(10**(i))
                num //= 10
                print(f"Number: {digit}")
                if (i == 0):
                    if digit <= 5:
                        if digit == 5:
                            roman = "V"
                        elif digit == 4:
                            roman = "IV"
                        else:
                            roman = "I"*digit
                    else:
                        if digit == 9:
                            roman = "IX"
                        else:
                            roman = "V" + "I"*(digit-5)
                if (i == 1):
                    if digit <= 50:
                        if digit == 50:
                            roman = "L"
                        elif digit == 40:
                            roman = "XL"
                        else:
                            roman = "X"*(digit//10*i)
                    else:
                        if digit == 90:
                            roman = "XC"
                        else:
                            roman = "L" + "X"*((digit-50)//10**i)
                if (i == 2):
                    if digit <= 500:
                        if digit == 500:
                            roman = "D"
                        elif digit == 400:
                            roman = "CD"
                        else:
                            roman = "C"*(digit//10**i)
                    else:
                        if digit == 900:
                            roman = "CM"
                        else:
                            roman = "D" + "C"*((digit-500)//10**i)
                if (i == 3):
                    roman = "M"*(digit//10**i)
                res = roman + res
                print(f"Result: {res}")
                print(f"-"*30)
                i +=1
            return res
        res = ugly_solution(num)
        return res
