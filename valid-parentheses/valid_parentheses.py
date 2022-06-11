class Solution:
    def isValid(self, s: str) -> bool:
        if s=="":
            return(True)
        if len(s)<2:
            return(False)
        pairbrackets={"(":")","{":"}","[":"]"}
        list1=[]
        for br in s:
            if br in pairbrackets:
                list1.append(br)
            else:
                if len(list1)==0 or pairbrackets[list1.pop()]!=br:
                    return(False)
        if len(list1)>0:
            return(False)
        else:
            return(True)
