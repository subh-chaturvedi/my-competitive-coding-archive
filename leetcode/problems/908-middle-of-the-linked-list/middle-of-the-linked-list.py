# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
        
        #finding len

        currnode = head
        count=0
        while currnode is not None:
            count+=1
            currnode=currnode.next
        
        mid = count//2
        
        currnode = head
        count=-1
        while currnode is not None:
            count+=1
            #print(count, currnode.val,mid)
            if count==mid:
                finalnode=currnode
                newnode=finalnode
            elif count>mid:
                newnode.next=currnode
                newnode=newnode.next
            currnode=currnode.next
        
        return finalnode
