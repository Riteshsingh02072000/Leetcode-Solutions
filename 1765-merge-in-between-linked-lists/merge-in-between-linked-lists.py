# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeInBetween(self, list1: ListNode, a: int, b: int, list2: ListNode) -> ListNode:
        cur = list1 
        idx = 1

        while idx<a:
            cur = cur.next
            idx+=1
        
        end = cur
        for i in range(b-a+1):
            end = end.next
        end = end.next
            
        
        cur2 = list2
        while cur2.next:
            cur2 = cur2.next
        
        cur.next = list2
        cur2.next = end
        return list1