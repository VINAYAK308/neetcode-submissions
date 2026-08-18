class Solution:
    def countBits(self, n: int) -> List[int]:
        output = []

        for i in range(n + 1):
            binary = bin(i)
            count = binary.count('1')
            output.append(count)

        return output