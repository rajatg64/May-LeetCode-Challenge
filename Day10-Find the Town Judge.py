class Solution:
    def findJudge(self, N, trust):
        arr = [0] * (N + 1)
        for i in range(len(trust)):
            temp = trust[i]
            arr[temp[0]] += 1
        # print(arr)
        potentialJudge = -1
        count = 0
        for i in range(1, len(arr)):
            if arr[i] == 0:
                potentialJudge = i
                count += 1

        if potentialJudge == -1 or count != 1:
            return -1
        else:
            for i in range(len(trust)):
                if trust[i][0] != potentialJudge:
                    if trust[i][1] == potentialJudge:
                        arr[trust[i][0]] = potentialJudge

        for i in range(1, len(arr)):
            if i != potentialJudge and  arr[i] != potentialJudge:
                return -1
        return potentialJudge