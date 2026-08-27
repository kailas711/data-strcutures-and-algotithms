class Solution:
    # function for basic approach
    def solution_1_n(self, num:int, counter:int):
        # Check base condition for recusion to stop
        print(counter)
        if counter >= num:
            return
        else: 
            self.solution_1_n(num, counter+1)  

    def solution_n_1(self, num:int, counter:int):  
        print(counter)
        # Check base condition for recusion to stop
        if counter < 0:
            return 
        else:
            self.solution_n_1(num, counter-1)
        
sol = Solution()
NUM = 4
result = sol.solution_1_n(NUM, counter=1)
result = sol.solution_n_1(NUM, counter=NUM)