# Python program Multiply all numbers in the list using list comprehension
newlist=[]
n=int(input("Enter the length you want in the list :"))
for i in range(0,n):
    ele= int(input())
    newlist.append(ele)
print (newlist) 
def multiply(newlist):
    mul=1
    for i in newlist:
        mul= mul*i
    print("The total after multiplication of elements in the list is:", mul)
multiply(newlist)