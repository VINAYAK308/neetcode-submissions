class Solution:
    def hammingWeight(self, n: int) -> int:
        x = int(n)
        y = bin(x)
        res = y.count('1')
        return res