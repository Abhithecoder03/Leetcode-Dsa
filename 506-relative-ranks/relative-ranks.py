class Solution:
    def findRelativeRanks(self, score: List[int]) -> List[str]:
        rank=sorted(score , reverse=True)
        res=[]
        for i in score:
            index=rank.index(i)
            if index==0:
                res.append("Gold Medal")
            elif index==1:
                res.append("Silver Medal")
            elif index==2:
                res.append("Bronze Medal")
            else:
                res.append(str(index+1))
        return res

        