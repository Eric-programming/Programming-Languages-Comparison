from datetime import datetime
from datetime import date
from datetime import time
# python3 python.basics.py
print("hello")

# python functions
python_global_var = 9


def python_functions():
    python_global_var = 10
    print("inside func", python_global_var)


print("outside func", python_global_var)
python_functions()

# python *args and params of functions


def _arg_function_(*args):
    for item in args:
        print(item)


_arg_function_(1, 2, 3, 4, 5, 6)


def _params_function_(x, y, *nums):
    print("pass params without order. x is ", x, " y is ", y)


_params_function_(y=9, x=10)

# conditions statement
small = 0
big = 0
if(small < big):
    print("Correct")
elif(small == big):
    print("They are all equal")
else:
    print("incorrect")

# while loop
whileloop_var = 0
while (whileloop_var < 10):
    print(whileloop_var)
    whileloop_var += 1

# for loop
arr = ["A", "B", "C", "D"]
for target_list in arr:
    print(target_list)

# for loop with index
for index, val in enumerate(arr):
    print("Index is ", index, " and value is ", val)

# class and inheritance


class Class1():
    def main(self):
        return "This is Class1"


class Class2(Class1):
    def mainClass2(self):
        c = Class1()
        print(c.main())
        print("this is Class2")


c = Class2()
c.mainClass2()

# Python Time


todaysDate = date.today()
print('todaysDate: ', todaysDate)
gettodayday = todaysDate.day
print('gettodayday: ', gettodayday)
timeRightNow = datetime.now()
print('timeRightNow: ', timeRightNow)
