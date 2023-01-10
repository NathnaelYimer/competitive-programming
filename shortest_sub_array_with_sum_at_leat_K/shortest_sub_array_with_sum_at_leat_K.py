class Solution:
    def shortestSubarray(self, nums: List[int], k: int) -> int:
        n=len(nums)
        pre_sums=[0]
        for i in range(n):
            pre_sums.append(nums[i] + pre_sums[-1])
        q=collections.deque()
        ans=sys.maxsize
        for right,s in enumerate(pre_sums):
            while q and s- pre_sums[q[0]] >=k:
                ans=min(ans,right-q.popleft())
            while q and  s<=pre_sums[q[-1]]:
                q.pop()
            q.append(right)
        if ans < sys.maxsize:
            return ans
        else:
            return -1
