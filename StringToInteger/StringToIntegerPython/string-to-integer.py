import re

class Solution(object):

    INT_MAX = 2147483647
    INT_MIN = -2147483648

    def myAtoi2(self, s: str) -> int:
        ans = re.sub('[\s]', '', s)
        if len(ans) == 0:
            return 0
        
        if not ans[0].isdecimal() and ans[0] not in ["+", "-"]:
            return 0

        ans = int(float(re.sub('[^0-9-+.]', '', s)))
        if ans > self.INT_MAX:
            return self.INT_MAX
        elif ans < self.INT_MIN:
            return self.INT_MIN
        else:
            return ans

    def myAtoi(self, s: str) -> int:
        nums_found = False
        first_idx = 0
        last_idx = len(s)

        for i, c in enumerate(s):
            if not nums_found:
                if not c.isdigit():
                    if c in ["-", "+"] and not ((i + 1) >= len(s)) and s[i+1].isdigit():
                        nums_found = True
                        first_idx = i
                    elif c == " ":
                        continue
                    else:
                        break
                else:
                    nums_found = True
                    first_idx = i
            else:
                if not c.isdigit():
                    last_idx = i
                    break

        if not nums_found:
            return 0
        else:
            ans = int(s[first_idx: last_idx])
            if ans > self.INT_MAX:
                return self.INT_MAX
            elif ans < self.INT_MIN:
                return self.INT_MIN
            else:
                return ans

s = "42"
ans = Solution().myAtoi(s)
print("ans: {}".format(ans))

s = "   -42"
ans = Solution().myAtoi(s)
print("ans: {}".format(ans))

s = "-91283472332"
ans = Solution().myAtoi(s)
print("ans: {}".format(ans))

s = "91283472332"
ans = Solution().myAtoi(s)
print("ans: {}".format(ans))

s = "4193 with words"
ans = Solution().myAtoi(s)
print("ans: {}".format(ans))

s = "words and 987"
ans = Solution().myAtoi(s)
print("ans: {}".format(ans))

s = "3.14159"
ans = Solution().myAtoi(s)
print("ans: {}".format(ans))

s = ""
ans = Solution().myAtoi(s)
print("ans: {}".format(ans))

s = "afa"
ans = Solution().myAtoi(s)
print("ans: {}".format(ans))

s = "+"
ans = Solution().myAtoi(s)
print("ans: {}".format(ans))

s = ".3"
ans = Solution().myAtoi(s)
print("ans: {}".format(ans))

s = "+1"
ans = Solution().myAtoi(s)
print("ans: {}".format(ans))