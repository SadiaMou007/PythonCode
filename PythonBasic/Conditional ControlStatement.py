
var1 = int(input("Enter Marsk: "))

#simple if else
if var1 >= 33:
    print("Pass")
else:
    print("Fail")

#modulus operator
if var1 % 2 == 0:
    print("Even number")
else:
    print("Odd number")

#same for nested if else,inner if else etc
#3.Ternary operator
num1 = 5;
num2 = 6;
print(num1 if num1>num2 else num2)

#logical operator
ch = 'i'
if (ch == 'a' or ch == 'e' or ch == 'i' or ch == 'o' or ch == 'u'):
    print("Vowel")
else:
    print("Consonant")