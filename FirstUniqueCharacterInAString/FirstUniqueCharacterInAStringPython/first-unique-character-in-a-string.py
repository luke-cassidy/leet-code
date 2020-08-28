import collections

class Solution(object):
    def firstUniqChar2(self, s: str) -> int:
        d = {}
        for i in range(len(s)):
            if s[i] in d:
                d[s[i]][0] += 1
            else:
                d[s[i]] = [1, i]

        ans = -1
        for k, v in d.items():
            if v[0] == 1 and ans == -1 or v[1] < ans:
                ans = v[1]

        return ans

class Solution(object):
    def firstUniqChar(self, s: str) -> int:
        count = collections.Counter(s)

        for i, v in enumerate(s):
            if count[v] == 1:
                return i

        return -1


s = "leetcode"
ans = Solution().firstUniqChar(s)
print("ans: {}".format(ans))

s = "loveleetcode"
ans = Solution().firstUniqChar(s)
print("ans: {}".format(ans))

s = "bbbaaaccd"
ans = Solution().firstUniqChar(s)
print("ans: {}".format(ans))
