class Solution(object):
    def intersect(self, nums1, nums2):
        d = {}
        for num in nums1:
            d[num] = d[num] + 1 if num in d else 1

        intersect = {}
        result = []
        for num in nums2:
            if num in d:
                if num in intersect:
                    if intersect[num] < d[num]:
                        intersect[num] += 1
                        result.append(num)
                else:
                    intersect[num] = 1
                    result.append(num)

        return result


nums1, nums2 = [1, 2, 2, 1], [2, 2]
ans = Solution.intersect(Solution(), nums1, nums2)
print("ans: {}".format(ans))
nums1, nums2 = [4, 9, 5], [9, 4, 9, 8, 4]
ans = Solution.intersect(Solution(), nums1, nums2)
print("ans: {}".format(ans))
nums1, nums2 = [1, 1, 1, 1], [2, 2, 2, 2]
ans = Solution.intersect(Solution(), nums1, nums2)
print("ans: {}".format(ans))
nums1, nums2 = [], [1, 2, 3, 4]
ans = Solution.intersect(Solution(), nums1, nums2)
print("ans: {}".format(ans))
