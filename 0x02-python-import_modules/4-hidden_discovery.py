#!/usr/bin/python3
if __name__ == "__main__":
    import py_compile
    import imp
    hidden_4 = "hidden_4.pyc"
    py_compile.compile(hidden_4)
    compiled = imp.load_compiled("hidden_4", hidden_4)
    names = (name for name in dir(compiled) if not name.startswith("__"))
    for name in sorted(names):
        print(name)
