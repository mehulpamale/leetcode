from typing import List


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
    def sort(self, nums: List):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        length = len(nums)
        sorted_ptr = 0
        while sorted_ptr <= length - 1:
            to_insert = nums.pop(sorted_ptr + 1)
            for i in range(sorted_ptr - 1, 0, -1):
                curr = nums[i]
                m_next = nums[i + 1]
                if curr >= to_insert >= m_next:
                    nums.insert(m_next, to_insert)
                    sorted_ptr += 1
                    break

        return nums


ip = [-1, 0, 1, 2, -1, -4]
ip2 = 3
output = Solution().sort(ip)
print(output)
