class Solution:
    def intervalIntersection(self, A: List[List[int]], B: List[List[int]]) -> List[List[int]]:
        output = []
        i = 0
        j = 0
        while (i < len(A) and j < len(B)):
            res = []
            n1 = A[i]
            n2 =  B[j]
            start = max(n1[0],n2[0])
            end = min(n1[1],n2[1])
            if start <= end:
                res.append(start)
                res.append(end)
                output.append(res)
            
            if n1[1] < n2[1]:
                i += 1
            elif n2[1] < n1[1]:
                j += 1
            else:
                i += 1
                j += 1
            #print(output)
        return output
            
        