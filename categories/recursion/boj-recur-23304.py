import sys
sys.setrecursionlimit(100001)

def isPalindrom(s): return s == s[::-1]

def isAkarakaPalindrom(s):
    if len(s) == 1: return True

    if not isPalindrom(s): return False

    mid = len(s) // 2

    if not isAkarakaPalindrom(s[:mid]): return False
    if not isAkarakaPalindrom(s[mid:] if len(s) % 2 == 0 else s[mid+1:]): return False

    return True

s = input()
result = isAkarakaPalindrom(s)
print("AKARAKA" if result else "IPSELENTI")

