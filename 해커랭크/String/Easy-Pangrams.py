def pangrams(s):
    a = [0 for _ in range(26)]

    for ch in s:
        if ch.isalpha():
            if ch.isupper(): a[ord(ch) - 65] += 1
            else: a[ord(ch) - 97] += 1


    return 'pangram' if all(a) else 'not pangram'
