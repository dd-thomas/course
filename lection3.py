def lection3():
    """
    """
    # a = 33
    # b = 200
    # if b > a:
    #     print("b is greater than a")

    # Logical conditions:
    # == : a == b
    # != : a != b / not a == b
    # < : a < b
    # <= : a <= b
    # > : a > b
    # >= : a >= b

    # TypeError because lvalue and rvalue have different types
    # a = 33
    # b = "200"
    # if b > a:
    #     print("b is greater than a")
    # if type(b) == type(a) and b > a:
    #     print("b is greater than a")

    # Cast to bool
    # a = 33
    # b = 32
    # print(bool(b / a))
    # if b / a:
    #     print(b / a)

    # a = 33
    # b = 32
    # if b / a > 0.:
    #     print(b / a)

    # IndentationError
    # a = 33
    # b = 32
    # if b / a > 0.:
    # print(b / a)

    # elif
    # x = 0
    # if 0 <= x < 10:
    #     print("x in [0; 10)")
    # elif 19.5 < x < 19.6:
    #     print("x in (19.5; 19.6)")

    # else
    # x = 100
    # if 0 <= x < 10:
    #     print("x in [0; 10)")
    # elif 19.5 < x < 19.6:
    #     print("x in (19.5; 19.6)")
    # else:
    #     print("else")

    # Short hand if
    # x = 4
    # if 0 <= x < 10: print(f"{x} in interval [0, 10)")

    # Short hand if..else
    # x = 5
    # print("in interval") if 0 <= x < 10 else print("not in interval")

    # Logical operator or
    # x = 19.6
    # if 0 <= x < 10 or 19.5 < x < 19.6:
    #     print("x in interval")
    # else:
    #     print("not in interval")

    # Logical operator and
    # a = 200
    # b = 33
    # c = 500
    # if a > b and c > a:
    #     print("Both conditions are True")

    # Logical operator not
    # a = 33
    # b = 200
    # if not a > b: # equivalent to a < b
    #     print("a is NOT greater than b")

    # Nested if
    # x = 41

    # if x > 10:
    #     print("Above ten,")
    #     if x > 20:
    #         print("and also above 20!")
    # else:
    #     print("but not above 20.")

    # pass statement
    a = 33
    b = 200
    if a > b:
        pass # do nothing
    else:
        pass # do nothing

