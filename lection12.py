def lection12():
    """
    OOP
    """
    # Polymorphism
    # print("string") # str
    # print([1, 2, 3]) # list of ints
    # print(4) # int
    # a = 4
    # print(type(a), a)
    # a = "4"
    # print(type(a), a)

    # Incapsulation
    # s = "This i a string"
    # print(s.upper())

    # Inheritance
    class Student:
        # Constructor
        def __init__(self, name : str, age : int):
            self.name = name
            self.age = age
            self._course = 1

        # String representation (for print)
        # <__main__.lection12.<locals>.Student object at 0x0000018714FBC1A0>
        def __str__(self):
            return f"{self.name} {self.age}"

        def __repr__(self):
            return self.__str__()

        def __lt__(self, other):
            return self.age < other.age

        # Custom method
        def SayHello(self):
            return f"{self.name} says hello!"

    class Aspirant(Student):
        def __init__(self, name, age, grade, spec : str = "default"):
            Student.__init__(self, name, age)
            self._grade = grade
            self.__spec = spec
            self.__disciplines = []

        def GetCourse(self):
            return self._course

        def SayHello(self):
            super().SayHello()
            return f"Aspirant {self.name} says hello!"

        def AddDiscipline(self, name : str):
            self.__disciplines.append(name)

        def GetDisciplines(self):
            return self.__disciplines

        def DeleteDiscipline(self, name):
            self.__disciplines.remove(name)
        
        def __increaseGrade(self):
            self._grade *= 2

    class User:
        # Python does not support constructor overloading!
        def __init__(self, first_name : str = "Default first name", last_name : str = "Default last name"):
            # By default all class members are public
            # To make member protected use _ suffix
            # To make member private use __ suffix
            # Public section
            self.first_name = first_name
            self.last_name = last_name
            self.email = ""
            self.department = ""
            # Protected section
            # Private section
            self.__login = ""
            self.__password = ""

        def __str__(self):
            return f"{self.first_name} {self.last_name}"

        def get_login(self):
            return self.__login

        def get_password(self):
            return self.__password

        def set_login(self, value : str):
            self.__login = value

        def set_password(self, value : str):
            self.__password = value

        def greet_user(self):
            return f"Hello, {self.__str__()}"

    # No default arguments
    user_with_first_and_last_names = User("Alexander", "Chernenko")
    # В этом случае создается новый член класс __login, так как приватный имеет имя _User__login (name mangling)
    print(user_with_first_and_last_names.get_login())
    user_with_first_and_last_names._User__login = "1"
    user_with_first_and_last_names.__login = "1"
    print(user_with_first_and_last_names.get_login(), user_with_first_and_last_names.__login)
    # user_with_first_and_last_names.email = "example@gmail.com"
    # user_with_first_and_last_names.set_login("123")
    # print(user_with_first_and_last_names.get_login())

    # Default last name
    # user_with_default_last_name = User("Alexey")

    # With default arguments
    # user_with_default_first_and_last_names = User()

    # print(user_with_first_and_last_names)
    # print(user_with_first_and_last_names.greet_user())
    # print(user_with_default_last_name.first_name, user_with_default_last_name.last_name)
    # print(user_with_default_first_and_last_names.first_name, user_with_default_first_and_last_names.last_name)

    # s1 = Student("Alexander", 25)
    # s2 = Student("Michael", 24)
    # s3 = Student("Svetlana", 23)
    # students = [s1, s2, s3, Student("Nikolay", 25)]

    # for s in students:
    #     print(s)
    # print(sorted(students))
    # print(s1.name, s1.age)
    # print(s2)
    # print(s2.SayHello(), s1.SayHello())

    # s2.age = 33
    # print(s2)
    # s2.name = "Oleg"
    # print(s2)

    # print("List of methods/attributes of Student:\n", "\n".join(dir(s1)))

    # aspirant = Aspirant("Alexander", 25, 5000.0)

    # print("List of methods/attributes of Aspirant:\n", "\n".join(dir(aspirant)))

    # print(aspirant.GetCourse())

    # Throws because access to private method
    # aspirant.__increaseGrade()

    # Throws because access to private member
    # print(aspirant.__spec)
    # Please do not do so
    # print(aspirant._Aspirant__spec)

    # Use Student API
    # print(aspirant.SayHello())

    # aspirant.AddDiscipline("1")
    # aspirant.AddDiscipline("2")
    # aspirant.AddDiscipline("3")

    # aspirant.DeleteDiscipline("3")

    # print(aspirant.GetDisciplines())

    pass

