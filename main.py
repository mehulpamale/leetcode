class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution(object):
    def isPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        p1, p2 = 0, len(s) - 1
        while p1 < p2:
            p1char = s[p1].lower()
            p2char = s[p2].lower()
            if not p1char.isalnum():
                p1 += 1
            elif not p2char.isalnum():
                p2 -= 1
            elif p1char.isalnum() and p2char.isalnum() and p1char == p2char:
                p1 += 1
                p2 -= 1
            else:
                return False
        return True


ip = ' '
ip2 = 3
output = Solution().isPalindrome(ip)
print(output)
