class Solution:
    def isPowerOfThree(self, n: int) -> bool:
        if n<0:
            return(False)
        x=1
        i=0
        while x<=n:
            if x==n:
                return(True)
            i+=1
            x=3**i
        return(False)
    
    
