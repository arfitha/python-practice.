def primeno(num):
    if num>1:
        for i in range(2,num):
            if (num%i) ==0:
                print(num,"is not a prime no.")
                break
        else:
            print(num,"is a prime no.")

num=int(input("Enter a no:\n"))
if num>0:
    primeno(num)
else:
    print("Enter a positive no")