class Solution:
    def specialArray(self, nums: List[int]) -> int:
        maxi=max(nums)
        for i in range(0,maxi+1):
            count= sum(j >= i for j in nums)
            if count==i:
                return i
        return -1