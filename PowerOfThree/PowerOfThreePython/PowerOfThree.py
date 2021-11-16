import math


class Solution:
    # orig lazy attempt
    def isPowerOfThree(self, n: int) -> bool:
        if n <= 0:
            return False
        else:
            return round(math.log(n, 3), 10) % 1 == 0

n = -3
ans = Solution().isPowerOfThree(n)
print("ans {}: {}".format(n, ans))

n = -1
ans = Solution().isPowerOfThree(n)
print("ans {}: {}".format(n, ans))

n = 0
ans = Solution().isPowerOfThree(n)
print("ans {}: {}".format(n, ans))

n = 1
ans = Solution().isPowerOfThree(n)
print("ans {}: {}".format(n, ans))

n = 2
ans = Solution().isPowerOfThree(n)
print("ans {}: {}".format(n, ans))

n = 3
ans = Solution().isPowerOfThree(n)
print("ans {}: {}".format(n, ans))

n = 6
ans = Solution().isPowerOfThree(n)
print("ans {}: {}".format(n, ans))

n = 9
ans = Solution().isPowerOfThree(n)
print("ans {}: {}".format(n, ans))

n = 12
ans = Solution().isPowerOfThree(n)
print("ans {}: {}".format(n, ans))

n = 24
ans = Solution().isPowerOfThree(n)
print("ans {}: {}".format(n, ans))

n = 27
ans = Solution().isPowerOfThree(n)
print("ans {}: {}".format(n, ans))

n = 45
ans = Solution().isPowerOfThree(n)
print("ans {}: {}".format(n, ans))

n = 243
ans = Solution().isPowerOfThree(n)
print("ans {}: {}".format(n, ans))
