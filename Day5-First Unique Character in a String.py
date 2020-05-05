import math
class Solution:
    def firstUniqChar(self, s: str) -> int:
        mydict = dict()
        for i in range(len(s)):
            if s[i] in mydict:
                mydict[s[i]] = math.inf
            else:
                mydict[s[i]] = i
        if len(mydict) == 0:
            return -1
        res = min(mydict.values())
        if res == math.inf:
            return -1
        else:
            return res
        