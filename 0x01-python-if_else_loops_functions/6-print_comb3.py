#!/usr/bin/python3
for first_num in range(9):
    for second_num in range(first_num + 1, 10):
        if first_num == 8 and second_num == 9:
            print("89")
        else:
            print("{:02d}, ".format(first_num * 10 + second_num), end='')
