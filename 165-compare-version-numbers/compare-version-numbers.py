class Solution:
    def compareVersion(self, version1: str, version2: str) -> int:
      

        v1 = [int(x) for x in version1.split('.')]
        v2 = [int(x) for x in version2.split('.')]
        print(v1,v2)
        
        len_diff = len(v1) - len(v2)
        if len_diff < 0:
            v1 += [0] * abs(len_diff)
        elif len_diff > 0:
            v2 += [0] * len_diff
        print(v1,v2)
        
        
        if v1 < v2:
            return -1
        elif v1 > v2:
            return 1
        else:
            return 0  


                    
            
        