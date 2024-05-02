class Solution:
    def findMaxK(self, nums: List[int]) -> int:
        nums.sort()
        target=nums[-1]
        i=0
        r=len(nums)-1
        while i<r:
            print(nums[i])
            if target==(-nums[i]):
                return target
            else:
                if abs(nums[i])>(nums[r]):
                    i+=1
                else:
                    r-=1
                target=nums[r]
        return -1
    
        