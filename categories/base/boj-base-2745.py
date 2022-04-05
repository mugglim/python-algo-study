from typing import List

BASE_DIC = {str(k):v for k,v in [[i,i] if i < 10 else [chr(65+i-10),i] for i in range(36)]}

def convertToDecimal(arr:List[str], base:int):
    return sum([BASE_DIC[v] * (base ** i) for i,v in enumerate(arr[::-1])])

n,b = input().split()
print(convertToDecimal(n,int(b)))