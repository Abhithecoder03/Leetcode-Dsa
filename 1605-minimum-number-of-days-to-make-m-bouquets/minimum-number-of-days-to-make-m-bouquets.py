class Solution:
    def minDays(self, arr: List[int], m: int, k: int) -> int:
        def possible(arr, day, m, k):
            n = len(arr)  # size of the array
            cnt = 0
            noOfB = 0
            # count the number of bouquets
            for i in range(n):
                if arr[i] <= day:
                    cnt += 1
                else:
                    noOfB += cnt // k
                    cnt = 0
            noOfB += cnt // k
            return noOfB >= m
        val = m * k
        n = len(arr)  # size of the array
        if val > n:
            return -1  # impossible case
        # find maximum and minimum
        mini = float('inf')
        maxi = float('-inf')
        for i in range(n):
            mini = min(mini, arr[i])
            maxi = max(maxi, arr[i])

        # apply binary search
        low = mini
        high = maxi
        while low <= high: 
            mid = (low + high) // 2
            if possible(arr, mid, m, k):
                high = mid - 1
            else:
                low = mid + 1
        return low
