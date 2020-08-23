class Solution(object):

    def singleNumber(self, nums):
        ans = 0
        for num in nums:
            ans ^= num
        return ans


# ans = Solution().singleNumber([1, 1, 2])
ans = Solution.singleNumber(Solution(), [1, 1, 2])

print(ans)
