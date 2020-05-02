class Solution:
    def numJewelsInStones(self, J: str, S: str) -> int:
        c = 0
        for i in range(len(J)):
            for j in range(len(S)):
                if J[i] == S[j]:
                    c+=1
        return c
        
        