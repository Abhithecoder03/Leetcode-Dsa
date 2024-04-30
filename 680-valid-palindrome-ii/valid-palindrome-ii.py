class Solution:
    def validPalindrome(self, s: str) -> bool:
        left, right = 0, len(s) - 1
        
        
        def isPalindrome(substring):
            return substring == substring[::-1]
        
        while left < right:
            if s[left] != s[right]:
               
                return isPalindrome(s[left:right]) or isPalindrome(s[left + 1:right + 1])
            left += 1
            right -= 1
        
       
        return True
