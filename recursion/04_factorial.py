class Solution:
    # function for basic approach
    def solution(self, num:int):
        # Check base condition for recusion to stop
        if num==0:
            return 1 # factorial of 0 is 1
        else:
            return num * self.solution(num-1)
                
sol = Solution()
NUM = 4
result = sol.solution(NUM)
print(f"The factorial of {NUM} is {result}")
