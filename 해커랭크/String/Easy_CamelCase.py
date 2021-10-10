import re
def minimumNumber(n, password):
    cnt = 0

    specialCharList = '[!|@|#|$|%|^|&|*|(|)|+|-]'

    cnt += 1 if not re.search("[0-9]",password) else 0
    cnt += 1 if not re.search("[a-z]",password) else 0
    cnt += 1 if not re.search("[A-Z]",password) else 0
    cnt += 1 if not re.search(f"{specialCharList}",password) else 0



    return cnt if len(password) + cnt >= 6 else 6 - len(password)


