s1='I,love,python'
s2='aabbccddee'
s3='ab2b3n5nn2n67mm4n2'
print(s1.split(',')[1])
print(s2.replace('dd','ff'))
print('n出现了%d次'%s3.count('n'))
dict_count={}
for i in s3:
    dict_count.setdefault(i,s3.count(i))
print(dict_count)
