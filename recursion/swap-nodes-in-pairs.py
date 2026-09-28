# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def swapPairs(self, head: Optional[ListNode]) -> Optional[ListNode]:
        # Empty or 1 Node
        if head is None or head.next is None:
            return head
        def swap_with_no_prev():
            # [0 -> 1 -> 2 -> 3 -> 4]
            out_list = ListNode(0)
            dummy = out_list
            slow, fast = head, head.next
            i = 0
            while slow is not None and fast is not None:
                slow.next = fast.next
                fast.next = slow
                slow, fast = fast, slow
                #print("slow:", slow)  # [2 -> 1 -> 3 -> 4]
                #print("fast:", fast) # [1 -> 3 -> 4]

                if i > 0:
                    # Move dummy 2 steps
                    for _ in range(2):
                        dummy = dummy.next
                dummy.next = slow
                # Move each pointer by 2 steps
                for _ in range(2):
                    if fast is not None and slow is not None:
                        fast = fast.next
                        slow = slow.next
                        #print("slow:", slow)
                        #print("fast:", fast)
                        #print(">"*59)
                    else:
                        break
                i += 1
                return out_list.next
        #out_list = swap_with_no_prev()

        def swap_with_no_mem(head):
            prev = None 

            # [2]
            dummy = head.next

            # [1 -> 2 -> 3 -> 4]
            while head is not None and head.next is not None:
                if prev:
                    # 1st Iter: 1 -> Head 
                    #           1 -> [3 -> 4]
                    prev.next = head.next # prev = 1 -> 4

                # 2nd Iter: prev = head = [3 -> 4]
                prev = head # Tail of Previous Pair

                # [3 -> 4]
                next_node = head.next.next

                # [2 -> 1] / [1 -> 2]
                # Head: 1 | Dummy: 2 = Head.next
                head.next.next = head

                # Head: [1 -> 3 -> 4]
                # Dummy: [2 -> 1 -> 3- > 4]
                head.next = next_node

                # Advance to Next Pair of Nodes
                head = next_node # [3]
            return dummy
        d = swap_with_no_mem(head)
        return d