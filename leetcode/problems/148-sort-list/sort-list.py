# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def sortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        arr=[]
        if not head:
            return head
        while head:
            arr.append(head.val)
            head=head.next
        

        arr.sort()

        head = ListNode(arr[0])
        temp=head

        for i in arr[1:]:
            temp.next=ListNode(i)
            temp=temp.next
        
        return head