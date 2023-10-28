#Python program to find second largest number in a list
list1 = []
num = int(input("Enter number of elements in list: "))
for i in range(1, num + 1):
    ele= int(input("Enter elements: "))
    list1.append(ele)

list2=list(set(list1))
list2.sort()
print("Second largest number is :" , list2[-2])
   
