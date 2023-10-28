#Program to print duplicates from a list of integers
list1 = []
num = int(input("Enter  range of number of elements in list: "))
for i in range(1, num + 1):
    ele= int(input("Enter elements: "))
    list1.append(ele)
print(list1)

new_list=[]

for i in list1: 
   if list1.count(i)>1:
       new_list.append(i)
print(" Your duplicates in the list are :" ,new_list)


