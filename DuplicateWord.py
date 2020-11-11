s="What is ur name?How r u?What r u doing?What is ur hobby?"
l=s.split()
k=[]
for i in l:
    if (s.count(i)>1 and ((i not in k) or s.count(i)==1)):
        k.append(i)
print(' '.join(k))