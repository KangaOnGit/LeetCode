class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        """
        Brute Force:
            Get the total_len
            Get the median_idx = total_len//2
                total_len = 4 -> median_idx = 2
                total_len = 6 -> median_idx = 3
                    => the Median for total_len % 2 == 0 will be the num at
                        median_idx and median_idx - 1
                    => We just need to remember the previous number
                    (It will always overshoot by 1)
        """
        
        def brute_force():
            total_len = len(nums1) + len(nums2)
            med_idx = total_len // 2

            prev_num, curr_num = None, None
            ptr1, ptr2 = 0, 0

            # Stops right at the Median Index
            for _ in range(med_idx + 1):
                prev_num = curr_num
                if ptr1 >= len(nums1):
                    curr_num = nums2[ptr2]
                    ptr2 += 1
                    continue
                if ptr2 >= len(nums2):
                    curr_num = nums1[ptr1]
                    ptr1 += 1
                    continue
            
                num1 = nums1[ptr1]
                num2 = nums2[ptr2]

                if num1 < num2:
                    # Remember the current number
                    curr_num = num1
                    ptr1 += 1
                else:
                    curr_num = num2
                    ptr2 += 1
            if total_len % 2 == 0:
                return (prev_num + curr_num) / 2
            else:
                return curr_num
        return brute_force()
