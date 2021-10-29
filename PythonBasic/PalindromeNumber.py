"""
Sadia Islam (16CSE007)
Problem 10: 10.Write a program to find whether a given number is palindrome or not.
"""

Number = int(input("Enter number:")) #take input
temp = Number
rev = 0
while (Number>0):

    rem = Number%10
    rev= rev*10+ rem
    Number = Number//10
if (temp == rev):
    print("The number is a Palindrome!")
else:
    print("The number isn't a Palindrome!")