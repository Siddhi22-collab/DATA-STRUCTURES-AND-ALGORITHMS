class Solution:
    def pattern16(self, n):
        for i in range(1, n + 1):
            ch = chr(64 + i)
            print(ch * i)