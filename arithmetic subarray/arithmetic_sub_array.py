class Solution:
    def checkArithmeticSubarrays(self, nums: List[int], l: List[int], r: List[int]) -> List[bool]:
        def isarray(nums):
            if len(nums) < 2:
                return False
            if len(nums)==2:
                return True
            dif=nums[1]-nums[0]
            for i in range(1,len(nums)-1):
                if nums[i+1]-nums[i]!=dif:
                    return False
            return True
        res=[]
        n=len(l)
        for i in range(n):
            s=nums[l[i]:r[i]+1]
            s.sort()
            if isarray(s):
                res.append(True)
            else:
                res.append(False)
        return res

            
