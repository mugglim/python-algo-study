import re
s = input()

if 'A' in s:
    print(re.sub('[B|C|D|F]','A',s))
else:
    if 'B' in s:
        print(re.sub('[C|D|F]', 'B', s))
    else:
        if 'C' in s:
            print(re.sub('[D|F]', 'C', s))
        else:
            print(re.sub('\w', 'A', s))
