from collections import *
import logging
import pickle
import json
from openpyxl.chart import LineChart
import openpyxl


# from itertools import *
def print_function(function):
    print("++++"*10)
    functions = {}
    others = []
    for i in function.__dict__:
        # functions.append(str(i)+":"+str(function.__dict__[i].__doc__))
        # functions.append(function.__dict__[i].__doc__)
        if "_" != i[0]:
            if function.__dict__[i].__doc__:
                functions[i] = function.__dict__[i].__doc__
        else:
            others.append(i)
    print("functionName:", function.__name__)
    print("function is :", function.__class__)
    print("function doc :", function.__doc__)
    try:
        print("function in the module:", function.__module__)
    except Exception as es:
        print(es)
    print("function have :", "".join("\n" + key for key in functions.keys()),"\n" , "\n*************\n".join([""] + list(j+":\n    "+functions[j] for j in functions.keys())))
    print("function have others :\n", "\n".join(others))


def print_object(ob):
    print("++++"*10)
    print(ob.__dir__())
    # for i in ob.__dir__:
    #     functions.append(i+":"+ob.__dir__[i].__doc__)
    #     functions.append(ob.__dir__[i].__doc__)
    #     # if "_" not in i:
        #     if function.__dict__[i].__doc__:
        #         functions.append(i+":"+function.__dict__[i].__doc__)
    # print("object name:", ob.__name__)
    print("object is :", ob.__class__)
    print("object doc :", ob.__doc__)
    print("object have :\n", ob.__dir__())
    for i in ob.__dir__():
        print(i)
        # print(i, eval("ob.%s()" % i))
        try:
            print(i,eval("ob.%s()"%i))
        except Exception as es:
            print("error class:",es.__doc__, "\nerror str:", es.__str__())


def print_item(item):
    try:
        print(item.__str__())
        print("begin:", item.__name__)
    except Exception as es:
        print("begin:", repr(item))
        print(es.__str__())

    if type(item) in (int,str,list,dict):
        print_object(item)
    else:
        try:
            for i in item:
                if type(i) == str:
                    print(i)
                else:
                    try:
                        print_function(i)
                    except Exception as es:
                        print(es.__str__())
        except Exception as es:
            print(es.__str__())
            print_function(item)


def test_openpyxl():
    wb = openpyxl.Workbook()
    cs0 = wb.create_sheet()


if __name__ == "__main__":
    # d = globals().copy()
    # at = object()
    # aa = {1: 2}
    # a = 12.12
    # print(f"{aa}:{a}")
    # print_item(openpyxl.chart)
    import sys
    print(int(1e9), float("inf"), sys.maxsize,sys.float_info.max)