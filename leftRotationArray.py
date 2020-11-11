def rotleft(a,d):
    temp=[]
    temp.extend(a[0:d])
    del a[0:d]
    a.extend(temp)
    return a
print(rotleft([1,2,3,4,5],4))