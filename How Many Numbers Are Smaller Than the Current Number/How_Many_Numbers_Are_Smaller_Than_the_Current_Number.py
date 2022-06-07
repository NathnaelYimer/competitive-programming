class Solution:
    def smallerNumbersThanCurrent(self, nums: List[int]) -> List[int]:
        count=[]
        for i in range(len(nums)):
            count2=0
            for j in range(len(nums)):
                if i!=j and nums[i]>nums[j]:
                    count2+=1
            count.append(count2)
        return(count)
       
            
