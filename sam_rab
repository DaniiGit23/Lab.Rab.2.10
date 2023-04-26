#!/usr/bin/env python3
# # -*- coding: utf-8 -*-

def sum_abs_after_negative(*args):
    for i, arg in enumerate(args):
        # Определяется самый первый отрицательный аргумент arg
        # Также индекс самого первого отрицательного аргумента i
        if arg < 0:
            return sum([abs(arg) for arg in args[i+1:]])
    return None


if __name__ == "__main__":
    print(sum_abs_after_negative(1, 4, -5, 3, 5, -3, 2, -1))
    print(sum_abs_after_negative())
