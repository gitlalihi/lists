#Python | Cloning or Copying a list
list1=[10,15,23,45,67,88]
def copy_list(list1):
    # Using the Assignment operator
    #list2 = list1

    # Using extend buuilt in - function
    #list2=[]
    #list2.extend(list1)
    #return list2
    
    print("Your original list is:",list1)
print("Your copied list is : ",copy_list(list1) )