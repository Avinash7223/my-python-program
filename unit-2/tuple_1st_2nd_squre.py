'''Given a list of numbers of list, write a Python program to create a list of tuples 
having first element as the number and second element as the square of the 
number'''

lister = []
total = int(input("Enter number of elements : "))
for i in range(0, total):
	num = int(input())
	lister.append(num) 
	
print(lister)

tuple = ()
for i in lister:
  numa=i*i
  tuple.append(numa)
    
print(tuple)
    