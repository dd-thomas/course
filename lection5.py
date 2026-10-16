def lection5():
    """
    Functions
    """
    def my_function(name : str):
        print(f"Hello from a function, {name}")

    def function_with_arbitrary_arguments(*names):
        joined = " ".join(names)
        print(f"Hello from a function, {joined}")

    def function_with_keyword_arguments(child3, child2, child1):
        print("The youngest child is " + child3)

    def product(arg1 : float, arg2 = 0., arg3 = 0.) -> float:
        return arg1 * arg2 * arg3
    
    def summ(arg1 : float, arg2 : float, /) -> float:
        return arg1 + arg2
    
    def empty_function():
        pass

    def function_with_arbitrary_keyword_arguments(**kwargs):
        supported_arguments = ["key1", "key2"]
        for k, v in kwargs.items():
            if k in supported_arguments:
                print(f"key:{k} value:{v}")
            else:
                print(f"Unsupported key {k}")

    # my_function("Thomas")
    # my_function(123)
    # my_function() # TypeError: my_function() missing 1 required positional argument: 'name'

    # Arbitrary arguments
    # function_with_arbitrary_arguments("T", "H", "O", "M")
    # function_with_arbitrary_arguments("Thomas")
    # function_with_arbitrary_arguments("1", "2", "3")

    # Keyword arguments
    # function_with_keyword_arguments(child1 = "Emil", child3 = "Linus", child2 = "Tobias")
    # function_with_keyword_arguments("Linus", "Tobias", "Emil")

    # Positional only arguments
    # print(summ(1, 4))
    # TypeError: summ() got some positional-only arguments passed as keyword arguments: 'arg1, arg2'
    # print(summ(arg1 = 1, arg2 = 4)) 

    # Default arguments
    # print(product(1))
    # print(product(2, 4))
    # print(product(arg2 = 2, arg1 = 4))
    # print(product(arg1 = 4))

    # The pass statement
    # empty_function()

    # Arbitrary keyword arguments, **kwargs
    # function_with_arbitrary_keyword_arguments(key1 = "value1", key2 = "value2", key3 = "value3")
    # function_with_arbitrary_keyword_arguments(key1 = "value1", key2 = "value2")

