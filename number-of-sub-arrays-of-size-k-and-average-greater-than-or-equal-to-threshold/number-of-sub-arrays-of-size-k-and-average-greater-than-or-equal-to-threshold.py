class Solution(object):
    def numOfSubarrays(self, arr, k, threshold):
        """
        :type arr: List[int]
        :type k: int
        :type threshold: int
        :rtype: int
        """
        sum_threshold = k * threshold
        cur_sum = sum(arr[:k])
        ans = 0
        if cur_sum >= sum_threshold:
            ans += 1
        for i in range(k, len(arr)):
            cur_sum -= arr[i - k]
            cur_sum += arr[i]
            if cur_sum >= sum_threshold:
                ans += 1
        return ans
