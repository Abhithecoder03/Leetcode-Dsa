class Solution:
    def maximumCandies(self, candies: List[int], k: int) -> int:
        def check(candyPerPile):
            pile = 0
            for candy in candies:
                pile += candy // candyPerPile
            
            return pile >= k

        left = 1
        right = sum(candies) // k

        while left <= right:
            mid = (left + right) // 2

            if check(mid):
                left = mid + 1       
            else:
                right = mid - 1
        return right