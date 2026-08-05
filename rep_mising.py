x=(1,2,2,3,4,4,4,5)
for i in set(x):
  if x.count(i) > 1:
    print("repeted number: ",i)
    
print("\n")
    
x=(1,3,4,6,8)
for i in range(1,9):
  if i not in x:
    print("missing number:",i)