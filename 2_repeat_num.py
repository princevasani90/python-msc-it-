"""consecutive duplicate detector
accept n integers
display only those numbers that apper consecutively more than once 
input : 1 2 2 3 4 4 5
output : 2 4"""




x=tuple(input())

for i in range(len(x) -1):
    if x[i] == x[i + 1]:
        if i == 0 or x[i] != x[i - 1]:
            print(x[i])
