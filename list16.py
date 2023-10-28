#Python program to print all odd numbers in a range
list1 = []
num = int(input("Enter  range of number of elements in list: "))
for i in range(1, num + 1):
    ele= int(input("Enter elements: "))
    list1.append(ele)
print(list1)
start=int(input("Enter your starting position in your list:"))
end=int(input("Enter your last position in your list:"))
for i in range(start,end):
    if list1[i] % 2 != 0:
       print("Your odd number in your list is :",list1[i])
 