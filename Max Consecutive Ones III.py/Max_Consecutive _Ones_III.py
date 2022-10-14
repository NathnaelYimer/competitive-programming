class Solution:
    def longestOnes(self, nums: List[int], k: int) -> int:
        i, j = 0, 0
        cnt_0 = 0
        n = len(nums)
        ret = 0
        while i < n and j < n:
            while j < n:
                if nums[j] == 0 and cnt_0 < k:
                    j += 1
                    cnt_0 += 1
                elif nums[j] == 1:
                    j += 1
                else:
                    break

            ret = max(ret, j - i)
            if nums[i] == 0:
                cnt_0 -= 1
            i += 1

        return ret


if __name__ == "__main__":
    assert Solution().longestOnes([1,1,1,0,0,0,1,1,1,1,0], 2) == 6
