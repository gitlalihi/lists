#Remove multiple elements from a list in Python
list1 = []
num = int(input("Enter  range of number of elements in list: "))
for i in range(1, num + 1):
    ele= int(input("Enter elements: "))
    list1.append(ele)
print(list1)

for i in list1:
    if i % 2== 0:
        list1.remove(i)
print("Modified list after removing even numbers is:" , list1)        

