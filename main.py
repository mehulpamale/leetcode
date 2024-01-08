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
    def findSubstring(self, s, words):
        """
        :type s: str
        :type words: List[str]
        :rtype: List[int]
        """
        total_word_count = len(words)
        word_length = len(words[0])
        length = word_length * total_word_count
        res = []

        original_counter = {}
        for i in words:
            if i in original_counter:
                original_counter[i] += 1
            else:
                original_counter[i] = 1

        for i in range(len(s) - length + 1):
            curr = s[i: i + length]
            curr_words = [''] * total_word_count

            for index, val in enumerate(curr):
                curr_words[(index // word_length)] += val

            curr_word_counter = {k: 0 for k in curr_words}

            for index in range(total_word_count):
                if curr_words[index] in words:
                    curr_word_counter[curr_words[index]] += 1

            for k, value in original_counter.items():
                if k not in curr_word_counter or value != curr_word_counter[k]:
                    break
            else:
                res.append(i)

        return res


# ip = 2, 10
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
ip = "wordgoodgoodgoodbestword", ["word", "good", "best", "good"]
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
output = Solution().findSubstring(*ip)
print(ip[0])
print(output)

# nums = [0, 0, 1, 1, 1, 2, 2, 3, 3, 4]  # Input array
# expectedNums = [0, 1, 2, 3, 4]  # The expected answer with correct length
#
# k = Solution().removeDuplicates(nums)  # Calls your implementation
#
# assert k == len(expectedNums)
# for colIndex in range():
#     assert nums[colIndex] == expectedNums[colIndex];
