def str_cmp (string1, string2):
    if len(string1) == len(string2):
        return 1
    elif len(string1) > len(string2):
        if (string2 == 'learn'):
            return 3
        else:
            return 2
    else:
        return 0


a='3 2 1 4'
b= '5 1 3 7'
print(str_cmp (a, b))
c='3 2 1'
print(str_cmp(a, c))
d='learn'
print(str_cmp(a, d))