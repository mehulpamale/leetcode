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

    def threeSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        nums.sort()
        length = len(nums)
        ans = set()
        for i in range(length - 2):
            if i > 0 and nums[i] == nums[i - 1]:
                continue
            first = nums[i]
            j = i + 1
            k = length - 1
            while j < k:
                second = nums[j]
                third = nums[k]

                m_sum = first + second + third

                if m_sum > 0:
                    k -= 1
                elif m_sum < 0:
                    j += 1
                else:
                    ans.add((first, second, third))
                    j += 1
                    k -= 1
                    while j < k and nums[j] == nums[j - 1]:
                        j += 1
                    while j < k and nums[k] == nums[k + 1]:
                        k -= 1
        return ans


ip = [-1, 0, 1, 2, -1, -4]
ip2 = 3
output = Solution().threeSum(ip)
print(output)
