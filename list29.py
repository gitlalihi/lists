#Break a list into chunks of size N in Python
list1 = []
num = int(input("Enter  range of number of elements in list: "))
for i in range(1, num + 1):
    ele= int(input("Enter elements: "))
    list1.append(ele)
print(list1)

def slice_list(list1):
   start=0
   end=len(list1)
   N= int(input("Enter the number you want to break/slice the list into : "))
   for i in range(start,end,N):
    print(list1[i:i+N])

slice_list(list1)