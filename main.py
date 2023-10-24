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
    def largestValues(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        if root is None:
            return []
        curr_lvl = [root]
        res = []
        temp = []
        while curr_lvl:
            mmax = curr_lvl[0].val
            for node in curr_lvl:
                mmax = max(node.val, mmax)
                if node.left:
                    temp.append(node.left)
                if node.right:
                    temp.append(node.right)
            curr_lvl = temp
            temp = []
            res.append(mmax)
            mmax = None
        return res


ip = ' '
ip2 = 3
output = Solution().largestValues(
    TreeNode(1, TreeNode(2, TreeNode(4), TreeNode(5)), TreeNode(3, TreeNode(6), TreeNode(7))))
print(output)
