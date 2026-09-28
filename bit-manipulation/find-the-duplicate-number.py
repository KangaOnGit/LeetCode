class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        """
        Intuition:

            1. Create a Dictionary then use Lookup
                -> O(n) Space, O(1) Lookup Time
            
            2. Sort and then check if nums[i - 1] - nums[i] == 0
                -> O(nlogn) * O(n) Time -> O(n^2 logn) Time

            3. XOR: 2 XOR 2 = 0, Any number XOR itself = 0
                (Only works if number appears exactly 2 Times for it to be equal to 0)

            4. Tortoise and Hare to detect if there's a Loop
                -> 2 Pointers, O(1) Space | 1 Loop -> O(n) Time
            Why 4. Works?
                Because nums has n+1 integers in the range [1, n]
                    => Every single Integer in Num can be Trace back to the Index
                        Without causing Error
            Floyd works on any function f(x)
                where repeatedly applying the function eventually enters a cycle.
        """

        def Tortoise_n_Hare(nums):
            """
            nums = [1,3,4,2,2]
            Index = [0, 1, 2, 3, 4]

            0 -> 3 -> 2 -> 4 -> 2
                => There's a Cycle
            Rewritten:
            0 -> 3 -> 2 -> 4
                      ^    |
                      | ---|
            """
            slow = 0
            fast = 0
            while True:
                slow = nums[slow]
                fast = nums[nums[fast]]

                # Find their Meeting Point // Where Loop Starts
                if slow == fast:
                    break

            slow = 0
            while slow != fast:
                slow = nums[slow]
                fast = nums[fast]

            return slow
        return Tortoise_n_Hare(nums)
"""
How to find where Loop Start knowing there's a cycle and a meeting point


μ (mu) = distance from the start to the beginning of the cycle
λ (lambda) = length of the cycle
x = distance from the cycle entrance to where slow and fast first meet

Start
  |
  | μ
  v
  A ------> B
            |
            C ---- D ---- E
            ^            |
            |____________|

C = cycle entrance
Meeting point = D

Distance(C -> D) = x
Cycle length = λ = 3 (C -> D -> E -> C)

Slow Pointer Traveled: μ + x
Fast Travelled: 2(μ + x) (2x Speed of Slow Pointer -> 2x Distance Travelled)

But, in actuality, Fast hasn't travelled 2μ
    It has travelled cλ + μ + x  where c is a constant
        => It has travelled c times Length of the Cycle such that cλ = μ + x

So we have:
    2(μ + x) = cλ + μ + x
    -> μ + x = kλ -> μ = kλ - x
    -> μ = (k-1)λ + (λ-x)
        λ - x means: the distance from the meeting point to the entrance of the cycle.
        (C -> D minus C -> D -> E -> C = E -> C)

=> μ = (whole cycles) + (distance from meeting point to entrance)
=> Distance(Start -> Entrance Cycle) = Distance(Meeting -> Entrance Cycle)
        The whole cycles don't matter.
        Walking around a cycle one extra revolution leaves you at the same place.

=> To find where Slow and Fast Meets, we first make them Meet
    Then we Reset Slow to the Start
    Then we Loop til they both Meet Again
"""
        