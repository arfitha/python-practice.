lower=100
upper=2000
for num in range(lower,upper+1):
    order=len(str(num))
    s=0
    temp=num
    while temp>0:
        digit=temp%10 #gives the ones digit no.
        s+=digit**order
        temp//=10
    if num==s:
        print(num)