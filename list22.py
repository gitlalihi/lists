# python program to remove an empty list within a list
list1 =[1,3,45,[],456,34,890,[],100,25]
def remove_empty_list(list1):
    list2=[]
    for i in list1:
        if i:
            list2.append(i)
    return list2

print(f"Your  original list is: {list1}")
print(f"Your modified list is: {remove_empty_list(list1)}")        
