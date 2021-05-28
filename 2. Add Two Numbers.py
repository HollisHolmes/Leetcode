# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        digit_sum = 0
        digit_carry = 0
        total_sum = 0
        cur = head = ListNode()

        while l1 or l2:
            digit_sum = digit_carry
            if l1:
                digit_sum += l1.val
                l1 = l1.next
            if l2:
                digit_sum += l2.val
                l2 = l2.next

            digit_carry = digit_sum // 10
            digit_sum = digit_sum % 10

            cur.next = ListNode(digit_sum)
            cur = cur.next

        if digit_carry != 0:
            cur.next = ListNode(digit_carry)

        return head.next
