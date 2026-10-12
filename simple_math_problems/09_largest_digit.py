class Solution:
    def largestDigit(self, n):
        greater = 0
        while n >0:
            digit = n%10
            if digit > greater:
                greater = digit
            n = n//10
        return greater

#check for 1 and zero input