#!/usr/bin/env python3
# # -*- coding: utf-8 -*-

def sum_args_after_max(*args):
    if args:
        # Принимает максимальное значения среди всех аргументов
        max_value = max(args)
        # Принимает индекс максимального значения среди всех аргументов
        max_index = args.index(max_value)
        return sum(args[max_index+1:])
    return None


if __name__ == "__main__":
    print(sum_args_after_max(1, 2, 3, 4, 5, 6, 7))
    print(sum_args_after_max(11, 7, 13, 4, 2, 3))
    print(sum_args_after_max())
