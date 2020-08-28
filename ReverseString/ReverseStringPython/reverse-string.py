from typing import List


class Solution(object):
    def reverseString(self, s: List[str]) -> None:
        List[str].reverse(s)
        # s[:] = s[::-1]


s = ["h", "e", "l", "l", "o"]
Solution.reverseString(Solution(), s)
print("s: {}".format(s))
