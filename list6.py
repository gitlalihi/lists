# Reversing a List in Python
newlist=[]
n=int(input("Enter the length you want in the list :"))
for i in range(0,n):
    ele= int(input())
    newlist.append(ele)
print (newlist)   

def reverse_list(newlist):
    rev_list=newlist[::-1]
    print (rev_list)

reverse_list(newlist)    

