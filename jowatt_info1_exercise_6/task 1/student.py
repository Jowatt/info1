from module import *
from moduleElement import *

class Student(object):

    def __init__(self, name):
        pass
        ######## CODE MISSING HERE

        self.name = name
        self.modules = []
        self.grades = {}


    def add_module(self,title):
        pass
        ######## CODE MISSING HERE

        self.modules.append(title.get_title())
        self.grades[title.get_title()] = title.get_grade()

    def get_list_modules(self):
        pass
        ######## CODE MISSING HERE

        for m in self.modules:
            print(m)

    def get_grades(self):
        pass
        ######## CODE MISSING HERE

        for f in self.grades:
            print(f,':', self.grades[f])


### test cases ###

me = Student("FirstName LastName")
me.add_module(info1)
me.get_list_modules()
# expected output:
# Modules of Student FirstName LastName:
#	Info 1

me.get_grades()
# expected output:
# Grades of Student FirstName LastName:
#	Info 1: 6
