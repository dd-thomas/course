def lection6():
    """
    str
    """
    # print("Hello")
    # print('Hello')
    # print("""H
    #       'e
    #       l"
    #       l
    #       o""")
    # print("It's alright")
    # print('It\'s alright') # escape characters
    # # \' \"
    # # \\
    # # \n LF
    # # \r CR
    # # \t
    # # \b
    # # \f form feed
    # txt = "We are the so-called \"Vikings\" from the north."
    # print(txt)

    # a = "Hello, World!"
    # print(a[1], len(a))
    # print(a[10005]) # IndexError
    # Looping Through a String
    # for i in a:
    #     print(i)

    # Index based loop
    # i = 0
    # while i < len(a):
    #     print(a[i])
    #     i += 1

    # Check string
    txt = "The best things in life are free!"
    # print("free" in txt)
    # print("Free" in txt)
    # if "free" in txt:
    #     print("OK")
    
    # print("Free" not in txt)

    # String concatenation
    a = "Hello"
    b = "World"
    b += "!"
    print(a + " " + b)

    # Modify strings
    # a = " Hello,   World! "
    # print(a.upper())
    # print(a.lower())
    # print(a.strip())
    # print(a.replace("H", "A"))
    # print(a.replace("l", "1"))
    # print(a.replace("l", "1", 1))
    # print("h e l l o".split(" ")) # ['h', 'e', 'l', 'l', 'o']
    # print("c:/windows/fonts".split("/"))
    # print("%%%".join("hello")) # "h%%%e%%%l%%%l%%%o"

    # Slicing
    # b = "Hello, World!"
    # print(b[0]) # first
    # print(b[-1]) # last
    # print(b[2:5]) # llo
    # print(b[:5]) # Hello
    # print(b[5:]) # , World!
    # print(b[-5:-2]) # orl

    # Format
    age = 36
    spec = "programmer"
    # txt = "My name is John, I am " + str(age) + " and work as " + spec
    # print(txt)

    # String format
    # print("My name is John, I am {0} and work as {1}".format(age, spec)) # index based
    # print("My name is John, I am {} and work as {}".format(age, spec)) # without index
    # print("My name is John, I am {a} and work as {b}".format(a = age, b = spec)) # named

    # F-strings python 3.6
    # print(f"My name is John, I am {age} and work as {spec}")

