#!/usr/bin/python3
import py_compile
import os
pyfile = os.environ.get('PYFILE')
if pyfile:
    print(f"Compiling {pyfile} ...")
    py_compile.compile(pyfile, cfile=pyfile + 'c')
