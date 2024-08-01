class Solution:
    def countSeniors(self, details: List[str]) -> int:
        age=0
        for i in details:
            if int(i[11:13])>60:
                age+=1
        return age