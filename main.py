class Solution(object):
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """
        ans = 0
        min_limit = - 2 ** 31
        max_limit = -min_limit - 1
        while x != 0:
            ans *= 10
            ans += x % 10
            x //= 10
            if ans < min_limit or ans > max_limit:
                return -1
        return ans


ip = -123
ip2 = 1
output = Solution().reverse(ip)
print(output)
