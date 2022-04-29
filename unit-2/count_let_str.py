"""14.	Program for Counting occurrence of a certain element in a string, getting indexes that have matching elements.For ex -.In Rabbit count how many times b has occurred . Example-I have to go to a doctor and get myself checked. Count the number of occurrences of ‘to’"""

line=input("enter the statment:")

count=0
x=input("enter the charater:")

for i in line:
    if i == x :
        count=count+1
        
print("the number of charater ",count)