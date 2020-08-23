class Solution(object):
    def rotate(self, nums, k):
        for i in range(k % len(nums)):
            nums.insert(0, nums.pop())

    def rotate2(self, nums, k):
        n = len(nums)
        a = [0] * n
        for i in range(n):
            a[(i + k) % n] = nums[i]
        nums[:] = a

    def rotate3(self, nums, k):
        k %= len(nums)
        start = nums[len(nums) - k:]
        end = nums[:len(nums) - k]
        nums[:] = start + end


nums = [1, 2, 3, 4, 5, 6, 7]
ans = Solution.rotate3(Solution(), nums, 3)

print(nums)
