# The isBadVersion API is already defined for you.
# @param version, an integer
# @return an integer
def isBadVersion(version: int) -> bool:
    return version >= 3

# resursive solution
class Solution:
    def firstBadVersion(self, n: int) -> int:
        def binarySearch(lower: int, upper: int) -> int:
            if lower == upper:
                return lower

            mid: int = (lower + upper) // 2

            if isBadVersion(mid):
                return binarySearch(lower, mid)
            else:
                return binarySearch(mid + 1, upper)

        return binarySearch(1, n)


print("Solution 5 -> 3 : {}".format(Solution().firstBadVersion(1)))
