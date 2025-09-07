#!/usr/bin/python3
def raise_exception():
    try:
        raise TypeError("operation applied is the wrong type")
    except Exception as e:
        print("Exception has been raised")
