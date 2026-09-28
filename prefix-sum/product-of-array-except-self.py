class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        """
        Product of Array Except ITSELF
            -> Element at i will be the multiplication of:
                    [:i] and [i:] -> To the LEFT and to the RIGHT of i
            -> Create 2 Arrays Representing Multiplication to the LEFT and RIGHT
            if Left and Right no number -> return 1
        [1, 2, 3, 4] -> [1, 1, 2, 6] (Left -> Right)
        [1, 2, 3, 4] -> [1, 4, 12, 24] (Right -> Left)

        For L -> R Array: Index at i will return value [:i]
                            (Multiplication of all values BEFORE i)
        For R -> L Array: Index at i will return value [i:]
                            (Multiplication of all values AFTER i)

        Another Approach IF division is ALLOWED:
            At Index 0, get the multiplication total for [0:]
                Then for each index, you divide by the number of that index
                    And multiply by number at index - 1
        """

        def LR_Array_Init():
            """
                Basically the Base of the Idea/Solution
                    No extra technique, just raw bruteforce implementation
            Time Complexity: O(n) | O(2n)
            Space Complexity: O(n) | O(2n)
            """
            l = 1
            r = len(nums) - 2

            left_arr = [1] # O(n) Space
            right_arr = [1] # O(n) Space

            # O(n) Time
            while l < len(nums) and r >= 0:
                # Multiply values before i
                left = left_arr[-1] * nums[l - 1]
                left_arr.append(left)

                # Multiply values after i
                right = right_arr[-1] * nums[r + 1]
                right_arr.append(right)

                l += 1
                r -= 1

            res = [] # Doesn't count as Extra Space 
            for i in range(len(left_arr)): # O(n) Time
                val = left_arr[i] * right_arr[len(right_arr) - 1 - i]
                res.append(val)
            return res
        #return LR_Array_Init()

        def const_space():
            """
                You could do a DFS on Right and Left Side
                (Like in Palindrome, you expand at i 'til hit both sides)
        
            The trick to constant space is...
                "Output Array does NOT count as Extra Space"
                    -> We make Output Array into either the Left OR Right Array
                "Placeholder Array" if you will
            """
            res = [1] # Left Array
            l = 1
            while l < len(nums): # O(n) Time
                left = res[-1] * nums[l - 1]
                res.append(left)
                l += 1
            total_right = 1
            r = len(nums) - 1
            while r >= 0: # O(n) Time

                # res: [1, 1, 2, 6]
                res[r] = res[r] * total_right

                # total_right: 1 -> 4 -> 12 -> 24
                total_right = total_right * nums[r]
                r -= 1
            return res
        return const_space()
