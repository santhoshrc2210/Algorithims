'''Calculating the sum of the elements between 40-60 100th row 
   pascals triangle'''

import math
sum=0.0

for i_element in range(40,60):
    ith_ele=(math.factorial(100)/(math.factorial(i_element)*math.factorial(100-i_element)))
    sum+=float(ith_ele)/(2**100)
    
print sum    
    
