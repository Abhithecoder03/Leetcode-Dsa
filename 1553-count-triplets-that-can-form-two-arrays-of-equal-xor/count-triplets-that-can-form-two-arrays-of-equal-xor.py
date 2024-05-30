class Solution:
    def countTriplets(self, arr: List[int]) -> int:
        n=len(arr)
        if n==1: return 0
        ans=0
        for i in range(n):
            xor_sum=0
            for k in range(i, n):
                xor_sum^=arr[k]
                if xor_sum==0:
                    ans+=k-i
        return ans
        