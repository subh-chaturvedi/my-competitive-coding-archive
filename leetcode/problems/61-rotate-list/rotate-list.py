# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def rotate(self, head):
        end=head

        while end.next.next:
            end=end.next
        
        newHead=end.next
        end.next.next=head
        end.next=None

        # print(newHead)
        return newHead

    def lenL(self,head):
        count=0
        
        tt=head

        while tt:
            count+=1
            tt=tt.next
        
        return count

    def rotateRight(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        
        if head is None or head.next is None:
            return head

        lenL=self.lenL(head)

        k=k%lenL

        for _ in range(k):
            head=self.rotate(head)

        return head