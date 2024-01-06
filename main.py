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
    def fourSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        ans = set()
        for i_first, first in enumerate(nums):
            for i_second, second in enumerate(nums):
                if i_first == i_second:
                    continue
                for i_third, third in enumerate(nums):
                    if i_second == i_third or i_first == i_third:
                        continue
                    for i_fourth, fourth in enumerate(nums):
                        if i_third == i_fourth or i_third == i_second or i_third == i_first:
                            continue
                        if (first + second + third + fourth) == target:
                            ans.add(tuple(sorted([first, second, third, fourth])))
        return ans


# ip = 2, 10
# ip = [1, 3, 2, 1, 3, 5], 3
# ip = [1, 0, -1, 0, -2, 2], 0
ip = [1, 0, -1, 0, -2, 2], 0

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
output = Solution().fourSum(*ip)
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
