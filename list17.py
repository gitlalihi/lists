#Python program to print positive numbers in a list
list1 = []
num = int(input("Enter  range of number of elements in list: "))
for i in range(1, num + 1):
    ele= int(input("Enter elements: "))
    list1.append(ele)
print(list1)
#start=int(input("Enter your starting index:"))
#end=int(input("Enter your last index :"))
for i in range(len(list1)):
    if list1[i] >= 0:
       print("Your positive number in your list is :",list1[i])
 