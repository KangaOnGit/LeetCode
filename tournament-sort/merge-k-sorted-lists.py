# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
import heapq
class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        if len(lists) == 0:
            return
        """
        Same Idea as "Longest Common Prefix"
            -> Vertical Search
        """
        out_list = ListNode(0)
        dummy = out_list

        def recursion(idx, min_idx, min_val, dummy):
            """
            Basically Vertical Search for Minimum Value
                N: Total Nodes
                k: Total Linked Lists
                Time: O(N*k)
                Space Complexity: O(N)
            """
            if len(lists) == 0:
                return

            if idx >= len(lists) and len(lists) > 0:
                # If minimum value doesn't change
                if min_val == 10e5:
                    # End of list -> Return
                    return
                dummy.next = ListNode(min_val)
                dummy = dummy.next
                if lists[min_idx] is None or lists[min_idx].next is None:
                    lists.pop(min_idx)
                else:
                    lists[min_idx] = lists[min_idx].next
                recursion(0, 0, 10e5, dummy)
                return

            linked_list = lists[idx]
            if linked_list is not None:
                if linked_list.val < min_val:
                    min_idx = idx
                    min_val = linked_list.val
            recursion(idx + 1, min_idx, min_val, dummy)

        #recursion(0, 0, min_val = 10e5, dummy = dummy)
        def better_recursion(dummy):
            """
            No Pop and doesn't create new nodes
                So both faster and uses less memory
            """
            while True:
                min_idx = -1
                min_val = float("inf")

                for i in range(len(lists)):
                    node = lists[i]
                    if node and node.val < min_val:
                        min_val = node.val
                        min_idx = i

                # If min_idx doesn't change -> lists = [None,...]
                if min_idx == -1:
                    break

                dummy.next = lists[min_idx]
                dummy = dummy.next
                lists[min_idx] = lists[min_idx].next

        #better_recursion(dummy)

        def heap_merge():
            """
            Heap is basically an automatically sorted List
                If you input any value, it will sort it for you
            """
            heap = []
            out = ListNode(0)
            dummy = out

            for i in range(len(lists)):
                if lists[i]:
                    heapq.heappush(heap, (lists[i].val, i, lists[i]))
            while heap:
                # Get lowest value node
                val, i, node = heapq.heappop(heap)
                dummy.next = node
                dummy = dummy.next

                # If that node has next
                if node.next:
                    # Push into heap
                    heapq.heappush(heap, (node.next.val, i, node.next))
            return out
        out = heap_merge()
        return out.next
