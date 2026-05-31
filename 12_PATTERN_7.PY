class Solution:
    def pattern7(self, n):
        for i in range(n):
            a=" "*(n-i-1)
            b="*"*(2*i+1)
            print(a+b)
            