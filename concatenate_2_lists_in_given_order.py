'''Concatenate two lists in the following order
i/p:
list1 = ["Hello ", "take "]
list2 = ["Dear", "Sir"]
o/p:
['Hello Dear', 'Hello Sir', 'take Dear', 'take Sir']
'''

list1 = ["Hello ", "take "]
list2 = ["Dear", "Sir"]
list3 = []

for i in list1:
    for j in list2:
        list3.append(i+j)


print("Expected result: ",list3)
