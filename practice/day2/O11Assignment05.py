import math
x="145"
sum = 0
for i in range(0,len(x)):
    if(x[i]!=0):
        sum += math.factorial(int(x[i]))
if(sum == int(x)):
    print("magic number")
    print(sum)
