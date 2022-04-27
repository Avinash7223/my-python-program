'''Given list of tuples, remove all the tuples with length K.
Input : test_list = [(4, 5), (4, ), (8, 6, 7), (1, ), (3, 4, 6, 7)], K = 2
Output : [(4, ), (8, 6, 7), (1, ), (3, 4, 6, 7)]
Explanation : (4, 5) of len = 2 is removed.
'''
list1 = []
tup = ()
total1 = int(input("Enter number of elements of list 1 : "))
for i in range(0, total1):
    total2 = int(input())
    for j in range(0, total2):
        numa=int(input())
        num=tup.append(numa)
    list1.append(num)
    
print(list1)
print(tup)
