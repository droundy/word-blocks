import numpy as np

alldigits = '0123456789'

def has_all_digits(x):
    return all(map(lambda d: d in x, alldigits))

for i in range(999):
    for j in range(999):
        result = i+j
        wehave = str(i)+str(j)+str(result)
        if len(str(result)) <= 4 and has_all_digits(wehave) and np.sqrt(i) == int(np.sqrt(i)):
            print i,j,result, np.sqrt(i)

