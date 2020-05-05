class Solution:
    def findComplement(self, num: int) -> int:
        if num == 0: 
            return 1
        else:
            return 2**(int(log2(num))+1)-1 - num
        