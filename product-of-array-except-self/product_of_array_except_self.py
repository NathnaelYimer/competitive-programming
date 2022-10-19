class Solution(object):
    def productExceptSelf(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        mul = 1
        right_side_mul = []
        left_side_mul = []
        for num in reversed(nums):
            mul *= num
            right_side_mul.append(mul)
        right_side_mul.reverse()
        
        mul = 1
        for num in nums:
            mul *= num
            left_side_mul.append(mul)
        
        ret = [right_side_mul[1]]
        for idx, num in enumerate(nums[1:-1]):
            try:
                ret.append(left_side_mul[idx] * right_side_mul[idx + 2]) 
            except:
                print(idx)
        ret.append(left_side_mul[-2])
        return ret
