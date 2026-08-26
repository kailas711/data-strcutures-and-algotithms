class Solution:
    # function for basic approach
    def solution(self, name:str, times: int, counter:int):
        # Define what the funciton does
        print(f"The name is {name}")
        # Check base condition for recusion to stop
        if counter == times:
            return
        else: 
            self.solution(name, times, counter+1)        
        
sol = Solution()
NUM = 7
NAME = "MAX"
result = sol.solution(name=NAME, times=NUM, counter=0)
