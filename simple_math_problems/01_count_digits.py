import math 

class Solution:
    # function to count digits.
    def digit_counter(self, N: int) -> int:
        N = abs(N)
        if N == 0:
            return 1
        
        counter = 0
        while N > 0:
            # floor divison.
            N = N // 10
            counter +=1
        # returns the counter.
        return counter

    # 1st alternative solution.
    # Convert to string and get the length
    def alternative_1(self, N:int) -> int:
        N = abs(N)
        return 0 if N == 0 else len(str(N))

    # The logarithmic base 10 of a positive integers gives the number of digits in n
    # 2nd alternative solution which is optimal 
    def alternative_2(self, N : int) -> int:
        # We add 1 to the result to ensure that the count is correct even for numbers that are powers of 10.
        count = int(math.log10(N)+1)
        return count

if __name__ == "__main__":
    sol = Solution()
    N = -6778
    res = sol.alternative_2(N)
    print(f"Number of digits in {N} is {res}")  
