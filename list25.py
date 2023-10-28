#Python | Remove empty tuples from a list
tuples=[('23','67','90'),(),('45','90','89'),()]
print("Your original list is:",tuples)
def remove_tuples(tuples):
    for i in tuples:
        if (i == ()):
            tuples.remove(i)
    return tuples

print(" Your list after  empty tuples removal is :" ,remove_tuples(tuples))