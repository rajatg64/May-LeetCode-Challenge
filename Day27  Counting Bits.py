class Solution:
    def countBits(self, num: int) -> List[int]:
        res = []
        for i in range(num+1):
            res.append(str(bin(i).replace("0b", "")).count('1'))
        return(res)
            
            
        