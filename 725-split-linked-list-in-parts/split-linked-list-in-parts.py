# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def splitListToParts(self, head: Optional[ListNode], k: int) -> List[Optional[ListNode]]:
        ans = []
        length = 0
        cur = head

        while cur:
            length+=1
            cur = cur.next
        
        n, r = divmod(length, k)

        for i in range(k):
            dummy = ListNode(0)
            dummy_head = dummy

            for j in range(n+(r>0)):
                dummy.next, dummy, head = head, head, head.next
            
            dummy.next = None

            if r>0:
                r-=1
            
            ans.append(dummy_head.next)
        return ans