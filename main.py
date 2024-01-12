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

    def longestConsecutive(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        mset = set(nums)

        max_len = 0
        for i in mset:
            counter = 1
            while i + counter in mset:
                counter += 1
            max_len = max(counter, max_len)
        return max_len


ip = [100, 4, 200, 1, 3, 2, 10, 11, 12, 13, 14]
output = Solution().longestConsecutive(ip)
print(ip)
print(output)

# nums = [0, 0, 1, 1, 1, 2, 2, 3, 3, 4]  # Input array
# expectedNums = [0, 1, 2, 3, 4]  # The expected answer with correct length
#
# k = Solution().removeDuplicates(nums)  # Calls your implementation
#
# assert k == len(expectedNums)
# for colIndex in range():
#     assert nums[colIndex] == expectedNums[colIndex];
