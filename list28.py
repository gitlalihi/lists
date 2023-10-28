#Python - Sum of number digits in List
list1 = []
num = int(input("Enter  range of number of elements in list: "))
for i in range(1, num + 1):
    ele= int(input("Enter elements: "))
    list1.append(ele)
print(str(list1))
new_list=list(sum(int(d)for d in str(ele)) for ele in list1)
print("List Integer Summation : " + str(list(new_list)))


