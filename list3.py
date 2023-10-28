#Python programTo Find the Length of a List in Python
def find_length(newlist):
    x=0
    for i in enumerate(newlist):
        x=x+1
    print(x)
newlist=[1,2,3,4,5,6]
find_length(newlist)       

    