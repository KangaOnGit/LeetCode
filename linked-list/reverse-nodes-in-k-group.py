# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:

    def kthNode(self, curr, k):
        while curr and k > 0:
            curr = curr.next
            k -= 1
        return curr

    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        out = ListNode(0, head)
        previous_group = out
        # [1 -> 2 -> 3 -> 4 -> 5] | k = 3
        while True:
            # Get end of group
            end_of_group = self.kthNode(previous_group, k)
            if not end_of_group:
                break
            next_group = end_of_group.next 

            # Swap each of the node
            # prev, curr = 4, 1
            prev_curr, curr = end_of_group.next, previous_group.next
            while curr != next_group:
                tmp = curr.next # tmp: [2 -> 3 -> 4 -> 5]
                curr.next = prev_curr # curr: [1 -> 4 -> 5]
                prev_curr = curr # prev = 1
                curr = tmp  # curr = 2

            # Store first node in group
            tmp = previous_group.next

            # End of previous group
            previous_group.next = end_of_group

            # Start of previous group
            previous_group = tmp

        return out.next