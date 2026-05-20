class Solution:
    def whileLoop(self, d: int) -> int:
        total = 0
        count = 0
        num = d

        while count < 50:
            if num > 0:
                total += num
                count += 1

            num += 10

        return total


