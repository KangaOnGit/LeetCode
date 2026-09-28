"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""
from collections import defaultdict

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        """
        Given A -> B -> C
            Return A' -> B' -> C'
            such that A' has the properties as A but doesn't have the same address
        Node.random points to the Node not an Index
        """

        def initial_approach():
            copy = Node(0)
            dummy = copy
            node_dict = defaultdict(list)
            
            while head:
                # 0 -> 7 -> 13 -> 11 -> 10 -> 1 -> None
                dummy.next = Node(head.val)
                node_dict[head.val] = [head.val, head.next, head.random]
                

                dummy = dummy.next
                head = head.next
            dummy = copy.next
            while dummy:
                dummy.random = node_dict[dummy.val][2]
                dummy = dummy.next

            # Doesn't work because 13.random points to a node from original list
                # Because node_dict[head.val] saves the RANDOM NODE from the ORIGINAL LIST
                    # Through head.random
                # Another problem is that there can be multiple nodes with same value
                # -> dict[head.val] can be replaced by another head.val if 3 -> 3 -> 3
                # -> Either save by Reference for each Node or use a List
            return copy.next
        #return initial_approach()


        def improved_dictionary(head):
            """
            Complexity:
                O(n) Space
                O(n) Time
            We need to make a deep copy of the linked list.

            The difficult part is that each node has a `random` pointer, which may
                point to any node in the list, including one we haven't copied yet.

            Idea 1:
                Map copied node -> original/copied node.

                While creating the copied list, we may encounter
                    original.random ---> some future node
                A' -> B' -> C'
                Suppose we try to map   
                    copied_node -> copied_node
                                or
                    copied_node -> original_node
                while constructing the copied list.
                Let's say we have A'.random = C' but we are only creating Nodes Sequentially
                    -> we can't do node_dict[A'.random] = C'
                        Because C' hasn't been created

                If that future node hasn't been copied yet, we have no copied node
                to point to.

                In other words, we cannot correctly assign the copied node's
                `random` pointer during a single pass because the destination
                copied node may not exist yet.

            Idea 2:
                Map original node -> copied node.

                First pass:
                    - Create a copy of every node.
                    - Store:
                        original_node -> copied_node

                Second pass:
                    - Since every copied node already exists,
                    we can connect

                        copy.next   = map[original.next]
                        copy.random = map[original.random]
            A -> B -> C
            node_dict[A] = A' | node_dict[B] = B'
            If A.random = C then: node_dict[A.random] = node_dict[C] = C'
                => We don't need to have already created the copied node

            Why not use node.val as the key?

                Node values are NOT guaranteed to be unique.
                    7 -> 7 -> 7
                Using the node object itself as the key uniquely identifies each node.
            """
            if not head:
                return None

            node_dict = {} # O(n) Space

            dummy_head = head
            # O(n) Time
            while dummy_head:
                # Rather than Pointing to a Copied Reference
                    # We make the Original Holds the Value to the Copied
                node_dict[dummy_head] = Node(dummy_head.val)

                dummy_head = dummy_head.next
            
            dummy_head = head
            # O(n) Time
            while dummy_head:
                copied_node = node_dict[dummy_head]

                # .get() method returns Value of the Key, if No Key -> Return None
                    # Points to the Original Reference which stores the Copied Version
                copied_node.next = node_dict.get(dummy_head.next)
                copied_node.random = node_dict.get(dummy_head.random)
                dummy_head = dummy_head.next
            return node_dict[head]
        #return improved_dictionary(head)
        
        def optimal_solution(head):
            """
            Complexity:
                O(n) Time
                O(1) Space (1 Pointer)

            A -> B -> C
            Rather than doing: node_dict[A] = A'
                as a way of saving copied Node

            We can do:
            A -> A' -> B -> B' -> C -> C'
            """

            if not head:
                return None
            
            # Create A -> A' -> B -> B' -> C -> C' Structure
            dummy_head = head
            while dummy_head:
                tmp = dummy_head.next # B -> C

                copied_node = Node(dummy_head.val) # A'
                dummy_head.next = copied_node # A -> A'
                copied_node.next = tmp # A' -> B -> C
                
                dummy_head = dummy_head.next # A'
                dummy_head = dummy_head.next # B
                # Or you can do dummy_head = copied_node.next which makes it B

            # Assign .random Pointers
            dummy_head = head
            # A' -> B -> B' -> C -> C'
            while dummy_head:
                # A' random is A.random.next
                    # Because A.random points to the Original Node
                    # .next will point it to the Copied Node because of the struct
                    # Original Node -> Copied Node
                if dummy_head.random:
                    dummy_head.next.random = dummy_head.random.next

                # Move to next Original Node
                dummy_head = dummy_head.next # A'
                dummy_head = dummy_head.next # B
            
            # Take the Copied Nodes out of Original List
            copied_list = Node(0)
            dummy_copied = copied_list
            dummy_head = head
            while dummy_head:
                dummy_copied.next = dummy_head.next

                dummy_copied = dummy_copied.next
                dummy_head = dummy_head.next.next
            return copied_list.next
        return optimal_solution(head)