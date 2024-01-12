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
        mmin, mmax = 10 ** 9, -10 ** 9
        mset = set()
        for num in nums:
            mmin = min(num, mmin)
            mmax = max(num, mmax)
            mset.add(num)

        counter = 0
        max_len = 0
        last = None
        for num in range(mmin, mmax + 1):
            if num not in mset:
                continue

            if last is None:
                last = num
                counter = 1
                continue
            elif last + 1 != num:
                max_len = max(max_len, counter)
                last = num
                counter = 1
                continue
            else:
                counter += 1

            last = num

        max_len = max(max_len, counter)

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
