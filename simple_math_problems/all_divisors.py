class Solution:
    def divisors(self, n):
        n = abs(n)
        divisors = []
        if n == 0:
            return 0
        else:
            for i in range(1,n+1):
                if n%i==0:
                    divisors.append(i)

            return divisors

sol = Solution()
print(sol.divisors(-1))
