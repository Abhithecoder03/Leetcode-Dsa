class Solution:
    def reversePrefix(self, word: str, ch: str) -> str:
        rev=''
        if ch not in word:
            return word
        index=word.index(ch)
        temp=word[0:index+1]
        print(temp)
        rev=temp[::-1]+word[index+1:]
        return rev
        
        