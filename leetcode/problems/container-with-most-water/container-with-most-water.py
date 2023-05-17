def areacalc(i,j,h1,h2):
        l = j-i
        b=min(h1,h2)

        area = l*b
        return area

class Solution:

    def maxArea(self, height: List[int]) -> int:
        maxarea = 0
        j = -1
        i = 0
        for o in range(0,len(height)):
            
            area = areacalc(i,len(height)+j,height[i],height[j])
            #print("&",i,j,o,maxarea,area)
            if maxarea < area:
                maxarea=area

            if height[i] <= height[j]:
                i=i+1
            elif height[i] > height[j]:
                j=j-1

        return maxarea