class Solution:
# 1. SUM OF ARRAY
# using buil-in sum funciton
    def sum(self,arr, n):
        return sum(arr[:n])

# using recursion 
        if n<=0:
            return 0 
        return arr[n-1] + self.sum(arr, n-1)

# using the general loop 
        total = 0
        for num in arr:
            total +=num 
        return total
        
# COUNT ODD NUMBER 
    def countOdd(self, arr, n):
        # Your code goes here
        count = 0
        for num in arr:
            if num % 2 == 0:
                pass
            else:
                count +=1
        return count 

# Check sorted in Ascending 
    def arraySortedOrNot(self, arr, n):
        # i = 0
        # while i<n-1:
        #     if arr[i]>arr[i+1]:
        #         return False
        #     i+=1
        # return True
        for i in range(n-1):
            if arr[i]>arr[i+1]:
                return False 
        return True
