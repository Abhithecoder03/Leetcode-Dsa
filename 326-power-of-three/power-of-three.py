class Solution:
    def isPowerOfThree(self, n: int) -> bool:
        if n<=0:
            return False
        def rec(val, i):
            if val > n:
                return False
            elif val == n:
                return True
            return rec(val * 3, i + 1)
        
        return rec(1, 0)