class Solution:
    # function to reverse a digit
    def reverse_digit(self, num:int)->int:
        # dealing with negative numbers 
        num = abs(num)
        #storing the reversed number
        reverse = 0
        while(num>0):
            # Extracting the last digit
            last = num%10
            # reversing 
            reverse = reverse * 10 + last
            # removing the last digit 
            num = num//10
        # returns reversed number
        return reverse

    def alternative1(self, num:int):
        # ensure num is positive
        num = abs(num)
        # convert num to a list of string
        reverse = list(reversed(str(num)))
        num = int(''.join(reverse))
        # return reversed num
        return num

    def alternative2(self, num:int):
        # ensure num is positive
        num = abs(num)
        # convert num to a list of string
        num = int(str(num)[::-1])
        # return reversed num
        return num

sol = Solution()
print(sol.reverse_digit(876))
print(sol.alternative1(567))
print(sol.alternative2(7890))
