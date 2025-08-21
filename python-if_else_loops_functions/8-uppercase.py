#!/usr/bin/python3
def uppercase(s):
    for i in s:
        print("{}".format(chr(ord(i) - 32) if 'a' <= i <= 'z' else i
        ), end="")
    print()
