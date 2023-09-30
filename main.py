class TrieNode(object):
    def __init__(self, val):
        self.val = val
        self.nodes = set()
        self.indexes = set()


class Trie(object):

    def __init__(self):
        self.nodes = {chr(i): TrieNode(chr(i)) for i in range(97, 123)}

    def insert(self, word):
        """
        :type word: str
        :rtype: None
        """
        last = None
        for i, c in enumerate(word):
            node = self.nodes[c]
            if last:
                last.nodes.add(node)
            last = node

    def search(self, word):
        """
        :type word: str
        :rtype: bool
        """
        length = len(word)
        last = None
        for i, c in enumerate(word):
            node = self.nodes[c]
            isfirst = i == 0
            islast = i == length - 1
            if isfirst:
                if not node.start:
                    return False
            if not isfirst and not islast:
                if not node.mid:
                    return False
            if islast:
                if node.end:
                    return True
                else:
                    return False
            if last and node not in last.nodes:
                return False
            last = node

    def startsWith(self, prefix):
        """
        :type prefix: str
        :rtype: bool
        """
        last = None
        for i, c in enumerate(prefix):
            node = self.nodes[c]
            if i == 0:
                if not node.start:
                    return False
            if last and node not in last.nodes:
                return False
            last = node
        return True


class Solution(object):
    def minFlips(self, a, b, c):
        """
        :type a: int
        :type b: int
        :type c: int
        :rtype: int
        """
        min_one_flip_required_bits = (a | b) ^ c
        two_flips_required_bits = a & b & min_one_flip_required_bits
        return bin(min_one_flip_required_bits).count('1') + bin(two_flips_required_bits).count('1')


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
# trie.insert('ad')
# output = trie.search('abc')
# output = trie.search('apps')
# print(output)
# output = trie.search('app')
# print(output)
output = trie.search('ad')
print(output)
