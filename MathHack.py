#! /usr/bin/env python3

import math # for trig func. ,  degrees(),radians() && gcd()
import sys #for cli args

def err(): #function for input error 
    print("Invalid Input, Sorry.")

def trcalc(func,angle): #function for TCAL
    if func == "sin":
        print('Result =',round((math.sin(angle)),4))
    elif func == "cos":
        print('Result =',round(math.cos(angle),4))
    elif func == "tan":
        print('Result =',round(math.tan(angle),4))
    elif func == "cosec":
        print('Result =',round(1/(math.sin(angle)),4))
    elif func == "sec":
        print('Result =',round(1/(math.cos(angle)),4))
    elif func == "cot":
        print('Result =',round(1/(math.tan(angle)),4))
    else: err()

def factorial(x): 
    f = 1
    i = x
    while i >= 1:
        f = f*i
        i -= 1
    print('Factorial of ',x,' = ',"{:e}".format(f))

frequency = len(sys.argv)
arguments = sys.argv 

#-----Begin 'Main'-----

if frequency >= 3:

    choice = arguments[1]

    if choice ==  "cal" and frequency >= 5:
      num1, op, num2 = float(arguments[2]), arguments[3] , float(arguments[4])

      if op == '+':
          print("Result = ",num1+num2)
      elif op == '-':
          print("Result = ",num1-num2)
      elif op == 'x' or op == '*':
          print("Result = ",num1*num2)
      elif op == '/':
          print("Result = ",num1/num2)
      elif op == '^':
          print("Result = ",num1**num2)
      elif op == '%':
          print("Result  = ",num1%num2)
      elif op == '|' or op == '\\' :
          print("Result = ",(num1)**(1/num2))
      else:
          err() #invokes error message

    elif choice == 'fact':
        num = int(arguments[2])
        if num >= 2:
            print("Factors of ",num," are: ","1, ", end = "") # 1 is factor of every num
            factor = 2 # sets counter to begin @ 2
            while factor <= ((num)/2):
                if num%factor == 0:
                    print(factor,end=", ")
                factor += 1
            print(num) # num is factor of itself
        else:
            err()
    elif choice == 'avg' and frequency  >= 4:
        import statistics
        lst =[]
        count = 0;
        for argument in arguments :
            if count >= 2:
                lst.append(int(argument))
            count += 1
        print('The average is',statistics.mean(lst))

    elif choice == 'prime':
        flag = False # flag is false by default
        n = int(arguments[2])
        i = 2
        while i <= (n**0.5):
            if (n%i) == 0:
                flag = True
                break
            i += 1
        if n == 1:
            print('1 is neither prime nor composite')
        elif flag == False :
            print(n,' is a prime number.')
        elif flag == True :
            print(n,' is not a prime number.')

    elif choice == 'pmfact': #prints only unique prime factors
        num = int(arguments[2])
        print('Prime factors of ',num,' are : ', end='')
        i = 2
        while i <= num:
            if num%i == 0:
                isPrime = 1
                j = 2
                while j <= (i**(0.5)): 
                    if i%j == 0:
                        isPrime = 0
                        break
                    j += 1
                if isPrime == 1:
                    print(i,end =' ')
            i += 1
        print('')

    elif choice == 'tab':
        num = float(arguments[2])
        for i in range (2,20):
            print(num,' x ',i,' = ',round((num*i),4))
            
            
    elif choice == 'fctrl':
        num = int(arguments[2])
        factorial(num)

    elif choice == 'eq' and  frequency >= 5:
        a = float(arguments[2])
        b = float(arguments[3])
        c = float(arguments[4])

        dscrmnt = (b**2) - (4*a*c)
        print('Discriminant evaluates to ',dscrmnt)

        if dscrmnt > 0:
            r1= (-b + (dscrmnt**0.5))/ (2*a);
            r2= (-b - (dscrmnt**0.5))/ (2*a);
            print('Root 1 = ',round(r1,4))
            print('Root 1 = ',round(r2,4))

        elif dscrmnt == 0:
            r = -b/(2*a)
            print('Root 1 = Root 2 = ',round(r,4))

        else:
            print('Roots are not real.')
            real = -b/(2*a)
            ima = ((-dscrmnt)**0.5) / (2*a)
            print('Root 1 = ',round(real,4),'+',round(ima,4),'i')
            print('Root 2 = ',round(real,4),'-',round(ima,4),'i')

    elif choice == 'hcf' and frequency >= 4:
        a = int(arguments[2])
        b = int(arguments[3])
        print('HCF of ',a,' and ',b,' = ',math.gcd(a,b)) #uses gcd() from math module

    elif choice == 'smp' and frequency >= 4:
        nu = int(arguments[2])
        den = int(arguments[3])
        gcd = math.gcd(nu,den)
        print('Simplified fraction is',int(nu/gcd),'/',int(den/gcd))

    elif choice == 'tcal' and frequency >= 5:
        unit = arguments[2]
        func = arguments[3]

        if unit == 'r' :
            rad = float(arguments[4])
            trcalc(func,rad)
        elif unit == 'd' :
             deg = float(arguments[4])
             rad = math.radians(deg) # converts degrees to rad
             trcalc(func,rad)
        else:
            err() 

    elif choice == 'ttab' and frequency >=  4:
        what = arguments[2]

        if what == 'd' or what == 'D':
            dig = float(arguments[3])
            this = math.radians(dig) # converts to radians

            print('Angle in radian =',round(this,4))
            print('\nSin of',dig,'=',round(math.sin(this),4))
            print('Cos of',dig,'=',round(math.cos(this),4))
            print('Tan of',dig,'=',round(math.tan(this),4))
            print('Cosec of',dig,'=',round(1/(math.sin(this)),4))
            print('Sec of',dig,'=',round(1/(math.cos(this)),4))
            print('Cot of',dig,'=',round(1/(math.tan(this)),4))

        elif what == 'r' or what == 'R' :
            this = float(arguments[3])
            dig = math.degrees(this) # converts to degrees

            print('Angle in degree =',round(dig,4))
            print('\nSin of',this,'=',round(math.sin(this),4))
            print('Cos of',this,'=',round(math.cos(this),4))
            print('Tan of',this,'=',round(math.tan(this),4))
            print('Cosec of',this,'=',round(1/(math.sin(this)),4))
            print('Sec of',this,'=',round(1/(math.cos(this)),4))
            print('Cot of',this,'=',round(1/(math.tan(this)),4))

        else:
            err()

    else :
        print("Insufficient or Incorrect Input.")
else :
    print("Too few arguments.")

#---------End 'Main'----------

