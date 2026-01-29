n=int(input("Enter a number: "))
if n<=1:
    print("Not a prime number")
else:
    i=2
    prime=True
    while i*i<=n:
        if n%i==0:
            prime=False
            break
        i+=1
    if prime:
        print("Prime number")
    else:
        print("Not a prime number")
