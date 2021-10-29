"""
Sadia Islam (16CSE007)
Problem 2: Write a python program that calculates the Body Mass Index (BMI) and categories it as
underweight, normal, overweight, obese based on standard measurement.
"""

Height = float(input("Enter height: "))
Weight = float(input("Enter weight: "))

BMI = Weight/(Height**2)

print("The BMI is",format(BMI))

print("Category: ", end='')
if (BMI < 18.5):
	print("Underweight")

elif ( BMI >= 18.5 and BMI < 24.9):
	print("Normalweight")

elif ( BMI >= 24.9 or BMI < 30):
	print("Overweight")

elif ( BMI >=30):
	print("Obese")