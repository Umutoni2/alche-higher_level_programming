#!/usr/bin/python3    
def raise_exception():
    try:
        raise_exception()
    except Exception as e:
         print("Exception raised",e)
