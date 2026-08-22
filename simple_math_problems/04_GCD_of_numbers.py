'''
The GCD of two numbers is the largest number that divides both of them without leaving a remainder. 
'''
class Solution:
    # define the solution function 
    # brute force
    def solution1(self, num1:int, num2:int)->int:
        gcd = 1
        # the GCD of 2 numbers won't be bigger than the smallest number
        for i in range(1,min(num1,num2)+1):
            # check if i is the common factor 
            if num1%i==0 and num2%i==0:
                gcd = i

        return gcd
    
    # Optimial solution, Euclidean 
    # Repeatedly subtract the smaller number from the larger number until one of them becomes 0.
    # Repeatedly get the remainder of bigger/smaller using modulus 
    def solution2(self, num1:int, num2:int)->int:
        while num1>0 and num2>0:
            # if num1 is greater than num2 then get the remainder and update num1
            if num1>num2:
                num1 = num1%num2
            # else if num2 is greater than num1 the get the remainder and update num2
            # in other words, this is the subtraction step. 
            else:
                num2 = num2%num1 
        # If num1 becomes 0 then num2 is the GCD
        if num1 == 0:
            return num2 
        else:
            return num1
            

# Initialize the solution class and call the function. 
sol = Solution()
NUM1=100
NUM2=25
#result = sol.solution1(NUM1, NUM2)
result = sol.solution2(NUM1, NUM2)
print(f"The common factors b/w {NUM1} and {NUM2} is {result}")
        