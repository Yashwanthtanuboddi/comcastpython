# 1.Finding a string palindrome or not
my_str = "hello world"
rev_str = reversed(my_str)

if list(my_str) == list(rev_str):
    print("they are palindromes")
else:
    print("they are not  palindrome")

# 2.romoving odd index values of a string
print("-"*40)

str1 = input("Enter a string : ")
str2 = ''
for i in range(len(str1)):
    if(i%2==0):
        str2 = str2 + str1[i]
print("After removing the odd index: ", str2)

# 3.counting no
print("-"*40)

str1 = "IND IND AUS IRE PAK NEZ IND AUS WI ENG IND WI"
sub = "IND"
sub1 = "AUS"
sub2 = "ENG"
count = str1.count(sub)
count1 = str1.count(sub1)
count2 = str1.count(sub2)
print(F"IND occured {count} times in a str")
print(F"AUS occured {count1} times in a str")
print(F"AUS occured {count2} times in a str")


# 4
print("-"*40)
n = int(input("Enter the Index number :"))
s = input("Enter the String :")
mod_s = ''
for char in range(0, len(s)):

   if(char != n):
      mod_s += s[char]

print(f"mod_s : {mod_s}")

#5
print("-"*40)
str1 = input("Enter a mixed string: ")
res = []
temp = str1.split()
for i in temp:
    if  any (chr.isalpha() for chr in i ) and any  (chr.isdigit() for chr in i):
        res.append(i)
print("Both charcter and number : " + str(res))

# 6
print("-"*40)
str1 = input("Enter mixed string : ")
alph = 0
dig = 0
special = 0
for i in range(len(str1)):
    if(str1[i].isalpha()):
        alph = alph+1
    elif(str1[i].isdigit()):
        dig = dig+1
    else:
        special = special+1
print("Alphabets in string : ",alph)
print("Digits in string : ",dig)
print("Special in string : ",special)