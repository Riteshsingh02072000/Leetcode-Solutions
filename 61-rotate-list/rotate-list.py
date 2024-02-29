# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def rotateRight(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        if not head or k == 0:
            return head
        
        length = 1
        slow = head

        while slow.next:
            slow = slow.next
            length +=1
        
        k%=length
        slow.next = head
        temp = head
        
        for i in range(length-k-1):
            temp = temp.next
        
        ans = temp.next
        temp.next = None
        return ans