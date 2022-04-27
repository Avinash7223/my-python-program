"""Program to get the maximum and minimum value in a dictionary"""

n = int(input("enter a number of value:"))
dic = {}

for i in range(n):
    keys = input() 
    values = input() 
    dic[keys] = values
print(dic)

dic[keys].sort()

print(" maxi and minu")

print(dic)
