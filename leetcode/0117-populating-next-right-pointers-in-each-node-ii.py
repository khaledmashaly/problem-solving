# https://leetcode.com/submissions/detail/698875530/

class Solution:
    def connect(self, root):
        if root is None:
            return None

        next_level_pre_head = Node()
        current_level_head = root

        while current_level_head is not None:
            current = current_level_head
            next_level_tail = next_level_pre_head

            while current is not None:
                if current.left is not None:
                    next_level_tail.next = current.left
                    next_level_tail = next_level_tail.next

                if current.right is not None:
                    next_level_tail.next = current.right
                    next_level_tail = next_level_tail.next

                current = current.next

            current_level_head = next_level_pre_head.next
            next_level_pre_head.next = None

        return root
