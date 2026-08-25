class Solution():
    # function for base solution
    def solution(self, num:int)->list:
        divisors = []
        for i in range(1,num):
            if num%i==0:
                divisors.append(i)
        return divisors

sol = Solution()
print(sol.solution(32))
