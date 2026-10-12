class Solution:
    def isPerfect(self, n: int) -> bool:
        sum = 0
        for i in range(1,n):
            if n % i == 0:
                sum += i
        if sum == n:
            return True
        else:
            return False
# check for 1 and 0 input 