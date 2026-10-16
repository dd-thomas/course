GLOBAL_Y = 300

def lection11():
    """
    scopes
    exceptions
    """
    y = 300

    def some_func():
        x = 300
        print(x)

    def some_func_2():
        some_func()
        print(y)

    def func_that_uses_local_y():
        # This is local variable
        y = 200
        print(y)

    def func_that_uses_global_y():
        global GLOBAL_Y
        GLOBAL_Y = 100

    def func_that_uses_nonlocal_y():
        nonlocal y
        y = 100

    # some_func()
    # some_func_2()

    # func_that_uses_local_y()

    # print(GLOBAL_Y)

    # func_that_uses_global_y()

    # print(GLOBAL_Y)

    # print("y before run func_that_uses_nonlocal_y()", y)

    # func_that_uses_nonlocal_y()

    # print("y after run func_that_uses_nonlocal_y()", y)

    # Exceptions
    # try
    # except 
    # else
    # finally

    # TypeError
    # a = 10
    # b = "14"
    # print(a + b)

    # try:
    #     print(x)
    # except NameError as e:
    #     print("NameError", e)
    # except Exception as e:
    #     print(type(e), e)  

    # try:
    #     print("Hello")
    # except:
    #     print("Something went wrong")
    # else:
    #     print("Nothing went wrong")
    # finally:
    #     print("This block will be called anyway")

    # try:
    #     print("Hello")
    #     raise RuntimeError("bla bla bla")
    # except RuntimeError as e:
    #     print("Something went wrong", e)
    # finally:
    #     print("This block will be called anyway")

    # try:
    #     print("No problem")
    #     try:
    #         print(x)
    #     except NameError as e:
    #         print(e)
    #         raise RuntimeError("From NameError")
    # except Exception as e:
    #     print("scope #1 exception:", type(e), e)

