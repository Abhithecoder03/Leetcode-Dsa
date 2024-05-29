class Solution:
    def numSteps(self, s: str) -> int:
        num=int(s, 2)
        print(num)
        count=0
        while num>1:
            if num%2==0:
                num=num//2
                print(num)
            else:
                num=num+1
            count+=1
        return count
        
        