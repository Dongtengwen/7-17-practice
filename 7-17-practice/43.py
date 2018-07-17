for i in range(2,100):
    for j in range(2,i+1):
        if j==i:
            print('%d'%i,end=',')
        if i%j==0:
            break
print()
