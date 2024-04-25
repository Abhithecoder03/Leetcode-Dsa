class Solution:
    def longestIdealString(self, s: str, k: int) -> int:
        dp = [0] * 26  # Initialize a list to store the maximum length of ideal strings for each character
        
        for char in s:
            code = ord(char) - ord('a')  # Convert character to integer code
            
            # Calculate the start and end index of the sliding window
            start = max(0, code - k)
            end = min(25, code + k)
            
            # Update the maximum length of ideal strings for the current character
            dp[code] = max(dp[start:end+1]) + 1
        
        # Return the maximum length of ideal strings found in the dp array
        return max(dp)
