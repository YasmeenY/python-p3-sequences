#!/usr/bin/env python3

def print_fibonacci(length):
    fib_list = list()
    n1,n2 = 0,1
    count = 0
    while (count < length):
        fib_list.append(n1)
        nth = n1 + n2
        n1 = n2
        n2 = nth
        count += 1
    print(fib_list)