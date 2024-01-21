"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        if not head:
            return head
        #First Copy

        copy=Node(head.val)

        temp=head
        tempCopy=copy

        while temp.next:
            tempCopy.next=Node(temp.next.val)
            temp=temp.next
            tempCopy=tempCopy.next
        
        #Random Copying

        temp=head
        tempCopy=copy

        while temp:
            steps=0
            randFinder=head
            while randFinder:
                if randFinder==temp.random:
                    break
                steps+=1
                randFinder=randFinder.next
                
            # print(steps,temp.val)
            tempRand=copy
            for i in range(steps):
                tempRand=tempRand.next
            
            tempCopy.random = tempRand

            tempCopy=tempCopy.next
            temp=temp.next
        
        return copy
