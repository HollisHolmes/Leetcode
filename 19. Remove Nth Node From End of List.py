# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: ListNode, n: int) -> ListNode:
        '''
        using 2 pointers, first move a fast pointer ahead n nodes.
        Then move both the fast and slow pointers ahead by 1 until the fast pointer reached end of the list
        At this point fast pointer will have moved len(list) nodes and the slow pointer will have moved
            len(list)-n nodes, so it will be at the nth node from the end of the list
        '''
        fast = slow = head
        for _ in range(n):
            fast = fast.next
        if fast is None:
            return head.next
        while fast.next:
            slow = slow.next
            fast = fast.next
        slow.next = slow.next.next

        return head

        '''
        This method reverses a linked list, skips the nth element, then reverses the list back.
        '''
        def reverse_ll(head):
            '''reverse a linked list'''
            prev = None
            cur = head
            while cur:
                temp = cur.next
                cur.next = prev
                prev = cur
                cur = temp
            return prev

        def skip_nth_node(head, n):
            '''return linked list with nth node skipped'''
            if n == 1:
                return head.next
            cur = head
            count = 1
            prev = None
            while True:
                if count == n:
                    prev.next = cur.next
                    return head
                prev = cur
                cur = cur.next
                count += 1

        return reverse_ll(skip_nth_node(reverse_ll(head), n))
