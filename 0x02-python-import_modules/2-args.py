#!/usr/bin/python3
if __name__ == "__main__":
    import sys
    argv = sys.argv[1:]
    arguments = len(argv)
    if arguments == 0:
        print("0 arguments.")
    elif arguments == 1:
        print("1 argument:")
    else:
        print("{} arguments:".format(arguments))
    if arguments > 0:
        for index, value in enumerate(argv, start=1):
            print("{}: {}".format(index, value))
