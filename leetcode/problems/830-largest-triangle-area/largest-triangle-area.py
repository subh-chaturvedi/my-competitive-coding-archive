class Solution:
    def largestTriangleArea(self, points: List[List[int]]) -> float:
        #Area = (1/2) * |x1 * (y2 - y3) + x2 * (y3 - y1) + x3 * (y1 - y2)|

        def area(x,y,z):
            ans = x[0]*(y[1]-z[1])
            ans+= y[0]*(z[1]-x[1])
            ans+= z[0]*(x[1]-y[1])

            ans = abs(ans)

            ans*= 0.5

            return ans


        ans = 0 

        for i in range(len(points)):
            for j in range(i,len(points)):
                for k in range(j,len(points)):

                    area2 = area(points[i],points[j],points[k])

                    ans= max(ans,area2)
        
        return ans