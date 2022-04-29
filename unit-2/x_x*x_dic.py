'''10.Program to generate and print a dictionary that contains a number (between 1 
and n) in the form (x, x*x). 
Sample Input: (n=5) : 
Expected Output : {1: 1, 2: 4, 3: 9, 4: 16, 5: 25}
'''
n = int(input("enter a number of value:"))
dic = {}

for i in range(1,(n+1)):
    keys = int(i)
    values = keys*keys 
    dic[keys] = values
print(dic)


