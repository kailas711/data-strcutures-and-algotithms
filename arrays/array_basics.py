class Solution:
# using buil-in sum funciton
    def sum(self,arr, n):
        return sum(arr[:n])

# using recursion 
        # if n<=0:
        #     return 0 
        # return arr[n-1] + self.sum(arr, n-1)

# using the general loop 
        # total = 0
        # for num in arr:
        #     total +=num 
        # return total
