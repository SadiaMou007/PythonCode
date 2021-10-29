"""
Sadia Islam (16CSE007)
Problem 3:Write a program to find the mean, median, mode of a given set of data.
"""
from collections import Counter

arrN = [1, 2, 3, 3, 4, 4, 5, 6]
n = len(arrN)
print(n)

Sum = sum(arrN)
Mean = Sum / n #Calculate mean
print("Mean : " + str(Mean)) #print mean

arrN.sort()
if n % 2 == 0:
    M1 = arrN[n // 2]
    M2 = arrN[n // 2 - 1]
    Median = (M1 + M2) / 2  #Calculate median
else:
    Median = arrN[n // 2]
print("Median: " + str(Median)) #Print median

# Mode
D = Counter(arrN)
M = dict(D)
Mode = [k for k, v in M.items() if v == max(list(D.values()))] #calculate mode

if len(M) == n:
    Mode = "No mode found"
else:
    Mode = "Mode: " + ', '.join(map(str, M)) #print mode

print(Mode)