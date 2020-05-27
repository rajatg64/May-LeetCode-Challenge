class Solution:
    def findMaxLength(self, nums: List[int]) -> int:
        if(len(nums)<=1):
            return 0

        dick={0:-1}
        count=0
        maxi=0
        for i,v in enumerate(nums):

            if(v==1):
                count+=1
            else:
                count-=1

            if count in dick:
                maxi=max(maxi,i-dick[count])

            else:
                dick[count]=i
        return maxi
            
        