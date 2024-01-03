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

    def maxArea(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        min_pointer = 0
        max_pointer = len(height) - 1
        max_area = 0
        while min_pointer < max_pointer:
            distance = max_pointer - min_pointer
            
            min_height = min(height[min_pointer], height[max_pointer])
            current_area = min_height * distance
            max_area = max(current_area, max_area)

            if min_pointer > max_pointer:
                max_pointer += 1
            else:
                min_pointer += 1
        return max_area

# ip = 2, 10
# ip = [1, 8, 6, 2, 5, 4, 8, 3, 7]
ip = [2, 3, 4, 5, 18, 17, 6]
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
output = Solution().maxArea(ip)
print(output)

# nums = [0, 0, 1, 1, 1, 2, 2, 3, 3, 4]  # Input array
# expectedNums = [0, 1, 2, 3, 4]  # The expected answer with correct length
#
# k = Solution().removeDuplicates(nums)  # Calls your implementation
#
# assert k == len(expectedNums)
# for colIndex in range():
#     assert nums[colIndex] == expectedNums[colIndex];
