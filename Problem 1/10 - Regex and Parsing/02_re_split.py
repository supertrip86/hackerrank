# -*- coding: utf-8 -*-
"""
Re.split()

"""

# found on Tutorial: https://www.datacamp.com/community/tutorials/python-regular-expression-tutorial
# \D <---> Uppercase D. Matches any character that is not a decimal digit.

regex_pattern = r"\D"	# Do not delete 'r'.

import re
print("\n".join(re.split(regex_pattern, input())))