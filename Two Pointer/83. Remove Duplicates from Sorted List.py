# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteDuplicates(self, head: ListNode) -> ListNode:
        '''
        Using 2 pointers to move through the list, this can be solved in O(n) time.
        First pointer keeps track of the current node, second pointer moves to the next non-duplicate item
        Then set the .next of the current node to the next non-duplicate node.
        Then move both pointers up to this node.
        '''
        cur_node, next_node = head, head
        while next_node:
            while next_node.next and next_node.next.val == next_node.val:
                next_node = next_node.next
            cur_node.next = next_node.next
            cur_node, next_node = cur_node.next, cur_node.next

        return head
            
