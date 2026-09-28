from collections import deque
class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        """
        Intuition:
            - Max Heap
                Append Every Node into the Max Heap
                    If len() > k -> Pop the Max Heap to get the max value
                    Pop the First-appended Node
                        (Can either use Queue or dictionary and remember left_most node)
                heap.remove() then heap.heapify the heap again -> O(n^2)
        """

        def bruteforce():
            """
                Compute max() every iter >= k
                Time Complexity:
                    max(): O(k)
                    outer for-loop: O(n)
                -> O(n * k)
            """
            out_list = []
            for right in range(len(nums) - k + 1):
                seq = nums[right : right + k]
                out_list.append(max(seq))
            return out_list
        #return bruteforce()

        def sliding_window():
            """
                Deque (Double-Ended Queue):
                    adding/removing elements from both ends in O(1) time

                Monotonic Queue:
                    Similar to Monotonic Stack
                        Where a Queue/Stack can ONLY be decreasing or increasing
                        Good for keeping track of min/max values
                        (Basically you kind of sort it)

                Heap/Priority Queue:
                    Finding maximum/minimum elements efficiently with lazy deletion

            Keep track of max -> Monotonically Increasing
            Keep track of min -> Monotonically Decreasing

            Finding Boundaries (Maximum Rectangle) -> Monotonically Increasing/Decreasing both works
                Since they can find you the BOUNDARIES that enclose those rectangles
            In a Monotonically Increasing queue, if next value is smaller than previous value
                Then we have found the right-most boundary
                Since in an increasing queue, all elements can only multiply with
                    the elements to its right
            vice-versa
            """

            l = 0
            idx_q = deque()
            out_list = []
            for right in range(len(nums)):

                # Maintain a Monotonically Increasing Queue
                while idx_q and nums[idx_q[-1]] < nums[right]:
                    idx_q.pop()
                idx_q.append(right)

                # If left is incremented
                    # Remove left-most value
                if l > idx_q[0]:
                    idx_q.popleft()
                
                # When right = k - 1
                    # Increment Left to slide the window
                if right + 1 >= k:
                    # Since it's a monotonically increasing queue
                        # The left-most value is always the largest
                        # Since we pop smaller values
                    out_list.append(nums[idx_q[0]])
                    l += 1
            return out_list
        return sliding_window()