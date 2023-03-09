#Reverse a list in python

list1 = [10,20,30,40,50]
print("Before reversing the list: ", list1)
reversed_list = []

for item in list1[-1::-1]:
    reversed_list.append(item)

print("Reversed list is :",reversed_list)
    

