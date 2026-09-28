# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        """
        2 Pointers
        (i, j) if i.val < j.val then we increment i by 1 (i.next)
            else increment j by 1 (j.next)
        """
        out_list = ListNode(0)
        def dfs(i, j, curr):

            # Logging
            print(f"list1: {i}")
            print(f" ")
            print(f"list2: {j}")
            print(f" ")
            print(f"List:{out_list}")
            print(f"-"*59)

            # Take remaining nodes
            if i is None:
                while j is not None:
                    curr.next = ListNode(j.val)
                    curr = curr.next
                    j = j.next
                return
            if j is None and i is not None:
                while i is not None:
                    curr.next = ListNode(i.val)
                    curr = curr.next
                    i = i.next
                return
            # if both is None then done
            if i and j is None:
                return

            # else compare
            if i.val < j.val:
                curr.next = ListNode(i.val)
                curr = curr.next
                dfs(i.next, j, curr)
            else:
                curr.next = ListNode(j.val)
                curr = curr.next
                dfs(i, j.next, curr)

        dfs(list1, list2, out_list)
        return out_list.next