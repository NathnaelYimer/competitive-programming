class Solution(object):
    def subarraySum(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        ret = 0
        s = 0
        hash_map = {}
        hash_map[0] = 1
        for n in nums:
            s += n
            if s - k in hash_map:
                ret += hash_map[s - k]
            hash_map[s] = hash_map.get(s, 0) + 1
        return ret
        
