# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def oddEvenList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        
        if not head or not head.next:
            return head

        odd=head
        even= head.next
        evens=[]
        while even:
            evens.append(even.val)
            even=even.next
            odd.next=odd.next.next
            
            if not even:
                break
            odd=odd.next
            even=even.next
        
        print(evens)

        for i in evens:
            odd.next=ListNode(i)
            odd=odd.next

        return head