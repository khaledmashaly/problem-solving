# https://leetcode.com/submissions/detail/658416984/

"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        new_to_old = {None: None}
        dummy_new_head = Node(0)
        new_head = dummy_new_head
        temp_head = head

        while temp_head:
            new_head.next = Node(temp_head.val)
            new_to_old[temp_head] = new_head.next
            temp_head = temp_head.next
            new_head = new_head.next

        new_head = dummy_new_head.next
        while head:
            new_head.random = new_to_old[head.random]
            head = head.next
            new_head = new_head.next

        return dummy_new_head.next
