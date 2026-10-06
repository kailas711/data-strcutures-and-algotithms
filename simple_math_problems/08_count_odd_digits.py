class solution:
    def solution(self, num:int)->bool:
        has_odd = False
        while num > 0:
            digit = num % 10
            if digit % 2 != 0:
                has_odd = True
            else:
                num = num // 10
            num = num // 10
        return has_odd


    
NUM = 2668
sol = solution()
result = sol.solution(NUM)
print(result)