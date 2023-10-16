class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution(object):
    def spiralMatrix(self, m, n, head):
        """
        :type m: int
        :type n: int
        :type head: Optional[ListNode]
        :rtype: List[List[int]]
        """
        arr = []
        for i in range(m):
            arr.append([-1] * n)

        right = ListNode(1)
        down = ListNode(-2)
        left = ListNode(-1)
        up = ListNode(2)

        right.next = down
        down.next = left
        left.next = up
        up.next = right

        direction = right

        i, j = 0, 0
        m -= 1
        n -= 1
        while head:

            num = head.val
            head = head.next

            arr[i][j] = num

            dir_val = direction.val
            if dir_val == 1:
                if j == n:
                    j -= 1
                    n -= 1
                else:
                    j += 1
            elif dir_val == -2:
                if i == m:
                    i -= 1
                    m -= 1
                else:
                    i += 1
            elif dir_val == -1:
                if j == 0:
                    j -= 1
                    n -= 1
                else:
                    j -= 1
            elif dir_val == -2:
                if i == 0:
                    i -= 1
                    m -= 1
                else:
                    i -= 1

        return arr


ip = [0]
ip2 = 3
output = Solution().spiralMatrix(3, 4, ListNode(1, ListNode(2, ListNode(3, ListNode(4, ListNode(5, ListNode(6,
                                                                                                            ListNode(7,
                                                                                                                     ListNode(
                                                                                                                         8,
                                                                                                                         ListNode(
                                                                                                                             9,
                                                                                                                             ListNode(
                                                                                                                                 10,
                                                                                                                                 ListNode(
                                                                                                                                     11,
                                                                                                                                     ListNode(
                                                                                                                                         12)))))))))))))
print(output)
