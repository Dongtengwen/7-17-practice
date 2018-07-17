d={'a':1,'b':2,'c':3}
d_add={'d':4}
print('旧字典：')
for i in d:
    print('%s,%d'%(i,d[i]))
d.update(d_add)
print('新字典：')
for i in d:
    print('%s,%d'%(i,d[i]))

