#Python program to find Cumulative sum of a list
list1 = []
num = int(input("Enter  range of number of elements in list: "))
for i in range(1, num + 1):
    ele= int(input("Enter elements: "))
    list1.append(ele)
print(list1)
new_list=[]
j=0
for i in range(0,len(list1)):
    j= j+list1[i]
    new_list.append(j)
print(new_list)
    
    

