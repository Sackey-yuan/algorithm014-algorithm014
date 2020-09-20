import time
import collections
import logging
import pickle
import itertools
import _thread
# import
import locust
import os
import sys


test_code = """
from Week_05.practice.testing import TestCode


class Solution:
    """"""
    pass


def main():
    test_case = [
                    ]
    tester = TestCode()
    tester.creat_function(Solution().minPathSum)
    tester.creat_test_case(test_case)
    # tester.start()
    # tester.del_log_cache()


if __name__ == "__main__":
    main()
"""

class Tasker(object):
    def __init__(self):
        self.times = {"firstTime": None, "nextTime": None, "list": []}
        self.task = None

    def next_time(self):
        return self.times["nextTime"]





class Memory:
    def __init__(self):
        pass

    def add(self):
        pass

    def check(self):
        pass

    def start(self):
        pass

    def renew(self):
        pass


class CodeM(Memory):

    def __init__(self):
        super().__init__()


class EnglishM(Memory):
    def __init__(self):
        super().__init__()


class TaskM(Memory):
    def __init__(self):
        super().__init__()


class TestCode:
    def __init__(self):
        self.testCase = []
        self.timeDb = []
        self.timeSum = 0
        self.timeAvg = 0
        self.samples = 0
        self.resultDb = []
        self.function = None
        self.error = 0
        self.errorCase = []
        self.dirName = ""
        self.fireName = __file__
        self.logsFile = time.strftime("%Y_%m_%d_%H.%M.%S_", time.localtime()) + "test.log"
        logging.basicConfig(filename=self.logsFile, level=logging.INFO)

    def add_case(self, test_case):
        if test_case:
            self.testCase.append(test_case)

    def creat_test_case(self, case_list):
        self.testCase = case_list

    def start(self, function=None, test_case=None):
        if function:
            self.function = function
        if test_case:
            self.creat_test_case(test_case)
        if not self.testCase:
            raise Exception("No testCase")
        if not self.function:
            raise Exception("No function")
        for case in self.testCase:
            start_time = time.time()
            # time.sleep(0.01)
            try:
                res = self.function(*case)
            except Exception as es:
                logging.exception("\nCase:\n" + "\n" + str(case) + str(es))
                # print(str(es), "error class:", es.__doc__, "\nerror str:", es.__str__(), "test Case is:", case)
                self.error += 1
                # self.errorCase.append("\nCase:\n" + str(case)+ "\nerror class:" + es.__doc__ + es.__str__())
            else:
                self.timeDb.append((time.time() - start_time)*1000)
                self.resultDb.append((case, res))
        self.print_time()

    def print_time(self):
        c = collections.Counter(self.timeDb)
        self.samples = len(self.testCase)
        self.timeSum = sum(self.timeDb)
        self.timeAvg = self.timeSum / self.samples
        print("\n timeSum:%fms" % self.timeSum)
        print("\nsamples num:", self.samples)
        print("\n timeAvg:%fms" % self.timeAvg)
        print("\ntime item:\n", self.timeDb)
        print("Counter:")
        for i in c.keys():
            print(f"{i}:{c[i]}")
        print("\nError num:", self.error)
        print("resultDb:")
        for i in self.resultDb:
            print(f"testCase:\n{i[0]}\nresult:\n{i[1]}")
        with open(self.logsFile, "r") as logs:
            print("\nError case:", self.logsFile)
            for error in logs:
                print(error)

    def creat_function(self, function):
        self.function = function

    def del_log_cache(self):
        print(self.fireName)
        print(sys.path)
        self.dirName = sys.path[0]
        for file in search_file(self.dirName, ".log"):
            try:
                os.remove(f"{file}")
            except PermissionError as es:
                logging.exception(f"\ndel file:\n\\{file}")
            else:
                print(f"Successfully deleted \\{file}")


def search_file(path, file_ext):
    dir_list = [path]
    n = len(file_ext)
    file_list = []
    while dir_list:
        dir0 = dir_list.pop()
        if os.path.isdir(dir0):
            for dir1 in os.listdir(dir0):
                if os.path.isdir(dir1):
                    dir_list.append(f"{dir0}\\{dir1}")
                else:
                    # print(dir1, dir1[-n:], file_ext)
                    if dir1[-n:] == file_ext:
                        file_list.append(f"{dir0}\\{dir1}")
    return file_list


def test_function(y, x):
    for i in range(x):
        print(i)
    for j in y:
        print(j)
    print(x, y)


def mk_practice_py_file(practice_name):
    dir0 = sys.path[0]
    file_name = practice_name
    # file_name.replace('-', '_')
    file_name = file_name.replace("-", "_")
    # for i in file_name:
    #     print(i, i == '-')
    print(file_name)
    file = open(f"{dir0}\\{file_name}.py", "a")
    file.writelines(test_code)


def main():
    st = TestCode()
    st.creat_function(test_function)
    caseDB = [([1,2,3],10 )#, (3, "qwe"), (1, [1, 2]), (1, [2])
              ]
    st.creat_test_case(caseDB)
    st.start()


if __name__ == "__main__":
    print('decode-ways'.replace('-', '_'))
    TestCode().del_log_cache()