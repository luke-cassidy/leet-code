class Solution(object):
    def twoSum(self, nums, target):
        d = {}
        for i in range(len(nums)):
            d[nums[i]] = i
        for i in range(len(nums)):
            val = target - nums[i]
            if val in d:
                if d[val] != i:
                    return i, d[val]
        raise Exception(
            "No two sum solution for given args: {}, {}".format(nums, target))

    def twoSum2(self, nums, target):
        d = {}
        for i in range(len(nums)):
            if nums[i] not in d:
                d[nums[i]] = i
            val = target - nums[i]
            if val in d:
                if d[val] != i:
                    return i, d[val]
        raise Exception(
            "No two sum solution for given args: {}, {}".format(nums, target))


nums, target = [2, 7, 11, 15], 9
ans = Solution.twoSum2(Solution(), nums, target)
print("ans: {}".format(ans))

nums.reverse()
ans = Solution.twoSum2(Solution(), nums, target)
print("ans: {}".format(ans))

nums, target = [3, 2, 4], 6
ans = Solution.twoSum2(Solution(), nums, target)
print("ans: {}".format(ans))

nums, target = [3, 3], 6
ans = Solution.twoSum2(Solution(), nums, target)
print("ans: {}".format(ans))

nums, target = [3, 2], 6
ans = Solution.twoSum2(Solution(), nums, target)
print("ans: {}".format(ans))
