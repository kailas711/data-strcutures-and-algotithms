class Solution:
    # function for basic approach
    def solution(self, num:int)->bool:

        power=len(str(num)) # number of digits
        original_number = num
        armstrong = 0 # store the sum

        while num>0:
            # Get the last digit, apply power and sum it to armstrong
            LastDigit = num%10
            armstrong += LastDigit ** power
            # Removed the last digit as it was used
            num = num//10

        return original_number==armstrong
        
sol = Solution()
NUM = 153
result = sol.solution(NUM)
print(f"Is the number {NUM} an Armstrong number? {result}")
