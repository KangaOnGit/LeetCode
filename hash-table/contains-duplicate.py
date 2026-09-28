class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        """
        Approaches:
            1. Counter/Hash: O(n) Space and Time

            2. XOR: O(n) Time ONLY work if the problem is:
                "Find the number that's the duplicate"
            
            3. Turn list into Set
                -> If len(set) != len(list) then there are dupes
        """

        def counter_hash():
            counter = {}
            for idx, num in enumerate(nums):
                if num in counter:
                    print(f"False")
                    return True
                counter[num] = idx
            return False
        #return counter_hash()
    
        def check_set():
            return len(nums) != len(set(nums))
        return check_set()

