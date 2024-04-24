class Solution:
    def splitArray(self, arr: List[int], m: int) -> int:
        n=len(arr)
        if m>n:
            return -1
        def good(arr,low):
            student=1
            sum1=0
            for i in range(len(arr)):
                if sum1+arr[i]<=low:
                    sum1+= arr[i]
                else:
                    student+=1
                    sum1= arr[i]
                
            return student
        low=max(arr)
        high=sum(arr)
        while low < high:
            mid = (low + high) // 2
            students_covered = good(arr, mid)
            if students_covered <= m:
                high = mid
            else:
                low = mid + 1
        return low
    
        