#if no. of zeros is greater than (size/2) ,then it is a sparse mtrix
a=[
    [4,0,0],
    [0,5,0],
    [0,0,6]
]
count=0
rows=len(a)
cols=len(a[0])
size=rows*cols
for i in range(0,rows):
    for j in range(0,cols):
        if a[i][j]==0:
            count=count+1
if (count>(size/2)):
    print("It is a sparse matrix.")
else:
    print("Not a sparse matrix.")