def lection10():
    """
    dictionary and tuple
    """
    t = ("banana", "apple", "cherry", "cherry") # ordered, unchangable, allow dupplicates
    # l = ["banana", "apple", "cherry"]
    # l.append("pear")
    # l.append("pear")
    # print(f"tuple={t} {type(t)} list={l} {type(l)}")    
    # tuple
    # print(len(t))
    # set
    # change elements (WARNING)
    # changed = list(t)
    # changed[-1] = "pear"
    # t = tuple(changed)
    # print(f"tuple={t} {type(t)}")
    # print(f"list={changed} {type(changed)}")

    # dictionary
    # JSON (https://jsonformatter.curiousconcept.com/)
    # python 3.7+ dictionaries are ordered
    # d = {
    #     "brand": "Ford",
    #     "year": 1964,
    #     "model": "Mustang",
    #     "owner": "Alex"
    #     }
    # print(d)

    # keys
    # print(d.keys())

    # values
    # print(d.values())

    # items
    # print(d.items())
    # for k, v in d.items():
    #     print(f"{k}: {v}")

    # keys iteration
    # for k in d.keys():
    #     print(k)

    # values iteration
    # for v in d.values():
    #     print(v)

    # dupplicates
    # d = {
    #     "brand": "Ford",
    #     "model": "Mustang",
    #     "year": 1964,
    #     "year": 2010
    #     }
    # print(d)

    # update
    # d["year"] = 1964

    # add
    # d["some_key"] = "123"

    # length
    # print(len(d), len(d.keys()), len(d.values()), len(d.items()))

    # print(d)

    # dict consturctor
    # **kwargs overload
    # d = dict(name = "Alexander", age = 22, country = "Russia")
    # print(d, type(d))

    # access items
    # print(d["year"])
    # KeyError
    # print(d["not_exist"])
    # print(d.get("year"))
    # print(d.get("not_exist"))
    # print(d.get("not_exist", "not found"))
    # print("not_exist" in d.keys())

    # Methods
    # clear
    # copy
    # fromkeys
    # get
    # pop
    # popitem
    # update

    # copy
    # d = {
    #     "brand": "Ford",
    #     "model": "Mustang",
    #     "year": 1964
    # }
    # get only reference, not copy!
    # copy = d
    # d.update(new_key = 1)
    # print(copy, d)

    # copy() call
    # copy = d.copy()
    # d.update(new_key = 1)
    # print(copy, d)

    # dict() constructor
    # copy = dict(d)
    # d.update(new_key = 1)
    # print(copy, d)

