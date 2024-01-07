import typing as t
from collections import defaultdict


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution(object):
    def isMatch(self, s, p):
        """
        :type s: str
        :type p: str
        :rtype: bool
        """
        cache = {}

        def dfs(sptr, pptr):
            if (sptr, pptr) in cache:
                return cache[sptr, pptr]

            if sptr >= len(s) and pptr >= len(p):
                return True
            if pptr >= len(p):
                return False

            single_match = sptr < len(s) and (s[sptr] == p[pptr] or p[pptr] == '.')
            if (pptr + 1) < len(p) and p[pptr + 1] == '*':
                if dfs(sptr, pptr + 2):
                    cache[sptr, pptr + 2] = True
                    return True
                else:
                    if single_match:
                        res = dfs(sptr + 1, pptr)
                        cache[(sptr + 1, pptr)] = res
                        return res

            if single_match:
                res = dfs(sptr + 1, pptr + 1)
                cache[(sptr + 1, pptr + 1)] = res
                return res

            cache[(sptr, pptr)] = False
            return False

        return dfs(0, 0)


# ip = 2, 10
# ip = [1, 3, 2, 1, 3, 5], 3
# ip = [1, 0, -1, 0, -2, 2], 0
# ip = "aa", "a"
# ip = "aa", "a*"
# ip = "a", "a"
# ip = "ab", ".*"
# ip = "aab", "c*a*b"
ip = "aaaaaaaaaaaaaaaaaaab", "a*a*a*a*a*a*a*a*a*a*"
# ip = [2, 2, 2, 2, 2], 8
# ip = [0, 0, 0, 0], 0

# ip = [1], 1
# ip = [2], 3
# ip = [4, 2, 0, 2, 2, 1, 4, 4, 1, 4, 3, 2], 2
# ip = [1, 3, 2, 1, 3, 5], 1
# ip = [3, 2, 2, 3], 3
# ip = [1, 2, 5, 6], 5
# ip = [1, 3, 5], 4
# ip = [1, 3, 5], 2
# ip = "23"
# ip = 2.00000, 10
# ip = 2, 4
# ip = [0, 1, 2]
# ip = [10, 9, 8, 7, 6, 5, 4, 3, 2]
# ip = [7, 8, 9, 11, 12]
# ip = [1, 2, 0]
# ip = [0, 0, 0, 1, 2, 3, 3, 3], 3
# ip = [2, 2], 2
# ip = [2], 2
# ip = [1, 1]
ip2 = 3
output = Solution().isMatch(*ip)
print(ip[0])
print(output)

# nums = [0, 0, 1, 1, 1, 2, 2, 3, 3, 4]  # Input array
# expectedNums = [0, 1, 2, 3, 4]  # The expected answer with correct length
#
# k = Solution().removeDuplicates(nums)  # Calls your implementation
#
# assert k == len(expectedNums)
# for colIndex in range():
#     assert nums[colIndex] == expectedNums[colIndex];
