class Fraction():
    def __init__(self) -> None:
        pass
    def fraction(self,a,b):
        n = 0
        if a > b:
            n = b
        else:
            n = a


        while n > 1:
            if a % n == 0 and b % n == 0:
                try:
                    a = a / n
                    b = b / n
                except ZeroDivisionError:
                    print("don't give zero as input")
                finally:
                    print("The try except is completed")
            n -= 1

        print(str(int(a)),"/",str(int(b)))

    def fractAdd(self,a,b,c,d):
        x = 0 
        y = 0
        gcd = 0

        x = (a*d) + (b*c) #numerator
        y = b * d

        i = 1
        while i<=x and i <=y:
            if x % i == 0 and y % i == 0:
                gcd = i
            i = 1 + i
        print("The added fraction is ",int(x/gcd), "/", int(y/gcd))  
    #fractMultiplication
    def fractMultiplication(self,a,b,c,d):
        x = 0 
        y = 0
        gcd = 0

        x = (a*c)   #numerator
        y = (b*d) # denominator
        self.fraction(x,y)

if __name__ == "__main__":
    fract1 = Fraction()
    iplist = input().split()
    arithmeticOpration = input("enter + or * or none fraction division : ")
    if len(iplist) == 2 and arithmeticOpration == "":
        a = int(iplist[0])
        b = int(iplist[1])
        fract1.fraction(a,b)
    elif len(iplist) == 4 and arithmeticOpration == "+":
        a,b,c,d = int(iplist[0]),int(iplist[1]),int(iplist[2]),int(iplist[3])
        fract1.fractAdd(a,b,c,d)
    elif len(iplist) == 4 and arithmeticOpration == "*":
        a,b,c,d = int(iplist[0]),int(iplist[1]),int(iplist[2]),int(iplist[3])
        fract1.fractMultiplication(a,b,c,d)
    else:
        print("Thank you")
    

    
