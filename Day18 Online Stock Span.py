class StockSpanner:

    def __init__(self):
        self.stacks = []

    def next(self, price: int) -> int:
        n = 1
        while self.stacks:
            val, num = self.stacks[-1]
            if price < val:
                self.stacks.append((price, n))
                return n
            else:
                n += num
                self.stacks.pop()
        self.stacks.append((price, n))
        return n
        


# Your StockSpanner object will be instantiated and called as such:
# obj = StockSpanner()
# param_1 = obj.next(price)