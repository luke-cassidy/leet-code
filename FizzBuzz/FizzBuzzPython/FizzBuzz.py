from typing import List


class Solution(object):
    def fizzBuzz(self, n: int) -> List[str]:
        mappings = {3: "Fizz", 5: "Buzz"}
        result = []
        for i in range(n):
            res = ""
            for key, val in mappings.items():
                if (i+1) % key == 0:
                    res += val
            if res == "":
                res += str(i + 1)
            result.append(res)
        return result


n = 0
ans = Solution().fizzBuzz(n)
print("ans: {}".format(ans))

n = 1
ans = Solution().fizzBuzz(n)
print("ans: {}".format(ans))

n = 20
ans = Solution().fizzBuzz(n)
print("ans: {}".format(ans))
