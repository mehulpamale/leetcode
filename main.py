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
    def intToRoman(self, num):
        """
        :type num: int
        :rtype: str
        """
        tenxzeros = {
            0: 'I',
            1: 'X',
            2: 'C',
            3: 'M',
        }
        fivexzeros = {
            0: 'V',
            1: 'L',
            2: 'D',
        }
        res = ''
        no_of_zeros = 0
        while num > 0:
            divisor = 10
            rem = num % divisor
            num //= divisor
            prefix = ''
            if rem < 4:
                prefix = tenxzeros[no_of_zeros] * rem
            elif rem == 4:
                prefix = tenxzeros[no_of_zeros] + fivexzeros[no_of_zeros]
            elif rem == 5:
                prefix = fivexzeros[no_of_zeros]
            elif rem < 9:
                prefix = tenxzeros[no_of_zeros] * rem
            elif rem == 9:
                prefix = tenxzeros[no_of_zeros] + fivexzeros[no_of_zeros]
            res = prefix + res

            no_of_zeros += 1

        return res


ip = 1451
ip2 = 3
output = Solution().intToRoman(ip)
print(output)
