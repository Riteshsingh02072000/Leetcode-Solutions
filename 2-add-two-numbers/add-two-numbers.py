# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        temp = ListNode(0)
        ans = temp
        carry = 0

        while l1 or l2 or carry!=0:
            first = l1.val if l1 else 0
            second = l2.val if l2 else 0

            add = first+second+carry
            cur = add%10
            carry = add//10

            temp.next = ListNode(cur)
            temp = temp.next
            l1 = l1.next if l1 else None
            l2 = l2.next if l2 else None
        
        return ans.next

        
        
        
        
        
        
        
        
        temp = ListNode(0)
        ans = temp
        carry = 0
        while l1 and l2:
            add = (l1.val+l2.val+carry)
            carry = 0
            if add>9:
                cur = add%10
                carry = add//10
                temp.next = ListNode(cur)
            else:
                temp.next = ListNode(add)
            l1 = l1.next
            l2 = l2.next
            temp = temp.next
        while l1:
            add = l1.val + carry
            carry = 0
            if add>9:
                cur = add%10
                carry = add//10
                temp.next = ListNode(cur)
            else:
                temp.next = ListNode(add)
            
            l1 = l1.next
            temp = temp.next

        while l2:
            add = l2.val + carry
            carry = 0
            if add>9:
                cur = add%10
                carry = add//10
                temp.next = ListNode(cur)
            else:
                temp.next = ListNode(add)
            
            l2 = l2.next
            temp = temp.next
        if carry:
            temp.next = ListNode(carry)
        return ans.next
            

