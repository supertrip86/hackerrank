# -*- coding: utf-8 -*-
"""
Polynomials

"""

import numpy

coef = list(map(float, input().split()))

x = int(input())

print(numpy.polyval(coef, x))