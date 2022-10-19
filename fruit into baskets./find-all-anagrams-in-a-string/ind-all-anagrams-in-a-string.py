class Solution(object):
    def findAnagrams(self, s, p):
        """
        :type s: str
        :type p: str
        :rtype: List[int]
        """
        res, charP, charS = [], [0]*26, [0]*26
        if len(p) > len(s): # edge case
            return res
        for c in p:       
            charP[ord(c)-ord('a')] += 1
        for i in range(0, len(s)-len(p)+1): 
            if i == 0: # begining of the word
                for j in range(i, i+len(p)):
                    charS[ord(s[j])-ord('a')] += 1       
            else: 
                charS[ord(s[i+len(p)-1])-ord('a')] += 1
                
            if charS == charP:
                res.append(i)
            
            # decrement the starting of sliding window count in charS
            charS[ord(s[i])-ord('a')] -= 1
            
        return res
        
