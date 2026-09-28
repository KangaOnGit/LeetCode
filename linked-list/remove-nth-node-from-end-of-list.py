# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        def two_pointers():
            """
            Remove Nth Node from the End
                -> Nth Node is n Nodes behind the End Node (None)
                -> 2 Pointers:
                    Pointer 1 (P1) with v1 = 1
                    Pointer 2 (P2) with v2 = n + 1
                        -> P1 is n nodes behind the End Node
            [1, 2, 3, 4, 5, None]
            i = 1
            j = n = 2

            Iter 0: i = 1, j = 3
            Iter 1: i = 2, j = 4
            Iter 2: i = 3, j = 5
            Iter 3: i = 4, j = None
                j = None -> i = i.next
            """
            out = ListNode(head.val)
            dummy = out
            i = head    
            j = head
    
            # Creates an n-Nodes Distance Gap
            for _ in range(n):
                j = j.next
            while True:
                if j is not None:
                    print(f"(i, j) = ({i.val}, {j.val})")
                if j is None:
                    # If j has reached end of list
                        # then i will be at the Nth Node
                        # -> Move i by 1 Node
                    i = i.next
                    print(f"j: {j}")
                    while i is not None:
                        print(f"i: {i}")
                        dummy.next = ListNode(i.val)
                        dummy = dummy.next
                        i = i.next
                    break
                else:
                    j = j.next
                    dummy.next = ListNode(i.val)
                    dummy = dummy.next
                    i = i.next
            return out.next
        def two_pointers_optimal():
            """
            The optimal version of the two_pointers
                Rather than recreating the List
                We remove the Nth Node directly from the Original List

            [0, 1, 2, None]
            Iter 0: i = 0, j = n = 2
            Iter 1: i = 1, j = None
            """
            # [0, [head]]
            out = ListNode(0, head)
            i, j = out, out

            # Stopping 1 Node before the Nth Node
            for _ in range(n + 1):
                j = j.next
            while i is not None:
                if j is not None:
                    print(f"(i, j): ({i.val}, {j.val})")
                if j is None:
                    print(f"(i, j): ({i.val}, {j})")
                    if i.next is not None:
                        i.next = i.next.next
                    break
                else:
                    i = i.next
                    j = j.next
            return out.next
        return two_pointers_optimal()
            