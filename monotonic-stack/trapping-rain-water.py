class Solution:
    def trap(self, height: List[int]) -> int:

        def my_own_solution():
            """
            Essentially finding the 'Boundary' for the water to be trapped
                Left is my Left-boundary and Right is my right boundary.
            The right boundary is equal to or larger than the left boundary.
                -> Compute the water trapped between the boundary by taking all elements inside the stack minus the left boundary height.
                -> Move the marker and put left-boundary as the right-boundary and continue.

            Problem: Cases where there are boundaries within a boundary
                Example: [0,1,0,2,1,0,1,3,2,1,2,1]
                    the sequence [3, 2, 1, 2] has 1 water trapped
                            because there's a smaller boundary inside the big boundary of 3
            Similar to a "Monotonic Increasing Stack"/Stricly Increasing
            """
            l = 0
            cnt = 0
            while l < len(height):
                while height[l] == 0:
                    l += 1
                # Left boundary must be > 0
                h = height[l]
                stack = [height[l]]

                # Find Right-Boundary
                r = l + 1
                while r < len(height) and height[r] < h:
                    stack.append(height[r])
                    r += 1
                # Once find Right-boundary
                if r < len(height):
                    while stack:
                        # Compute Count by taking the diff between val and min(boundaries)
                        val = stack.pop(-1)
                        cnt += height[l] - val
                else: break

                l = r

            return cnt
        #my_own_solution()

        def monotonic_stack():
            """
            Basically my own version but more refined
                Accounting for Boundaries inside Boundaries
            Example: [6, 3, 4, 0, 5]
                Old Version -> No Trapped Water // Can't detect inner boundaries
                -> Nested Structure
                -> Recursion, Stack, Divide and Conquer
                -> If NO Equal or Higher Boundary exist, use the closest one POSSIBLE
            [6, 1, 5, 1, 2, 4] -> Highest wall Possible is 5, pick that since can't find >= 6
            """
            stack = [] # Save Indexes
            cnt = 0
            for i in range(len(height)):
                # Monotonic Increasing Stack
                while stack and height[i] > height[stack[-1]]:
                    # I.e: [3, 0, 3]
                    val = stack.pop()  # 0
                    if not stack:
                        break
                    left = stack[-1] # Left of Popped Value, [0]/3
                    w = i - left - 1 # Width/2
                    # Min Height between boundaries minus the Popped Value Height
                    h = min(height[left], height[i]) - height[val]
                    cnt += w * h
                stack.append(i)
            return cnt
        #return monotonic_stack()

        def two_pointers():
            """
            Rather than Finding Local Maxed Right/Left Height
            We find the GLOBAL Maxed/Right Left Height and then Recursive narrow it down
                Kinda like a Binary Search? I guess?
            """

            l = 0
            r = len(height) - 1
            left_max = height[l]
            right_max = height[r]

            cnt = 0
            while l < r:
                if left_max < right_max:
                    l += 1
                    left_max = max(left_max, height[l])
                    cnt += left_max - height[l]
                else:
                    r -= 1
                    right_max = max(right_max, height[r])
                    cnt += right_max - height[r]
            return cnt
        return two_pointers()


