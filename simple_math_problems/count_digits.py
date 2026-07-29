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

    # alternative solution.
    def alternative(self, N:int) -> int:
        N = abs(N)
        return 0 if N == 0 else len(str(N))

if __name__ == "__main__":
    sol = Solution()
    N = -6778
    res = sol.alternative(N)
    print(f"Number of digits in {N} is {res}")  
