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

    def nextPermutation(self, nums):
        """
        :type nums: List[int]
        :rtype: None Do not return anything, modify nums in-place instead.
        """

        def swap(a, b):
            nums[a], nums[b] = nums[b], nums[a]

        length = len(nums)

        if length == 1:
            return

        if length == 2:
            swap(0, 1)
            return

        p2 = length - 1
        while p2 >= 0:
            p1 = p2 - 1

            if p2 == 0:
                nums.sort()
                return

            if nums[p1] < nums[p2]:
                next_minimum = p2
                for i in range(p2, length):
                    if nums[p1] < nums[i] < nums[next_minimum]:
                        next_minimum = i
                swap(p1, next_minimum)
                msorted = sorted(nums[p2: length])
                for i in range(len(msorted)):
                    nums[p2 + i] = msorted[i]
                return
            p2 -= 1


# ip = [2, 10]
# ip = [2]
# ip = [1, 3, 2, 1, 3, 5], 3
# ip = [1, 0, -1, 0, -2, 2], 0
# ip = "aa", "a"
# ip = "aa", "a*"
# ip = "a", "a"
# ip = "ab", ".*"
# ip = "aab", "c*a*b"
# ip = "aaaaaaaaaaaaaaaaaaab", "ab"
# ip = 'madhatsadbadhad', ['sad', 'bad', 'hat']
# ip = "barfoothefoobarman", ["foo", "bar"]
# ip = "wordgoodgoodgoodbestword", ["word", "good", "best", "word"]
# ip = "wordgoodgoodgoodbestword", ["word", "good", "best", "good"]
# [6, 5, 4, 3, 2, 1]
ip = [1, 5, 4, 3, 2]
# ip = [1, 4, 5, 3, 2]
# ip = [1, 3, 5, 2, 4]
# ip = [1, 5, 3, 4, 2]
# ip = 'pjzkrkevzztxductzzxmxsvwjkxpvukmfjywwetvfnujhweiybwvvsrfequzkhossmootkmyxgjgfordrpapjuunmqnxxdrqrfgkrsjqbszgiqlcfnrpjlcwdrvbumtotzylshdvccdmsqoadfrpsvnwpizlwszrtyclhgilklydbmfhuywotjmktnwrfvizvnmfvvqfiokkdprznnnjycttprkxpuykhmpchiksyucbmtabiqkisgbhxngmhezrrqvayfsxauampdpxtafniiwfvdufhtwajrbkxtjzqjnfocdhekumttuqwovfjrgulhekcpjszyynadxhnttgmnxkduqmmyhzfnjhducesctufqbumxbamalqudeibljgbspeotkgvddcwgxidaiqcvgwykhbysjzlzfbupkqunuqtraxrlptivshhbihtsigtpipguhbhctcvubnhqipncyxfjebdnjyetnlnvmuxhzsdahkrscewabejifmxombiamxvauuitoltyymsarqcuuoezcbqpdaprxmsrickwpgwpsoplhugbikbkotzrtqkscekkgwjycfnvwfgdzogjzjvpcvixnsqsxacfwndzvrwrycwxrcismdhqapoojegggkocyrdtkzmiekhxoppctytvphjynrhtcvxcobxbcjjivtfjiwmduhzjokkbctweqtigwfhzorjlkpuuliaipbtfldinyetoybvugevwvhhhweejogrghllsouipabfafcxnhukcbtmxzshoyyufjhzadhrelweszbfgwpkzlwxkogyogutscvuhcllphshivnoteztpxsaoaacgxyaztuixhunrowzljqfqrahosheukhahhbiaxqzfmmwcjxountkevsvpbzjnilwpoermxrtlfroqoclexxisrdhvfsindffslyekrzwzqkpeocilatftymodgztjgybtyheqgcpwogdcjlnlesefgvimwbxcbzvaibspdjnrpqtyeilkcspknyylbwndvkffmzuriilxagyerjptbgeqgebiaqnvdubrtxibhvakcyotkfonmseszhczapxdlauexehhaireihxsplgdgmxfvaevrbadbwjbdrkfbbjjkgcztkcbwagtcnrtqryuqixtzhaakjlurnumzyovawrcjiwabuwretmdamfkxrgqgcdgbrdbnugzecbgyxxdqmisaqcyjkqrntxqmdrczxbebemcblftxplafnyoxqimkhcykwamvdsxjezkpgdpvopddptdfbprjustquhlazkjfluxrzopqdstulybnqvyknrchbphcarknnhhovweaqawdyxsqsqahkepluypwrzjegqtdoxfgzdkydeoxvrfhxusrujnmjzqrrlxglcmkiykldbiasnhrjbjekystzilrwkzhontwmehrfsrzfaqrbbxncphbzuuxeteshyrveamjsfiaharkcqxefghgceeixkdgkuboupxnwhnfigpkwnqdvzlydpidcljmflbccarbiegsmweklwngvygbqpescpeichmfidgsjmkvkofvkuehsmkkbocgejoiqcnafvuokelwuqsgkyoekaroptuvekfvmtxtqshcwsztkrzwrpabqrrhnlerxjojemcxel', [
#     "dhvf", "sind", "ffsl", "yekr", "zwzq", "kpeo", "cila", "tfty", "modg", "ztjg", "ybty", "heqg", "cpwo", "gdcj",
#     "lnle", "sefg", "vimw", "bxcb"]
# ip = [2, 2, 2, 2, 2], 8
# ip = [0, 0, 0, 0], 0

# ip = [1], 1
# ip = [2], 3
# ip = [4, 2, 0, 2, 2, 1, 4, 4, 1, 4, 3, 2], 2
# ip = [1, 3, 2, 1, 3, 5], 1
# ip = [3, 2, 2, 3], 3
# ip = [1, 2, 5, 6], 5
# ip = [1, 3, 5], 4
# ip = [1, 3, 5], 2
# ip = "23"
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
output = Solution().nextPermutation(ip)
print(ip)
print(output)

# nums = [0, 0, 1, 1, 1, 2, 2, 3, 3, 4]  # Input array
# expectedNums = [0, 1, 2, 3, 4]  # The expected answer with correct length
#
# k = Solution().removeDuplicates(nums)  # Calls your implementation
#
# assert k == len(expectedNums)
# for colIndex in range():
#     assert nums[colIndex] == expectedNums[colIndex];
