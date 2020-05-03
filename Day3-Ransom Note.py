class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        found = 0
        visited = [False] * len(magazine)
        for i in range(len(ransomNote)):
            found  = 0
            for j in range(len(magazine)):
                if ransomNote[i] == magazine[j] and visited[j] == False:
                    found = 1
                    visited[j] = True
                    break
            if found == 0:
                return False
        return True