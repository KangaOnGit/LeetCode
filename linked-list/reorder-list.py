# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        """
        Do not return anything, modify head in-place instead.

        Intuition:
            Tried While-Loop and do
                end.next = start.next
                start.next = end
            Problem: Not enough variables to store to do that many Loops
    
        Creating a List of Nodes?
        """

        def array_solution():
            """
            O(n) Space and Time

            Create a List to store all of the Nodes
                Node at the Start of List (index [i])
                        Points to -> Node at End of List

                Node at End of List (index [j])
                        Points to -> Node at the Start of List.next (index [i + 1])
                        Decrement j by 1, [j - 1]
                            So [i + 1] Points to  -> [j - 1]
            Two Pointers
            """
            q = []
            dummy = head
            while dummy:
                q.append(dummy)
                dummy = dummy.next

            i = 0
            j = len(q) - 1

            # 1 -> 2 -> 3 -> 4 -> 5
            while i < j:
                q[i].next = q[j] # 1 -> 5
                i += 1

                if i == j:
                    break

                q[j].next = q[i] # 5 -> 2
                                 # 1 -> 5 -> 2
                j -= 1
            q[i].next = None # Middle Node -> None
        #array_solution()

        def no_array_solution():
            """
            You obviously can't just get the End Node
                    And then Link it to the First Node
                        As Explained up above
            1 -> 2 -> 3 -> 4 -> 5

            Split the linked list into 2 halves:
                1 -> 2 -> 3
                4 -> 5 ===> 5 -> 4

            Merge lists together?
            """
            slow, fast = head, head.next

            #  Find Middle
            while fast and fast.next:
                slow = slow.next
                fast = fast.next.next

            second_half = slow.next # 3 -> 4
            first_half = head

            slow.next = None # Middle Node -> None

            # Reverse Second Half
            curr, prev = second_half, None # Start of List and End of List
            while curr:
                # Save next Iter of Curr
                tmp = curr.next
                curr.next = prev # Start of List -> End of List
                prev = curr
                curr = tmp # Move to next Node
            """
            1 -> 2 -> 3 -> 4 -> None
                Reverse List: 4 -> 3 -> 2 -> 1 -> None

            Current Node: 1
            Previous Node: None
            => 1 -> None 
                Save: 2 -> 3 -> 4
                Current Node = 2 -> 3 -> 4
                Previous Node = 1

            Next Iter: 2 -> 1 -> None | curr.next = prev
                       Save: 3 -> 4 | prev = curr, curr = tmp/save
            => Current Node Points to Previous Node
            """

            # Merge 2 Halves
            first = head # 1 -> 2 -> 3
            second_half = prev # 5 -> 4
            while second_half:
                """
                Rule of Thumb:
                    In LinkedList, if you're gonna switch reference (.next)
                        Then you should save it just in case
                        Like how Reverse Linked List you gotta
                                Save the Next Node and Previous Node
                                To then link that Next Node -> Previous Node
                """
                # 1, 2, 3 | 5, 4
                    # 1st Iter: 1 -> 5 -> 4
                    # => 2nd Iter follows same trajectory of 2 -> 4 -> 3
                    # => Move first half to first.next
                        # Move second half to second.next
                # 2
                tmp1 = first.next # Save first.next before switch
                first.next = second_half # 1 -> 5 -> 4

                # 4
                tmp2 = second_half.next # Save second_half.next before switch
                second_half.next = tmp1 # 5 -> 2

                second_half = tmp2 # 4
                first = tmp1 # 2
                # Next Iter: 2 Points to 4, 4 Points to 3

        no_array_solution()







    