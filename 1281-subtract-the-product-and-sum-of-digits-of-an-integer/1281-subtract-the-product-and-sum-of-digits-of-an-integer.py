class Solution:
    def subtractProductAndSum(self, n: int) -> int:
        temp = n
        sum1 = 0
        product = 1

        while (temp>0):
            rem = temp%10
            temp//=10
            sum1+=rem
            product*=rem
        return product-sum1
