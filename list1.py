#Python program to interchange first and last elements in a list
def swaplist(newlist):
    n=len(newlist)
    temp=newlist[0]
    newlist[0]= newlist[n-1]
    newlist[n-1]=temp
    print(newlist)

newlist=[1,2,3,4,5,6]
swaplist(newlist)