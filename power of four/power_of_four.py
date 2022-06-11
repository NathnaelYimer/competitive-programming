    def isPowerOfFour(self, n: int) -> bool:
        x=1
        i=0
        while x<=n:
            if x==n:
                return(True)
            i+=1
            x=4**i
        return(False)
        
