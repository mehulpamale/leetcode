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

    def myPow(self, x, n):
        """
        :type x: float
        :type n: int
        :rtype: float
        """


ip = [["8", "3", ".", ".", "7", ".", ".", ".", "."]
    , ["6", ".", ".", "1", "9", "5", ".", ".", "."]
    , [".", "9", "8", ".", ".", ".", ".", "6", "."]
    , ["8", ".", ".", ".", "6", ".", ".", ".", "3"]
    , ["4", ".", ".", "8", ".", "3", ".", ".", "1"]
    , ["7", ".", ".", ".", "2", ".", ".", ".", "6"]
    , [".", "6", ".", ".", ".", ".", "2", "8", "."]
    , [".", ".", ".", "4", "1", "9", ".", ".", "5"]
    , [".", ".", ".", ".", "8", ".", ".", "7", "9"]]
# ip = [0, 1, 2]
# ip = [10, 9, 8, 7, 6, 5, 4, 3, 2]
# ip = [7, 8, 9, 11, 12]
# ip = [1, 2, 0]
# ip = [0, 0, 0, 1, 2, 3, 3, 3], 3
# ip = [2, 2], 2
# ip = [2], 2
# ip = [1, 1]
ip2 = 3
output = Solution().isValidSudoku(ip)
print(output)

# nums = [0, 0, 1, 1, 1, 2, 2, 3, 3, 4]  # Input array
# expectedNums = [0, 1, 2, 3, 4]  # The expected answer with correct length
#
# k = Solution().removeDuplicates(nums)  # Calls your implementation
#
# assert k == len(expectedNums)
# for colIndex in range():
#     assert nums[colIndex] == expectedNums[colIndex];
