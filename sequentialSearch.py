# sequential search: 按顺序查找
# Lists are ordered collections of items. They can contain elements of different types and are mutable,
# meaning you can modify their contents. Lists are created using square brackets
def search(list,n):
    found = False
    for i in list:
        if i == n:
            found = True
            break
            #The loop continues to iterate over the remaining elements in the list until it reaches the end.
            # if I delete break
    return found

numbers = list(range(0,20))
print(search(numbers, 3))