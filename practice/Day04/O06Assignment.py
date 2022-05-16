
print("Months in order".center(40, "-"))
import calendar
month_list = list(calendar.month_name)
months = ['december', 'august', 'october', 'april', 'february', 'november', 'january', 'september', 'may', 'march', 'july', 'june']
res = sorted(months, key=calendar.month_name.index)
print(res)


print("Identity Matrix".center(40, "-"))
size = int(input("Enter the size of matrix: "))
for row in range(0, size):
    for colum in range(0, size):
        if(row == colum):
            print("1 ", end=" ")
        else:
            print("0 ", end=" ")
    print()