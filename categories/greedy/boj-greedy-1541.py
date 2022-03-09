import re
import sys

input = lambda:sys.stdin.readline().rstrip()
expression = input()

def map_exp(i,exp):
    tot = sum(list(map(int,re.split('[+]',exp))))
    return tot if i == 0 else -tot

def sol(expression):
    return sum([map_exp(i,exp)for i, exp in enumerate(re.split('-',expression))])

print(sol(expression))

