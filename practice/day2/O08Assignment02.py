
print("Pascal's Triangle".center(40,"-"))
rows = 6
a = 1
for i in range(rows+1):
    for space in range(rows-i+1):
        print(" ",end="")
    for j in range (i):
        if j==0 or i==0:
            a=1
        else:
            a=a*(i-j)//j
        print(a,end=" ")
    print()