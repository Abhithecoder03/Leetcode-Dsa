class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        pre=1
        suff=1
        n=len(nums)-1
        ans=float('-inf')
        for i in range(n+1):
            if pre==0:
                pre=1
            if suff==0:
                suff=1
            pre*=nums[i]
            suff*=nums[n-i]
            currmaxi=max(pre,suff)
            ans=max(ans,currmaxi)
        return ans
        