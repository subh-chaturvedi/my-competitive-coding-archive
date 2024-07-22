class Solution:
    def sortPeople(self, names: list[str], heights: list[int]) -> list[str]:
        height_to_name = {heights[i]: names[i] for i in range(len(names))}
        heights.sort()
        result = []
        
        for height in reversed(heights):
            result.append(height_to_name[height])
        
        return result
    