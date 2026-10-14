class Solution:
  def LCM(self, n1, n2):

      multiples = [] 
      if n1<n2:
          smaller = n1
          larger = n2
      else: 
          smaller = n2 
          larger = n1
      
      for i in range(1,larger+1):
          if (i*smaller)%larger==0:
              multiples.append(i*smaller)    
      return (multiples[0])

sol = Solution()
print(sol.LCM(4,5))
