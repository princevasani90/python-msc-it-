"""display all failed rules

missing roll number
roll number should be from 1 to n 
one roll number is missing 
find the missing roll number without sorting

example:1 2 3 5 6
output: 4"""

n = int(input("enter number of student: "))

roll = list(map(int, input("enter roll number: ")))

for i in range(1, n + 1):
    if i not in roll:
        print("missing roll number:",i)
