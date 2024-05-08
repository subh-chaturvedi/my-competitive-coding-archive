class Solution:
    def findRelativeRanks(self, score: List[int]) -> List[str]:
        indicesMap = {}

        for i in range(len(score)):
            indicesMap[score[i]] = i
        
        score.sort(reverse=True)

        ans=[0]*len(score)

        for i in range(len(score)):
            # print(i,score[i],indicesMap[score[i]])
            if i==0:
                ans[indicesMap[score[i]]]=("Gold Medal")
            elif i == 1:
                ans[indicesMap[score[i]]]=("Silver Medal")
            elif i == 2:
                ans[indicesMap[score[i]]]=("Bronze Medal")
            else:
                ans[indicesMap[score[i]]]=str(i+1)
        
        return ans