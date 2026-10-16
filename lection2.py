from .lection1 import ONE_HOUR_MS

def lection2():
    """
    """
    some_variable = True # True / False
    print(some_variable)
    some_variable = "True" # bool -> str
    print(some_variable)

    # 2name = "2name" # Illegal
    name2 = "2name"
    # name 2 = "name 2" # Illegal
    # 2-name = "2-name" # Illegal
    # class = 1 # Illegal
    # def = "def" # Illegal

    # case sensitive variables
    name = "Thomas"
    Name = "Andreas"
    NaMe = "NaMe"
    NAME = "NAME"
    print(name, Name, NaMe, NAME)
    
    a = 5
    print(a + 5)
    print(a + 5.0)
    # print(a + some_variable) # lvalue rvalue have different types
    print(a, some_variable) # __str__
    # cast some_variable to int
    some_variable = True # True -- 1 False - 0
    some_variable = int(some_variable) # str float bool
    print(some_variable)

    x = str(3)
    y = int(3)
    z = float(3)
    print("x={} of type {}\ny={} of type {}\nz={} of type {}".format(x, type(x), y, type(y), z, type(z)))

    s = "Double quoted string"
    print(s)
    s = 'Single quoted string'
    print(s)
    s = """Triple
    quoted ]] \ D m, % \%
        string"""
    print(s)
    s = "Doubleeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeee\n"\
        "quoted\n"\
            "string"
    print(s)

    # Assign multiple values
    # name1 = "Thomas"
    # name2 = "Andreas"
    # name3 = "Tobias"
    name1, name2, name3 = "Thomas", 4.11111, "Tobias"
    print(name1, name2, name3)
    name1 = name2 = name3 = "New"
    print(name1, name2, name3)

    # Redeclaration of global variable
    # ONE_HOUR_MS = "bbbb"
    # print(ONE_HOUR_MS)

    # Using global variables
    hours = 2
    print("{} hours in milliseconds: {}".format(hours, hours * ONE_HOUR_MS))

def homework2():
    """
    """
    total_sum = 0.
    while True:
        try:
            total_sum += int(input("стоимость монитора: "))
            total_sum += int(input("стоимость системного блока: "))
            total_sum += int(input("стоимость клавиатуры: "))
            total_sum += int(input("стоимость мыши: ")) 
            break
        except ValueError:
            print("Недопустимые символы. Введите только целые числа.")
            total_sum = 0.
            continue

    print(f"Итоговая стоимость: {total_sum * 3}")

