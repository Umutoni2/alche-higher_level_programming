#!/usr/bin/python3
def raise_exception_msg(message=""):
    raise NameError(message)
    try:
        raise NameError("C is fun")
    except Exception as e:
        print("Python is cool")
