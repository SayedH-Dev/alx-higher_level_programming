#!/usr/bin/python3
if __name__ == "__main__":
    import marshal
    with open("hidden_4.pyc", "rb") as pyc:
        compiled = marshal.load(pyc)
    names = (name for name in dir(compiled) if not name.startswith("__"))
    for name in sorted(names):
        print(name)
