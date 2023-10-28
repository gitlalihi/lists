#Python program to print even numbers in a list using for loop
list1 = []
num = int(input("Enter  range of number of elements in list: "))
for i in range(1, num + 1):
    ele= int(input("Enter elements: "))
    list1.append(ele)
print(list1)

for i in range(len(list1)):
    if list1[i] % 2 == 0:
       print("Your even number in your list is :",list1[i])
 
