"""
Sadia Islam (16CSE007)
Problem 6: Write a program to find the factors of a given number.
"""
Number = int(input("Enter any number: "))

print("The factors of",Number,"are: ")
for i in range(1, Number + 1):
    if Number % i == 0:
        print(i)