import numpy as np
class Solution:
    def smallerNumbersThanCurrent(self, nums: List[int]) -> List[int]:
        arr=np.array(nums)
        counts=[]
        for i in range(len(arr)):
            count_smaller = np.sum(arr < arr[i])
            counts.append(count_smaller)
        return counts

        


            
        