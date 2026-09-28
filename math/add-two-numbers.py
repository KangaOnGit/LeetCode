# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        
        dummy = ListNode(0)
        curr = dummy

        i = 0

        carry_over = 0

        while l1 or l2 or carry_over:

            i += 1

            # Check if l2 or l1.next is not None
            if l1:
                num1 = l1.val
            else:
                num1 = 0

            # Check if l1 or l1.next is not None
            if l2:
                num2 = l2.val
            else:
                num2 = 0

            # Logging
            print(f"Iteration {i}:\nnum1: {num1} | num2: {num2}")
            if i == 1:
                print(f"Type of Next (l1): {l1.next}")

            totes = num1 + num2 + carry_over

            carry_over = int(totes//10) # 18 -> 1 | 23 -> 2
            dummy_next = totes%10 # 18 -> 8 | 23 -> 3

            # Logging
            print(f"carry_over: {carry_over} | next: {dummy_next}")

            next_node = ListNode(dummy_next)
            print(f"Next Node for Dummy: {next_node}")

            # i == 1 -> curr.next <=> dummy.next
            curr.next = next_node
            print(f"Dummy Node at Iteration {i}: {dummy}")

            # Iterate to next Node
            curr = curr.next
            
            # Check if l1.next and l2.next are ListNode[] or None
            # If not None then go to next ListNode
            if l1:
                l1 = l1.next
            if l2:
                l2 = l2.next
            print(f"-"*59)

        return dummy.next