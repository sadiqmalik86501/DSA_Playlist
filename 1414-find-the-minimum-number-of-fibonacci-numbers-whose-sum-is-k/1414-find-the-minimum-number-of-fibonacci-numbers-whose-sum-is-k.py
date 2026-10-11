class Solution:
    def findMinFibonacciNumbers(self, k: int) -> int:
        a = 1
        b= 1
        if (k<2):
            return k
        while (b<=k):
            b+=a
            a = b-a
        return 1+self.findMinFibonacciNumbers(k-a)


