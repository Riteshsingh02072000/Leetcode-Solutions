# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
import sys
sys.set_int_max_str_digits(0)
class Solution:
    def doubleIt(self, head: Optional[ListNode]) -> Optional[ListNode]:
        num = ""
        while head:
            num+=str(head.val)
            head = head.next
        
        ans = str(2*int(num))
        dummy = tmp = ListNode(0)
        for i in range(len(ans)):
            tmp.next = ListNode(int(ans[i]))
            tmp = tmp.next
        return dummy.next