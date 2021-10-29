"""
Sadia Islam (16CSE007)
Problem 4: Write a program to find the range and IQR (Interquartile range) of a given set of data.
"""

import numpy as np

arr_list = []

# number of elements as input
n = int(input("Enter number of elements : "))

# iterating till the range
for i in range(0, n):
    elem = int(input())

    arr_list.append(elem)

print(arr_list)

q3, q1 = np.percentile(arr_list, [75, 25])
iqr = q3 - q1

print("Interquartile Range (IQR) is : " + str(iqr))
