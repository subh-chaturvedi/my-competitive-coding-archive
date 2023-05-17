class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        nums.sort()
        closest = 2000000
        


        for i in range(len(nums)-2):
            j=i+1
            k=len(nums)-1

            while j<k:
                x=nums[i]+nums[j]+nums[k]

                if abs(target-x)<abs(target-closest):
                    closest = x
                '''
                print("x",x)
                print("abs",abs(target-x))
                print("closest",closest)
                print(i,j,k)
                print(nums[i],nums[j],nums[k])
                print("----------")
                '''

                if x == target:
                    return x
                elif x<target:
                    j=j+1
                elif x>target:
                    k=k-1


        return closest
                