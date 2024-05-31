class Solution:
    def singleNumber(self, nums: List[int]) -> List[int]:
        xor = 0
        for num in nums:
            xor ^= num
    
        # Step 2: Find a set bit in the xor result (rightmost set bit)
        set_bit = xor & -xor
        
        # Step 3: Partition the array elements into two groups and XOR separately
        num1 = 0
        num2 = 0
        for num in nums:
            if num & set_bit:
                num1 ^= num
            else:
                num2 ^= num
        
        return num1, num2
        