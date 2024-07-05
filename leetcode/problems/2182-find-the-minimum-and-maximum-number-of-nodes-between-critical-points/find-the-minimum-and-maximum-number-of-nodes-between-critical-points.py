# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def nodesBetweenCriticalPoints(self, head: Optional[ListNode]) -> List[int]:
        
        dist=[]

        prev=head
        curr=head.next

        trav=1

        while curr.next:
            if (curr.val>prev.val and curr.val>curr.next.val) or (curr.val<prev.val and curr.val<curr.next.val):
                dist.append(trav)
            
            prev=curr
            curr=curr.next
            trav+=1
        
        # print(dist)
        minD = -1
        maxD = -1
        
        if len(dist)>1:
            maxD = dist[-1]-dist[0]

            minD = maxD
            for i in range(len(dist)-1):
                minD = min(dist[i+1]-dist[i], minD)
        
        return[minD,maxD]