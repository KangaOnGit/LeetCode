# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head:
            return head
        start, end = head, head
        while end:
            end = end.next  # Since the End is None
                            # You can just Assign prev = None
                            # But this is easier to infer    
        #print(start)
        #print(end)
        #print(f"-"*59)

        curr, prev = start, end
        while curr is not None:
            tmp = curr.next # Save Next Node
            curr.next = prev # Current Node Link to Previous Node
            prev = curr # Previous Node = Current Node
            curr = tmp # Current Node = Next Node to Link

            #print(f"Previous: {prev}")
            #print(f"Current: {curr}")
            #print(f"-"*59)
        return prev