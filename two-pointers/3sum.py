class Solution:
    def threeSum(self, nums: list[int]) -> list[list[int]]:
        def sorted_pointers(nums_list):
            """
            Quite slow due to the sort() method
            Idea:
                loop through the elements of list, for i in range...
                    1 pointer (left) at: i + 1
                    1 pointer (right) at: len(nums) - 1
                Because we loop i from 0 to len(nums) - 1
                    -> The element i loop through all elements from i + 1 to len(nums)
                    -> the element i+1 already has information on i
                Example: [-1, -1, 0, 1]
                    at i = 0, left and right will go from [1:3]
                    at i = 1, left and right don't have to go from idx 0 -> idx 3
                        because when i = 0, it has already carried information when i = 1
                            (-1 (i = 1), 0, 1) == (-1 (i = 1), 0, 0) = 3
                                -> We already know if sum of first 2 elements = 1
                                                then there must be a 2
                                                to satisfy total = 3
                            Similarly, if we already know the possible combinations for a specific value
                                -> We can delete its duplicates
                                i.e: if value = -1 and we have already computed its combinations
                                    then its duplicate value will have the SAME combination.
                since sorted:
                    if sum < 0 -> left += 1
                        elif sum > 0 -> right -= 1
            For each new value, scan the untouched region to its right exactly once.
                        If the value is the same as before, do not scan again
            """
            sorted_lst = sorted(nums_list)
            print(f"Sorted List: {sorted_lst}")
            res = []
            # Loop until there's less than 3 values left
            for i in range(len(sorted_lst) - 2):

                # Skip duplicate
                if i >= 1 and sorted_lst[i] == sorted_lst[i-1]:
                    continue
                # Since it's sorted, if idx at i > 0 then [i:] will be > 0
                if sorted_lst[i] > 0:
                    break

                print(f"Iteration: {i}")
                left, right = i + 1, len(sorted_lst) - 1
                while left < right:
                    total = sorted_lst[i] + sorted_lst[left] + sorted_lst[right]

                    #print(f"i, Left, Right = {i}, {left}, {right}")
                    #print(f"i, Left, Right (value) = {sorted_lst[i]}, {sorted_lst[left]}, {sorted_lst[right]}")
                    #print(f"Total: {total}")
                    if total == 0:
                        res.append([sorted_lst[left], sorted_lst[right], sorted_lst[i]])
                        # Reset to try other possible combinations
                        left += 1
                        # Only need to check if total == 0
                            # because you would need to check total again anyway if u loop
                        while left < right and sorted_lst[left] == sorted_lst[left - 1]:
                            left += 1

                    # If sum > 0 or right/left pointer == loop or duplicate value
                    elif total > 0:
                        right -= 1
                    else:
                        left += 1

                #print(f"Res: {res}")
                #print(f"-"*10)
            return res
        return sorted_pointers(nums_list = nums)