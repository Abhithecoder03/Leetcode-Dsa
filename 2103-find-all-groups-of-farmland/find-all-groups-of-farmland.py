class Solution:
    def findFarmland(self, land: List[List[int]]) -> List[List[int]]:
        row ,cols=len(land) , len(land[0])
        res=[]
        for i  in range(row):
            for j in range(cols):
                if land[i][j]==1 and (i==0 or land[i-1][j]==0) and (j==0 or land[i][j-1]==0):
                    bottom=i
                    right=j
                    while bottom+1<row and land[bottom+1][j]==1:
                        bottom+=1
                    while right+1<cols and land[i][right+1]==1:
                        right+=1
                    res.append([i,j,bottom,right])
        return res
