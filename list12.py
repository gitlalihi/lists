#Python program to find N largest element from given list of integers
list1 = []
num = int(input("Enter number of elements in list: "))
for i in range(1, num + 1):
    ele= int(input("Enter elements: "))
    list1.append(ele)

n=int(input("Enter the size  in your above mentioned list ,you want to find the largest :"))

def maxelements(list1,n):
    final_list=[]
    for i in range (0,n):
        max=0
        for j in range (len(list1)):
            if list1[j]>max:
                max=list1[j]
        list1.remove(max)
        final_list.append(max)
    print(final_list)

maxelements(list1,n)                
         