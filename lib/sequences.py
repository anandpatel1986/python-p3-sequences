#!/usr/bin/env python3


def print_fibonacci(length):
    fib_list = list()
    for i in range(0, length):
        if i == 0:
            fib_list.append(i)
        elif i == 1:
            fib_list.append(i)
        else:
            fib_list.append(fib_list[i - 1] + fib_list[i - 2])
    print(fib_list)
