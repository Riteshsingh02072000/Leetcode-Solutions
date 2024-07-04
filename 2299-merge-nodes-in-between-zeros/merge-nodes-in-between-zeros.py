# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeNodes(self, head: Optional[ListNode]) -> Optional[ListNode]:
        ans = demo = ListNode(0)
        sum_ = 0

        while head:
            if head.val:
                sum_+=head.val
            
            if not head.val and sum_:
                demo.next = ListNode(sum_)
                demo = demo.next
                sum_ = 0
            
            head = head.next
        return ans.next
