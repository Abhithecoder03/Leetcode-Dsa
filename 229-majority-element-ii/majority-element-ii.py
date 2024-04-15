class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        if len(nums)==1:
            return nums
        ele1=float('-inf')
        ele2=float('-inf')
        count1=0
        count2=0
        for i in range(len(nums)):
            if count1==0 and  ele2 != nums[i]:
                ele1=nums[i]
                count1=1
            elif ele1==nums[i]:
                count1+=1
            elif count2==0 and nums[i]!=ele1:
                count2=1
                ele2=nums[i]
            elif ele2==nums[i]:
                 count2+=1
            else:
                count1-=1
                count2-=1
        ls = [] 


        count1, count2 = 0, 0
        for i in range(len(nums)):
            if nums[i] == ele1:
                count1 += 1
            if nums[i] == ele2:
                count2 += 1

        mini = int(len(nums) / 3) + 1
        if count1 >= mini:
            ls.append(ele1)
        if count2 >= mini:
            ls.append(ele2)
        return ls
        