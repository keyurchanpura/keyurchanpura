def keyur(l):
    for i in l:
        if(l.count(i)>1):
            l.remove(i)
    return l
n=[1,1,1,2,3,'kdc',10.5,10.5,11.3,'cusp']
x=keyur(n)
print('shuffle list::',x)
