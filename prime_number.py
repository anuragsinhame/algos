def check_prime(n):
    i = 2
    if(n>2):
        while(i != (n//2)):
            if(n%i==0):
                return False
            else:
                i+=1
    elif(n==2):
        return True
    else:
        return False
    return True

for i in range(0,100):
    if check_prime(i):
        print(f"{i} is a prime number")
