#MathHack.py --> v2.1

#---- Begin Functions & Modules----
import math # for trig func. && degrees(),radians() && gcd()
def err(): #function for input error 
    print("\nInvalid Input, Sorry.")
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
#---- End Functions & Modules----
    
#-----Begin 'Main'-----
print("\nMathHack v2.1 \n\nCAL, FACT, AVG, PRIME, PMFACT, TAB, FCTRL, EQ, HCF, SMP, TCAL, TTAB") #INTRO TEXT (not looped)

while True: 
    print("\n-------------------------\n") #separator between iterations of loop
    choice = input("Choose Function : ")

# Body Of If/Elif Statements 

    if choice == "CAL" or choice == "cal":
      print("+  -  x  /  ^  % | are valid operations.\nInput Expression : ",end="")
      num1, op, num2 = input().split() #split() enable mutiple inputs in one line, split by SPACE
      num1 = float(num1) # converts num from str to float
      num2 = float(num2)

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
          num1 = int(num1) # modulo division can be done only on integers
          num2 = int(num2)
          print(num1,"%",num2," = ",num1%num2)
      elif op == '|':
          print("Result = ",(num1)**(1/num2))
      else:
          err() #invokes error message

    elif choice == 'FACT' or choice == 'fact':
        num = int(input("\nInput whole number : "))
        print("Factors of ",num," are: ","1, ", end="") # 1 is factor of every num
        factor = 2 # sets counter to begin @ 2
        while factor <= ((num)/2):
            if num%factor == 0:
                print(factor,end=", ")
            factor += 1
        print(num) # num is factor of itself

    elif choice == 'AVG' or choice == 'avg':
        import statistics # for average 
        lst = [] #creates empty list to store numbers in
        n = int(input('\nEnter number of values to calculate avg of : '))
        print('\n') 
        for i in range(1,n+1):
                print('Enter number ',i,' : ',end='')
                ele=float(input())
                lst.append(ele) # adds 'ele' to the list 
        avg = statistics.mean(lst) #calculates avg of list
        print('\nThe average is',avg)

    elif choice == 'PRIME' or choice == 'prime':
        flag = False # flag is false by default
        n = int(input('\nEnter whole number to check : '))
        i = 2
        while i <= (n**0.5):
            if (n%i) == 0:
                flag = True # flag made true if factor foud for sqrt(num)
                break
            i += 1 # i++ after one iteration
        if n == 1:
            print('1 is neither prime nor composite')
        elif flag == False :
            print('\n',n,' is a prime number.')
        elif flag == True :
            print('\n',n,' is not a prime number.')

    elif choice == 'PMFACT' or choice == 'pmfact': #prints only unique prime factors
        num = int(input('\nEnter whole number : '))
        print('\nPrime factors of ',num,' are : ', end='')
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

    elif choice == 'TAB' or choice == 'tab':
        num = float(input('\nEnter number to generate multiplication table : '))
        for i in range (2,20):
            print(num,' x ',i,' = ',round((num*i),4))
            
            
    elif choice == 'FCTRL' or choice == 'fctrl':
        num = int(input('\nEnter number to obtain factorial : '))
        factorial(num)

    elif choice == 'EQ' or choice == 'eq':
        print('\nGeneral form of quadratic equation is ax2 + bx + c = 0\n')
        a = float(input('Value of a : '))
        b = float(input('Value of b : '))
        c = float(input('Value of c : '))

        dscrmnt = (b**2) - (4*a*c)
        print('\nDiscriminant evaluates to ',dscrmnt)

        if dscrmnt > 0:
            r1= (-b + (dscrmnt**0.5))/ (2*a);
            r2= (-b - (dscrmnt**0.5))/ (2*a);
            print('\nRoot 1 = ',round(r1,4))
            print('Root 1 = ',round(r2,4))

        elif dscrmnt == 0:
            r = -b/(2*a)
            print('\nRoot 1 = Root 2 = ',round(r,4))

        else:
            print('\nRoots are not real.')
            real = -b/(2*a)
            ima = ((-dscrmnt)**0.5) / (2*a)
            print('Root 1 = ',round(real,4),'+',round(ima,4),'i')
            print('Root 2 = ',round(real,4),'-',round(ima,4),'i')

    elif choice == 'HCF' or choice == 'hcf':
        a = int(input('\nFirst Number : '))
        b = int(input('Second Number : '))
        print('\nHCF of ',a,' and ',b,' = ',math.gcd(a,b)) #uses gcd() from math module

    elif choice == 'SMP' or choice == 'smp':
        nu = int(input('\nNumerator is : '))
        den = int(input('Denominator is : '))
        gcd = math.gcd(nu,den)
        print('\nSimplified fraction is',int(nu/gcd),'/',int(den/gcd))

    elif choice == 'TCAL' or choice == 'tcal':
        unit = input('\nRadians (r) or Degrees (d) : ')

        if unit == 'r' or unit == 'R':
            print('\nEnter T.func. followed by angle : ',end='')
            func,rad = input().split()
            rad = float(rad)
            trcalc(func,rad)
        elif unit == 'd' or unit == 'D':
             print('\nEnter T.func. followed by angle : ',end='')
             func,deg = input().split()
             deg = float(deg)
             rad = math.radians(deg) # converts degrees to rad
             trcalc(func,rad)
        else:
            err() 

    elif choice == 'TTAB' or choice == 'ttab': 
        what = input('\nRadians (r) or Degrees (d) : ')

        if what == 'd' or what == 'D':
            dig = float(input('\nEnter degree angle : '))
            this = math.radians(dig) # converts to radians

            print('\nAngle in radian =',round(this,4))
            print('Sin of',dig,'=',round(math.sin(this),4))
            print('Cos of',dig,'=',round(math.cos(this),4))
            print('Tan of',dig,'=',round(math.tan(this),4))
            print('Cosec of',dig,'=',round(1/(math.sin(this)),4))
            print('Sec of',dig,'=',round(1/(math.cos(this)),4))
            print('Cot of',dig,'=',round(1/(math.tan(this)),4))

        elif what == 'r' or what == 'R' :
            this = float(input('\nEnter radian angle : '))
            dig = math.degrees(this) # converts to degrees

            print('\nAngle in degree =',round(dig,4))
            print('Sin of',this,'=',round(math.sin(this),4))
            print('Cos of',this,'=',round(math.cos(this),4))
            print('Tan of',this,'=',round(math.tan(this),4))
            print('Cosec of',this,'=',round(1/(math.sin(this)),4))
            print('Sec of',this,'=',round(1/(math.cos(this)),4))
            print('Cot of',this,'=',round(1/(math.tan(this)),4))

        else:
            err()

    elif choice == 'exit' or choice == 'EXIT': #exit option to terminate loop
        break;
#---------End 'Main'----------
