#######################################
# 정보통계학과 
# 학번 : 2019015020 
# 이름 : 오진석
# 작성일 : 09.14
#######################################

from Function import find_min_max
from Function import sum_range

data = [5, 3, 8, 4, 9, 1, 6, 2, 7]
print("(min,max) = ", find_min_max(data))
print("sum = ", sum_range(1, 10))

'''
(min,max) =  (1, 9)
sum =  45
'''

# math모듈
from math import pow, sqrt

result = pow(2, 10)
dist = sqrt(1000)

print(result)
print(dist)

'''
1024.0
31.622776601683793
'''

'''
# 이것도 가능
import Function 

data = [5, 3, 8, 4, 9, 1, 6, 2, 7]
print("(min,max) = ", Function.find_min_max(data))
print("sum = ", Function.sum_range(1, 10))
'''