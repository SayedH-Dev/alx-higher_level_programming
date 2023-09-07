#!/usr/bin/python3
if __name__ == "__main__":
    import py_compile
    import imp
    py_compile.compile("hidden_4.py")
    compiled = imp.load_compiled("hidden_4", "hidden_4.pyc")
    names = (name for name in dir(compiled) if not name.startswitch("__"))
    for name in sorted(names):
        print(name)
