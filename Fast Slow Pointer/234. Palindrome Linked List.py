# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head: ListNode) -> bool:
        def get_middle_ll(head):
            fast, slow = head, head
            # odd will have slow at the middle node
            # even will have second of the middle nodes
            # so we will always have the one to be reversed being longer
            while fast is not None and fast.next is not None:
                slow = slow.next
                fast = fast.next.next
            return slow
        def reverse_ll(head):
            prev = None
            cur = head
            while cur is not None:
                temp = cur.next
                cur.next = prev
                prev = cur
                cur = temp
            return prev

        def check_palindrome(ll1, ll2):
            '''
            if the linked list is even in length then we check all items of the LLs against each other
                in this case both LLs will be none at the same time
            if the linked list is odd in length then we will run out of nodes on the reversed one,
            this will be an overlap but this is ok since the middle node doesnt matter and
            will always be equal to itself
            '''
            while ll1 is not None and ll2 is not None:
                if ll1.val != ll2.val:
                    return False
                else:
                    ll1 = ll1.next
                    ll2 = ll2.next
            return True

        middle = get_middle_ll(head)
        end = reverse_ll(middle)
        return check_palindrome(head, end)
