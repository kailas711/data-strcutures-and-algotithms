class Solution:
    # function to reverse a digit
    # any reverse digit method from the reverse_digit.py works
    def reverse_digit(self, digit:int)->int:
        # dealing with negative numbers 
        digit = abs(digit)
        #storing the reversed number
        reverse = 0
        while(digit>0):
            # Extracting the last digit
            last = digit%10
            # reversing 
            reverse = reverse * 10 + last
            # removing the last digit 
            digit = digit//10
        return reverse
      
    def check_palindrome(self, num:int)->int:
        reverse = self.reverse_digit(num)
        if reverse == num:
            return "Palindrome Number"
        else:
            return "Not Palindrome Number"
        

sol = Solution()
print(sol.check_palindrome(878))
