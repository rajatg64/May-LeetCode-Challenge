from collections import Counter
class Solution:
    def frequencySort(self, s: str) -> str:
        result = ''
        count = Counter(s)
        '''
        hashtable = {}
        
        for i in range(len(s)):
            if s[i] in hashtable:
                hashtable[s[i]] += 1
            else:
                hashtable[s[i]] = 1
        '''
        a = dict(sorted(count.items(), key=lambda x: x[1], reverse=True))
        
        for key,t in a.items():
            while t:
                t-=1
                result += key
        return result
                
                

                
        