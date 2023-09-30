class Solution(object):
    def eraseOverlapIntervals(self, intervals):
        """
        :type intervals: List[List[int]]
        :rtype: int
        """


# node = TreeNode(1, TreeNode(2, TreeNode(4, TreeNode(5))), TreeNode(3, TreeNode(6), TreeNode(7)))
# input = TreeNode(1, TreeNode(2), TreeNode(3))
# input1 = TreeNode(1, TreeNode(2), TreeNode(3))
# input = TreeNode(1, TreeNode(2), TreeNode(3))
# input = TreeNode(1, TreeNode(2, TreeNode(4)), TreeNode(3, TreeNode(5), TreeNode(6)))
# input1 = TreeNode(1, TreeNode(2, TreeNode(4), TreeNode(5)), TreeNode(3, TreeNode(6)))
# input1 = TreeNode(-100, TreeNode(-200, TreeNode(-20), TreeNode(-5)), TreeNode(-300, TreeNode(-10)))
# input1 = TreeNode(4, TreeNode(2, TreeNode(1), TreeNode(3)), TreeNode(7))
# input1 = TreeNode(1, TreeNode(2, TreeNode(4, TreeNode(5))), TreeNode(3))
# input1 = TreeNode(2)
input2 = 'abc'
trie = Trie()
# trie.insert('app')
# trie.insert('apple')
# trie.insert('beer')
trie.insert('add')
# trie.insert('jam')
# trie.insert('rental')
# trie.insert('apps')
# trie.insert('ap')
trie.insert('ad')
# output = trie.search('abc')
# output = trie.search('apps')
# print(output)
# output = trie.search('app')
# print(output)
output = trie.search('ad')
# output = trie.startsWith('ad')
print(output)
