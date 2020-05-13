class Solution:
    
    # Efficient Solution
    def removeKdigits(self, num: str, k: int) -> str:
        stack=[]
        for n in num:
            while k and stack and stack[-1]>n:
                stack.pop()
                k-=1
            stack.append(n)
        
        stack = stack[:-k] if k else stack
        #print(stack)
        return "".join(stack).lstrip('0') or "0"
    
    #Naive Solution
    '''
    def removeKdigits(self, num: str, k: int) -> str:
        while k:
            delIndex = -1
            for i in range(len(num)-1):
                if num[i] > num[i+1]:
                    delIndex = i
                    break
            if delIndex != -1:
                 num = num[:delIndex] + num[delIndex + 1:]
            else:
                num = num[:len(num)-1]
            k -= 1
        if len(num) == 0:
            return str(0)
        res = int(num)
        return str(res)
    '''
                
                
                    
                    
            
        