def lection9():
    """
    Lists
    """
    l = [] # mutable list
    t = () # immutable list
    s = {} # dictionary
    l = ["apple", "banana", "cherry", 1, True, ["nested list"]]
    print(l)
    print(t)
    print(s)

    # Iterable
    # strings = 0
    # ints = 0
    # unexpected = 0
    # for i in l:
    #     print(f"type {type(i)} value {i}")

    #     if type(i) == str:
    #         strings += 1
    #     elif type(i) == int:
    #         ints += 1
    #     else:
    #         unexpected += 1

    # print(f"Total strings {strings} ints {ints} other {unexpected}")

    # single_element_seq = [1,]
    # single_value = 1
    # print(single_element_seq)
    # print(single_value)

    # Indexes
    # print(f"firstElement:{l[0]} LastElement:{l[-1]} SecondElement:{l[1]}")
    # IndexError
    # print(l[100500])

    # Index loop
    # i = 0
    # while i < len(l):
    #     print(l[i])
    #     i += 1

    # for i in range(len(l)):
    #     print(l[i])

    # Reverse loop
    # i = len(l)
    # while i > 0:
    #     print(l[i-1])
    #     i -= 1

    # Sliced list
    # Syntax: [start_index:stop_index:step]
    # for i in l[::-1]:
    #     print(i)
    # First three elements
    # print(l[0:3])
    # All elements from second
    # print(l[1::])
    # All elements from first to fourth
    # print(l[:4:])
    # Odd elements
    # print(l[::2])

    # list() constructor
    # immutable_list = ("apple", "banana", "cherry")
    # print(immutable_list)
    # immutable_list[2] = 3 # TypeError
    # mutable_list = list(immutable_list)
    # mutable_list.append("mango")
    # print(mutable_list)

    # check if item in list
    # l = ["apple", "banana", "cherry", "orange", "kiwi", "melon", "mango"]
    # if "melon" in l:
    #     print("found")

    # insert items
    # l.append("watermelon")
    # l.append("pear")
    # l.insert(0, "first")
    # print(l)

    # remove items
    # l.remove("not_present") # throws ValueError. Ensure that item is present before remove this one
    # l.remove("banana")
    # print(l)

    # removed = l.pop()
    # print(removed, l)
    # l.pop(2)
    # print(l)

    # Join list
    # print("\t".join(l))

