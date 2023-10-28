#Python program to sort values of first list based on second list
list1 = []
num = int(input("Enter  range  of elements in list: "))
for i in range(1, num + 1):
    ele= input("Enter elements: ")
    list1.append(ele)
print(list1)

list2 = []
num2 = int(input("Enter  range  of elements in your second list: "))
for i in range(1, num2 + 1):
    ele1= int(input("Enter elements: "))
    list2.append(ele1)
print(list2)

combined_list = []
for i in range(min(len(list1), len(list2))):
    combined_list.append((list1[i], list2[i]))

def custom_sort(item):
    return item[1]
combined_list.sort(key=custom_sort)
sorted_list1 = [x[0] for x in combined_list]
print( sorted_list1)
