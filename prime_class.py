class prime():
    def isprime(self,num):
        for i in range(2,num):
            if num%i==0:
                return False
        return True
if __name__ == "__main__":
    obj=prime()
    num =int(input("enter a number "))
    if obj.isprime(num):
        print(num,"is prime number")
    else:
        print(num,"is not prime number")