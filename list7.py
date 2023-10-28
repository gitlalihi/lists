# Add  the elements in a list using list comprehnsion
newlist=[]
n=int(input("Enter the length you want in the list :"))
for i in range(0,n):
    ele= int(input())
    newlist.append(ele)
print (newlist) 

def add_list(newlist):
    i=0
    n= [i for i in newlist]
    x=sum(n)
    print("The total after addition of all elements in the list are :", x)

add_list(newlist)    