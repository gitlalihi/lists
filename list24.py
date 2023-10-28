# Python | Count occurrences of an element in a list
list1 = []
num = int(input("Enter  range of number of elements in list: "))
for i in range(1, num + 1):
    ele= int(input("Enter elements: "))
    list1.append(ele)
print(list1)
x= int(input("Enter your number to find the occurrences in your list: "))
def count_occurences(list1,x):
    count = 0
    for i in list1:
        if i == x:
            count = count + 1
    return count
print("Your {} has  {} ocurrences".format(x,(count_occurences(list1,x))))


        