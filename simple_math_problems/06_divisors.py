import math 

class Solution():
    # function for base solution
    def solution1(self, num:int)->list:
        divisors = []
        for i in range(1,num):
            if num%i==0:
                divisors.append(i)
        return divisors

    # Optimal solution 
    # If d is a divisor of n then n/d is also a divisor of n. This property is symmetric on the square root of a number
    # After the squre root, the divisors decrease, example 1*36 becomes 36*1 
    def solution2(self, num:int)->list:
        square_root = math.sqrt(num)
        divisors = []
        for i in range(1,int(square_root)+1):
            # Collect divisors until square root
            if num%i==0:
                divisors.append(i)
            # num/divisor is also a divisor 
                if i != num//i:
                    divisors.append(num//i)
        return divisors

sol = Solution()
print(sol.solution2(32))
