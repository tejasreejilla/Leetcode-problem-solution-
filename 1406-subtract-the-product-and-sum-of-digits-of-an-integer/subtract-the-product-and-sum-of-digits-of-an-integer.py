class Solution:
    def subtractProductAndSum(self, n: int) -> int:
        x=1
        y=0
        while n>0:
            i=n%10
            x*=i
            y+=i
            n=n//10
        return x-y

        