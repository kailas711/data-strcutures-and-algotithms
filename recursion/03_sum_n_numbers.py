class Solution:
    # function for basic approach
    def solution(self, num:int):
        # Check base condition for recusion to stop
        if num<=0:
            return 0
        else: 
            return num + self.solution(num-1)
                
sol = Solution()
NUM = 4
result = sol.solution(NUM)
print(f"The sum of {NUM} is {result}")
