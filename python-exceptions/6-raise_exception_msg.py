#!/usr/bin/python3    
def raise_exception_msg(message=""):
    try:
        raise NameError("C is fun")
    except Exception as e:
        print(e)
