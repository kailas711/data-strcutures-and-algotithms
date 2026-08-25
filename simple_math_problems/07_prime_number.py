import math 

class Solution():
    # Function for base solution
    def solution1(self, num:int)->bool:
        divisors = []
        for i in range(1, num+1):
            if num%i ==0:
                divisors.append(i)
        return divisors==[1,num]

    # Optimal(Using sqrt based solution from 06_divisors.py)
    def solution2(self, num:int)->bool:
        divisors = []
        for i in range(1, int(math.sqrt(num))+1):
            if num%i==0:
                divisors.append(i)
                # If a number d divides num then any number num/d divides num
                if i != num//i:
                    divisors.append(num//i)
        return divisors==[1,num]
    
sol = Solution()
N = 5
print(sol.solution1(N))
        
