# a simple parser for python. use get_number() and get_word() to read
def parser():
    while 1:
        data = list(input().split(' '))
        for number in data:
            if len(number) > 0:
                yield(number)   

input_parser = parser()

def get_word():
    global input_parser
    return next(input_parser)

def get_number():
    data = get_word()
    try:
        return int(data)
    except ValueError:
        return float(data)

from collections import defaultdict

a = get_word()
b = get_word()

where_is = defaultdict(list)
por_onde_comecar = defaultdict(lambda: 0)

for i, char in enumerate(a):
    where_is[char].append(i)

else:
    k = 1
    where_i_am = -1
    for l in b:
        if len(where_is[l])==0:
            k = -1
            break
        
        if where_is[l][-1] <= where_i_am:
            k+=1
            where_i_am = -1
            por_onde_comecar.clear()
            
        for j in where_is[l][por_onde_comecar[l] : ]:
            if j > where_i_am:
                where_i_am = j
                break
            por_onde_comecar[l] += 1
    print(k)