# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        """ 
        Tortoise and Hare thing
            If 2 People move at 2 Different Speeds Meet Each Other (same time)
                -> The Road they're moving has a Loop
                Because on a Non-looped road, they should NEVER catch up to each other
        """
        slow, fast = head, head
        while slow and fast:
            slow = slow.next
            for _ in range(2):
                if fast is not None:
                    fast = fast.next
                else:
                    return False
            if slow == fast:
                return True

        return False