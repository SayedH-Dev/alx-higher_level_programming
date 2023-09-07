#!/usr/bin/python3
if __name__ == "__main__":
    import sys
    argv = sys.argv[1:]
    arguments = len(argv)
    if arguments == 0:
        print("0 arguments.")
    else:
        print("{} arguments:".format(arguments))
        for index, value enumerate(argv, start=1):
            print("{}: {}".format(index, value))
