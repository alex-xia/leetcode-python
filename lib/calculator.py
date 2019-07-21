'''
Write a program that takes a single line of input, representing an arithmetic expression.  The expression will consist of numeric digits (0-9), the plus operator (+) and the multiplication operator (*).  The given expression will be a valid arithmetic expression (ie. "*2++" is not valid).

Your task is to evaluate the arithmetic expression, following the normal rules of operator precedence, and print the result without any leading or trailing whitespace.

The resulting numbers will fit in a normal integer.

Note: Solutions such as "eval()" in python are elegant, but not what we are looking for here.  Please evaluate the expressions with your own code :).

Example Input
20+2*3
Example Output
26
'''

# This is Python 2
import sys

def calc(s):
    nums = []
    muls = []
    num_str = ''
    for c in s:
        if c is '+':
            num = int(num_str)
            num_str = ''
            if len(muls) > 0:
                num = num * muls[0]
                del muls[0]
            nums.append(num)
        elif c is '*':
            num = int(num_str)
            num_str = ''
            if len(muls) == 0:
                muls.append(num)
            else:
                muls = [muls[0] * num]
        else:
            num_str += c
        print nums, muls
    num = int(num_str)
    if len(muls) > 0:
        num = num * muls[0]
    nums.append(num)
    return sum(nums)

print calc('20+2*3*2')