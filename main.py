class StockSpanner(object):

    def __init__(self):
        self.prices = []
        self.stack = []

    def next(self, price):
        """
        :type price: int
        :rtype: int
        """
        prices = self.prices
        stack = self.stack
        prices.append(price)
        idx = len(prices) - 1
        while stack and prices[stack[-1]] <= price:
            stack.pop()
        prev_index = stack[-1] if stack else 0
        stack.append(idx)
        return idx - prev_index

    # input2 = [[1, 2], [2, 3], [3, 4], [1, 3]]


# input2 = [[1, 2], [1, 2], [1, 2]]
# input2 = [[1, 100], [11, 22], [1, 11], [2, 12]]
# input2 = [[-52, 31], [-73, -26], [82, 97], [-65, -11], [-62, -49], [95, 99], [58, 95], [-31, 49], [66, 98], [-63, 2],
#           [30, 47], [-40, -26]]
# input2 = [[0, 2], [1, 3], [2, 4], [3, 5], [4, 6]]
# input2 = 'God Ding'
s = StockSpanner()

output = s.next(100)
print(output)
output = s.next(80)
print(output)
output = s.next(60)
print(output)
output = s.next(70)
print(output)
output = s.next(60)
print(output)
output = s.next(75)
print(output)
output = s.next(85)
print(output)

# output = s.next(1)
# print(output)
# output = s.next(2)
# print(output)
# output = s.next(3)
# print(output)
# output = s.next(4)
# print(output)
# output = s.next(5)
# print(output)
# output = s.next(6)
# print(output)
# output = s.next(7)
# print(output)
