class Solution:
    def forLoop(self, low : int, high : int) -> int: 
        total=0
        for i in range(low,high+1):
            total +=i
        return total