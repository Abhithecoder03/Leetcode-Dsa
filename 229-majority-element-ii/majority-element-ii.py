class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        mydict= defaultdict(int)
        n=len(nums)
        mini=int(n/3)+1
        res=set()
        for i in nums:
            mydict[i]+=1
            if mydict[i]>=mini:
                res.add(i)
        return list(res)
        
        