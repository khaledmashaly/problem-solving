# https://leetcode.com/submissions/detail/657845531/

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def rotateRight(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        if not head or not k:
            return head

        def get_length_and_tail(head):
            l = 0
            prev_head = None
            while head:
                prev_head = head
                head = head.next
                l += 1

            return l, prev_head

        def convert_to_left_rotation(k, l):
            return l - (k % l)

        l, tail = get_length_and_tail(head)
        k = convert_to_left_rotation(k, l)

        tail.next = head

        new_head = head
        prev_new_head = None
        for i in range(k):
            prev_new_head = new_head
            new_head = new_head.next

        prev_new_head.next = None
        return new_head
