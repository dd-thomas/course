import os

def lection8():
    """
    files
    """
    # r - read
    # a - append
    # w - write
    # x - create
    # t - text
    # b - binary
    # c:\\python\\123.txt
    # /home/user/123.txt
    # # Valid path
    # path = "e:\\temp\\APP_HOST.InfraServer_super_new.log"
    # # Invalid path generates FileNotFoundError
    # # path = "124.txt"
    # f = open(path, "rt", encoding="utf-8")
    # # Read full content of the file. May be slow
    # # for l in f.readlines():
    # #     print(l)
    # print(f.read(100500))
    # f.close()
    # # \n LF Linux
    # # \r\n CR LF Windows

    print(os.getcwd())

    # Write file
    f = open("123.txt", "at", encoding="utf-8")
    # f = open("e:/work/devproject_hg/python/course/tests/123.txt", "at", encoding="utf-8")
    f.write("Hello")
    f.close()

    # f = open("e:/work/devproject_hg/python/course/tests/123.txt", "rt")
    f = open("123.txt", "rt")
    print(f.read())

    # with operator
    print(os.getcwd())
    
