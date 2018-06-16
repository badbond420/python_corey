import time
from functools import wraps
import logging

def my_decorater(func):
    def warpper(*args,**kwargs):
        print("begining")
        res = func(*args,**kwargs)
        return res *3
    return warpper


class decorater_class:
    def __init__(self,func):
        self.func = func

    def __call__(self,*args, **kwargs):
        res= self.func(*args, **kwargs)
        return res * 3

@decorater_class
def print_hello():
    return "hello"

# print(print_hello())

#intermediate

def logger(func):
    logging.basicConfig(filename="decorator.log",level=logging.DEBUG)
    @wraps(func)
    def wrapper(*args, **kwargs):
        logging.info('Ran with args: {}, and kwargs: {}'.format(args, kwargs))
        return func(*args,**kwargs)
    return wrapper

def timer(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        t =time.time()
        res = func(*args,**kwargs)
        print("{} function took {} time to finish".format(func.__name__,t - time.time()))
        return res
    return wrapper

@timer
@logger
def display_info(name, age):
    time.sleep(1)
    print('display_info ran with arguments ({}, {})'.format(name, age))

# display_info("bibek",26)

# decorator with args
def decorater_with_arg(arg):
    def outer(func):
        def wrapper(*args, **kwargs):
            print(arg)
            return func(*args, **kwargs)
        return wrapper
    return outer

@decorater_with_arg("lol")
def say_hi():
    print("Hi")

say_hi()