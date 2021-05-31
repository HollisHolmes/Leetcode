# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def detectCycle(self, head: ListNode) -> ListNode:
        '''
        2 steps:
        1) Detect if there is a cycle using tortoise and hare
        2) Find start of cycle using result from pt 1
        C lenght of cycle, A section into cycle where pointers met, I pre cycle, x - num iters

        slow: x = I + A
        fast: 2x = I + nC + A

        2I + 2A  = I + nC + A
        I = nC - A
        I is the meeting of the cycle so now we need to count out nC-A turns.
        The slow pointer is A into the cycle, so after nC-A steps will also be as the start of the cycle.
        Walk from the head node and from meeting of the pointers until they will meet at the start of the                   cycle
        WILD
        '''

        def find_cycle(head):
            slow = fast = head
            while fast and fast.next:
                slow =  slow.next
                fast = fast.next.next
                if slow == fast:
                    return slow
            return None

        cycle = find_cycle(head)
        if cycle is None:
            return None
        cur = head
        while cur != cycle:
            cur = cur.next
            cycle = cycle.next
        return cycle



            
