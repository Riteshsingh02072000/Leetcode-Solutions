# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        # s1, s2 = "", ""
        # temp = ListNode(0)
        # ans = temp
        # while l1:
        #     s1+=str(l1.val)
        #     l1 = l1.next

        # while l2:
        #     s2+=str(l2.val)
        #     l2 = l2.next
        
        # add = int(s1[::-1]) + int(s2[::-1])
        # add = str(add)[::-1]

        # for x in add:
        #     temp.next = ListNode(int(x))
        #     temp = temp.next
        # return ans.next

        
        
        
        
        
        
        
        
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
            

