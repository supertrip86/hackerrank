# -*- coding: utf-8 -*-
"""
Designer Door Mat

"""

if __name__ == '__main__':
    values = input().split()

    N = int(values[0])

    M = int(values[1])

    for i in range(1, N, 2):
        print(( (i) * ".|.").center(M, "-"))

    print("WELCOME".center(M, "-"))

    for i in range(1, N, 2):
        print(( (N - i - 1) * ".|.").center(M, "-"))