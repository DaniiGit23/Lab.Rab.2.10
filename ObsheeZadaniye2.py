#!/usr/bin/env python3
# # -*- coding: utf-8 -*-

def harmonic_zn(*args):
    return len(args) / sum([1 / i for i in args])

if __name__ == "__main__":
    print(harmonic_zn(2, 5, 1))
