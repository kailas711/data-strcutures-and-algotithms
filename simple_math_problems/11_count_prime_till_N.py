class Solution:
    def primeUptoN(self, n):
        prime = 0
        for i in range (1,n+1):
            divisors = []
            for j in range(1,i+1):
                if i % j == 0:
                    divisors.append(j)
                if divisors == [1,i]:
                    prime +=1
        return prime

sol = Solution()
print(sol.primeUptoN(10))
