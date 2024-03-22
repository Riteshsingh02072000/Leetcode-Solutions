# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        slow = fast = head
        temp = head

        while fast.next and fast.next.next:
            slow = slow.next
            fast = fast.next.next
        
        if fast.next:
            slow = slow.next
        
        second_half = self.reversed(slow)

        while second_half:
            if temp.val!=second_half.val:
                return False
            temp = temp.next
            second_half = second_half.next
        return True
        
    
    def reversed(self, node):
        prev = None
        while node:
            nxt = node.next
            node.next = prev
            prev = node
            node = nxt
        return prev