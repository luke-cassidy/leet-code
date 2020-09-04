class Solution(object):
    def strStr(self, haystack: str, needle: str) -> int:
        try:
            return haystack.index(needle)
        except ValueError:
            return -1


haystack, neddle = "hello", "ll"
ans = Solution.strStr(Solution(), haystack, neddle)
print("ans: {}".format(ans))

haystack, neddle = "aaaaa", "ba"
ans = Solution.strStr(Solution(), haystack, neddle)
print("ans: {}".format(ans))

haystack, neddle = "aaaaa", ""
ans = Solution.strStr(Solution(), haystack, neddle)
print("ans: {}".format(ans))

haystack, neddle = "", "d"
ans = Solution.strStr(Solution(), haystack, neddle)
print("ans: {}".format(ans))

haystack, neddle = "", ""
ans = Solution.strStr(Solution(), haystack, neddle)
print("ans: {}".format(ans))
