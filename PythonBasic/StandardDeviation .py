"""
Sadia Islam (16CSE007)
Problem 5: Write a program to find the standard deviation of a given set of data.
"""

arr = [2,4,6,10,8]
sum = 0
for i in range(len(arr)):
    sum = sum + arr[i]

mean_of_observations = sum/len(arr)

sum_of_squared_deviation = 0

for i in range(len(arr)):
    sum_of_squared_deviation += (arr[i]- mean_of_observations)**2

Standard_Deviation = ((sum_of_squared_deviation)/len(arr))**0.5
print("Standard Deviation of given number is ",Standard_Deviation)