# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
# import sys
# sys.set_int_max_str_digits(0)
class Solution:
    def doubleIt(self, head: Optional[ListNode]) -> Optional[ListNode]:
        reversed_list = self.reversed(head)
        cur = reversed_list
        prev = None
        carry = 0

        while cur:
            new_val = cur.val*2 + carry
            cur.val = new_val%10
            carry = 1 if new_val>9 else 0
            prev, cur = cur, cur.next
        
        if carry:
            prev.next = ListNode(carry)
        return self.reversed(reversed_list)
    
    def reversed(self, node):
        cur = node
        prev = None
        while cur:
            nxt = cur.next
            cur.next = prev
            prev = cur
            cur = nxt
        return prev
        