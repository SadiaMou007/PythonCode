"""
Sadia Islam (16CSE007)
Problem 7: Write a program for Binary Search.
"""


def binary_search(arr, low, high, x):

    # Check base case
    if high >= low:

        mid = (high + low) // 2

        # If element is present at the middle itself
        if arr[mid] == x:
            return mid
        elif arr[mid] > x:
            return binary_search(arr, low, mid - 1, x)
        else:
            return binary_search(arr, mid + 1, high, x)

    else:
        return -1

arr = []
n = int(input("Enter number of elements : "))
print("Enter sorted array numbers:")

for i in range(0, n):
    elem = int(input())

    arr.append(elem)

arr.sort()
print(arr)

x = int(input("Enter search value : "))


# Function call
result = binary_search(arr, 0, len(arr)-1, x)

if result != -1:
    print("Element is present at index", str(result + 1))
else:
    print("Element is not present in array")