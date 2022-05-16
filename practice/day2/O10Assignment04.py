"""
No.of prime between 50 to 150
"""
count = 0
for i in range (50, 150):
    for j in range(2, i):
        if(i % j) == 0:
            break
    else:
        count+= 1
        print(i)
print(f"No.of prime between 50 to 150 :{count}")