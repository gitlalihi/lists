# Python Program to Swap Two Elements in a List
def swapposition(newlist,pos1,pos2):
    newlist[pos1],newlist[pos2]= newlist[pos2],newlist[pos1]
    print(newlist)
    
newlist=[1,2,3,4,5,6]
swapposition(newlist,pos1=2,pos2=5)