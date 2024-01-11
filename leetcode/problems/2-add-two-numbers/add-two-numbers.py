# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        
        s1=l1
        s2=l2
        carry=0

        a= s1.val + s2.val
        if a>9:
            carry = a//10
            a=a%10
        
        l3 = ListNode(a)
        tempnode=l3
        s1=l1.next
        s2=l2.next

        while s1 or s2:
            if not s1:
                a = s2.val
            elif not s2:
                a = s1.val
            else:
                a= s1.val + s2.val

            a+=carry
            carry=0
            if a>9:
                carry = a//10
                a=a%10
            tempnode.next=ListNode(a)
            tempnode=tempnode.next

            if not s1:
                s2=s2.next
            elif not s2:
                s1=s1.next
            else:
                s1=s1.next
                s2=s2.next
        

        if carry!=0:
            tempnode.next=ListNode(carry)
        return l3