"""
Sadia Islam (16CSE007)
Problem 1: Write a program to find the prime numbers from a given range.
"""
import math

LowerRange = int(input("Enter lower range:"))
UpperRange = int(input("Enter upper range:"))

for number in range(LowerRange, UpperRange + 1):
    if number > 1:
        l = math.sqrt(number)
        for i in range(2, int(l + 1)):
            if (number % i == 0):
                break
        else:
            print(number)


