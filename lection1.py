# Global variables section
ONE_HOUR_MS = 1000 * 60 * 60
# 

def lection0():
    print("你好 Hello")
    someName = 1 # camel case myVariable
    some_name = 1 # snake case

# This is a special func for lection 1
def lection1():
    """
    func description
    return None
    """
    pass # do nothing a = 15
    a = 1
    # Skip this line until problem not solved
    # print(a + "error")
    # End error block
    # line = "line"
    # line = "1"
    # line "2"
    print("comment1", "comment2", "comment3", sep = "\t") # separate with tab \t LF \n  CR \r  CRLF\r\n 
    print("comment1", "comment2", "comment3") # default (separate with whitespace)
    print("comment1", "comment2", "comment3", sep = " ")
    print("comment1", "comment2", "comment3", sep = "||") # separate with ||
    print("comment1", end = " ")
    print("comment2", end = "\t")
    print("comment3") 

    # __str__
    result = 2024 / 14
    print(result)

    r = range(5)
    print(r)
    print(list(r))

    # input()
    # i = input("Please enter current year")
    # print("Current year is", i)
    # cast str -> int
    # print("Current year + 100 is", int(i) + 100) # because i is a string we need to cast this one to int

    # Math
    # + - * / // % **
    # a = int(input("Enter lenght:"))
    # b = int(input("Enter width:"))
    # p = (a + b) * 2 # 2 * a + 2 * b
    # s = a * b
    # # print("Perimeter={} Square={}".format(p, s))
    # print("Perimeter=", p, " Square=", s, sep = "")

    a = 5
    b = 2
    print(a / b) # cast int -> float
    print(int(a / b))
    print(a // b)
    print(a % b) # mod
    print(a ** 3) # a * a * a

    c = 2.5
    print(a * c)

    for i in range(3000):
        if i % 300 == 0:
            print(i)

    print("/" * 100)
    s1 = "string 1"
    s2 = "string 2"
    print(s1 + " " + s2)
    # print(s1 / s2) # Does not work
    # print(True / False) # Does not work
    print("/" * 100)

    # print(a + s1) # int + string not work

    # Example 1: fix "int + string" by casting int -> str
    print(s1 + " " + str(a)) # str(a) turns 5 into "5", so concatenation works

    # Example 2: build a date with sep and end
    day = 16
    month = 10
    year = 2026
    print(day, month, year, sep = ".", end = "\n\n") # 16.10.2026 followed by an empty line

    # Example 3: split milliseconds into minutes and seconds with // and %
    ms = 125000
    seconds_total = ms // 1000 # integer division drops the remainder: 125
    minutes = seconds_total // 60 # whole minutes: 2
    seconds = seconds_total % 60 # what's left after whole minutes: 5
    print("Minutes:", minutes, "Seconds:", seconds)
    print("One hour in minutes:", ONE_HOUR_MS // 1000 // 60) # uses the global variable

    # Example 4: even or odd numbers with % in a loop
    for i in range(6):
        if i % 2 == 0: # remainder 0 means the number divides by 2
            print(i, "is even")
        else:
            print(i, "is odd")

    # Example 5: rectangle perimeter and area without input()
    length = 4
    width = 2.5 # int * float gives float
    p = (length + width) * 2
    s = length * width
    print("Perimeter=", p, " Square=", s, sep = "") # Perimeter=13.0 Square=10.0
    print("-" * 30) # string repetition draws a separator line

