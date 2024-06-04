class Solution:
    def longestPalindrome(self, s: str) -> int:
        if len(s) == 0:
            return 0
        
        if len(s) == 1:
            return 1
        a=[]
        
        count=0
        b=set(s)
        res=0
        x=0
        for i in b:
            a.append(s.count(i))
        for i in a:
            if i%2==0:
                count+=i
            else:
                count+=i-1
                x=1
        if x==1:
            count+=1
        return (res+count)
            
            
        