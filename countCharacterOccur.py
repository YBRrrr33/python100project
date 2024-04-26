# This project is to count the occurrence of character
def count_character(s):
    # {} is used to define sets and dictionaries in python and [] is used to define a list in Python.
    # set is unordered and list is ordered
    # In Python, dictionaries are represented using curly braces {} with key-value pairs inside,
    # separated by colons :, like {"key1": value1, "key2": value2}.
    count = {}
    for i in s:
        if i in count:
            count[i] += 1
        else:
            count[i] = 1

    print(count)


print(count_character(input("Type in your sentence:")))

