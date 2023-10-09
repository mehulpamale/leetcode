# leetcode submit region begin(Prohibit modification and deletion)
class ListNode:
    def __init__(self, key=None, val=None, next=None):
        self.key = key
        self.val = val
        self.next = next


class LinkedList:
    def __init__(self):
        self.start = None
        self.head = None

    def get(self, key):
        mhead = self.start
        while mhead:
            if mhead.key == key:
                return mhead.val
            mhead = mhead.next

    def _append(self, key, val):
        node = ListNode(key, val)
        if self.head:
            self.head.next = node
            self.head = self.head.next
        else:
            self.head = node
            self.start = self.head

    def put(self, key, val):
        mhead = self.start
        while mhead:
            if mhead.key == key:
                mhead.val = val
                return
            mhead = mhead.next
        self._append(key, val)

    def remove(self, key):
        if not self.head:
            return
        mhead = self.start
        while mhead and mhead.next:
            if mhead.next.key == key:
                to_remove = mhead.next
                mhead.next = mhead.next.next
                to_remove.next = None
            mhead = mhead.next
        if mhead.key == key:
            self.head = None
            self.start = None


class MyHashMap(object):
    size = 10

    def __init__(self):
        self.ls = [LinkedList() for i in range(0, self.size)]

    def hash(self, key):
        return key % self.size

    def put(self, key, value):
        """
        :type key: int
        :type value: int
        :rtype: None
        """
        hc = self.hash(key)
        self.ls[hc].put(key, value)

    def get(self, key):
        """
        :type key: int
        :rtype: int
        """
        hc = self.hash(key)
        res = self.ls[hc].get(key)
        return res if res is not None else -1

    def remove(self, key):
        """
        :type key: int
        :rtype: None
        """
        hc = self.hash(key)
        self.ls[hc].remove(key)


# Your MyHashMap object will be instantiated and called as such:
# obj = MyHashMap()
# obj.put(key,value)
# param_2 = obj.get(key)
# obj.remove(key)
# leetcode submit region end(Prohibit modification and deletion)

mymap = MyHashMap()
mymap.put(1, 2)
# mymap.put(11, 2)
mymap.put(2, 3)
# mymap.put(3, 1)
# print(mymap)
# mymap.put(2, 6)
# print(mymap)
# mymap.put(2, 4)
mymap.remove(27)
mymap.put(16, 53)
print(mymap.get(16))
