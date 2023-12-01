import random
def myshuffle(l):
    random.shuffle(l)
    return l
n=[1,2,3,'kdc',10.5,11.3,'cusp']
x=myshuffle(n)
print('shuffle list::',x)
