class Solution:
    def averageWaitingTime(self, customers: List[List[int]]) -> float:
        
        t=1

        ans  = 0

        for cust in customers:
            
            t=max(t,cust[0])
            
            t+=cust[1]

            ans+= (t-cust[0])
        
        ans = ans/len(customers)

        return ans