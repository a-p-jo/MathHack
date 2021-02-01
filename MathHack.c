#include <stdio.h> 
#include <math.h>
#include <string.h>
#include <stdlib.h>

#define _USE_MATH_DEFINES // for M_PI in Visual Studio 

#define error printf("Invalid Input, Sorry.\n");

#ifndef M_PI // for compilers that do not have M_PI in math.h 
#define M_PI (3.14159265358979323846264338327950288)
#endif

void factorial(int unsigned long long); 
long long hcf(long long ,long long);
void trcalc(char * func,double);

int main(int frequency, char * arguments[])
{
	if (frequency >= 3)
	{
		char * choice = arguments[1];

		if (strcmp(choice, "cal")==0)
		{
			double num1, num2, result; 
			char op;

			sscanf(arguments[2],"%lf %c %lf", &num1, &op, &num2);

			switch(op) 
            {
                case '+':
                    result = num1 + num2;
                    printf("%s %lf\n","Result = ",result);
					break;

                case '-':
                    result = num1 - num2;
                    printf("%s %lf\n","Result = ",result);
					break;

                case 'x':
				case '*':
                    result = num1*num2;
                    printf("%s %lf\n","Result = ",result);
					break;

                case '/':
                    result = num1/num2;
                    printf("%s %lf\n","Result = ",result);
					break;

                case '^':
                    result = pow(num1,num2);
                    printf("%s %lf\n","Result = ",result);
					break;

                case '%':
                {
                    long long n1 = (long long) num1; 
                    long long n2 = (long long) num2; // only int values can be used for %

                    printf("%s %lld\n","Result = ",n1%n2);
					break;
                }
				case '\\':
					result = pow(num1, 1.0/num2);
					printf("%s %lf\n","Result = ",result);
					break;

                default :
                    error
					break;

            }
        }

		else if (strcmp(choice, "fact") == 0) 
		{
			long long num = strtol(arguments[2],NULL,10);

			if(num >= 0)
			{
				printf("Factors of %llu are: ", num);
				printf("1,"); // 1 is a factor of every number 
				unsigned long long factor = 2; // counter , starts checking factors from 2
				while (factor <= num / 2) // looks for factors till counter reaches half of num
				{
					if (num%factor == 0)
					{
						printf(" %llu, ", factor);

					}

					factor++;
				}

				printf("%llu\n", num); // number is factor of itself
			}
			else 
				error
		}

		else if (strcmp(choice, "avg") == 0) 
		{
			int i = 0, offset; 

			double sum = 0.0, average; 
			double x = 0.0; 

			while (sscanf(arguments[2],"%lf%n", &x, &offset) == 1)
			{
				sum += x;
				arguments[2] += offset;
				i++;
			}
			average = sum / i;
			printf("Average is %f\n", average);
		}

		else if (strcmp(choice,"prime") == 0 ) 
		{
			long long n = strtol(arguments[2],NULL,10);
			if(n >= 1)
			{
				unsigned long long i;
				int unsigned short flag = 0;

				for (i = 2; i <= (sqrt(n)); ++i) { // checks for factors from 2 to sqrt of number. 
					if (n % i == 0) {
						flag = 1; // flag made True , number is composite 
						break;
					}
				}
				if (n == 1) 
					printf("1 is neither prime nor composite.\n"); 
				else if (flag == 0) 
					printf("%llu is a prime number.\n", n);
				else
					printf("%llu is not a prime number.\n", n);
			}
			else 
				error
		}

		else if (strcmp(choice, "pmfact") == 0 )
		{ 
			long long num = strtol(arguments[2],NULL,10);
			if (num >= 1)
			{
				unsigned i, j;
				unsigned short isPrime; 

				printf("Prime factors of %lld are: ", num); 
				for (i = 2; i <= num; i++) // factors checked b/w 2 to value of number 
				{
					if (num%i == 0) 
					{
						isPrime = 1;
						for (j = 2; j <= i / 2; j++)
						{
							if (i%j == 0) 
							{
								isPrime = 0; 
								break;
							}
						}
						if (isPrime == 1) 
						{
							printf("%u ", i);
						}
					}
				}
				putchar('\n');
			}
			else
				error	
		}

		else if (strcmp(choice, "tab") == 0 )
		{ 
			double num, result; 
			int unsigned short i;

			num = strtof(arguments[2],NULL);

			for (i = 2; i<=19 ; ++i)
			{ 
				result = num*i;
				printf("%.3lf x %i = %.3lf\n", num, i, result);
			}
		}

		else if (strcmp(choice, "fctrl")== 0 )
		{ 
			long long num = strtol(arguments[2],NULL,10);

			if (num <= 20 && num >= 0)
			{
				factorial(num);
			}

			else if (num < 0)
				error

			else
			{
				printf("Sorry, max range is 20! .\n");
			}
		}

		else if ((strcmp(choice, "eq")== 0) && frequency >= 5 )
		{
			double a, b,c, r1, r2, r, dscrmnt, real, img; // co-efficients , constant , roots 1 & 2, discriminat 

			a = strtof(arguments[2],NULL);
			b = strtof(arguments[3],NULL);
			c = strtof(arguments[4],NULL);

			dscrmnt = (b*b) - (4*a*c);
			printf("Discriminant = %lf\n", dscrmnt);

			if (dscrmnt > 0)
			{
				r1= (-b + sqrt(dscrmnt))/ (2*a);
				r2= (-b - sqrt(dscrmnt))/ (2*a);
				printf("Root 1 = %lf\n", r1);
				printf("Root 2 = %lf\n", r2);
			}
			else if (dscrmnt == 0) {
				r = -b/(2*a);
				printf("\nRoot 1 = Root 2 = %lf", r);
			}
			else {
				printf("Roots are imaginary.\n");
				real = -b/(2*a);
				img = sqrt(-dscrmnt) / (2*a);
				printf("Root 1 = %lf + %lfi\n", real, img);
				printf("Root 2 = %lf - %lfi\n", real, img);
			}
		}
		
		else if ((strcmp(choice,"gcd")== 0 || strcmp(choice,"hcf")== 0) && frequency >= 4) { 
			long long a = strtol(arguments[2],NULL,10), b = strtol(arguments[3],NULL,10);
			
			printf("HCF of %lld and %lld = %lld\n", a, b, hcf(a,b)); 
		}

		else if ((strcmp(choice,"smp")==0) && frequency >= 4 )
		{ 
			long long nu = strtol(arguments[2],NULL,10), den = strtol(arguments[3],NULL,10), gcd, newn,newd; // initial numerator & denominator , their hcf/gcd, the new n&d

			gcd = hcf(nu,den);
			newn = nu/gcd;
			newd = den/gcd;

			printf("Simplified Fraction is %lld / %lld\n", newn,newd);
		}

    	else if((strcmp(choice,"tcal")==0) && frequency == 5 )
		{
        	char * func = arguments[3];
        	double rad; 
			char unit = *arguments[2];

        	if(unit == 'd' )
			{
				double deg = strtof(arguments[4],NULL);
            	rad = deg * M_PI/180; // converts angle to radians 
            	trcalc(func,rad); 
			}
        	else if(unit == 'r')
			{
            	rad = strtof(arguments[4],NULL);
            	trcalc(func,rad);
			}
			else 
				error
        }

		else if((strcmp(choice,"ttab") == 0) && frequency >= 4 )
		{ 
			char what = *arguments[2];
			double this,in; // this == rad value ; in == entered value. For rad angle, in == this.

			if(what=='d')
			{
				in = strtof(arguments[3],NULL);

				this = in * (M_PI/180); // converts degree to rad

				printf("Angle in Radian = %lf\n", this);

				printf("\nSin of %.2lf = %lf\n", in, sin(this));
				printf("Cos of %.2lf = %lf\n", in, cos(this));
				printf("Tan of %.2lf = %lf\n", in, tan(this));
				printf("Cosec of %.2lf = %lf\n", in, 1/ (sin(this)));
				printf("Sec of %.2lf = %lf\n", in, 1/ (cos(this)));
				printf("Cot of %.2lf = %lf\n", in, 1/ (tan(this)));
			}
			else if(what== 'r')
			{
				in = strtof(arguments[3],NULL);

				this = in * (180.0 / M_PI); // converts rad to deg

				printf("Angle in degrees = %lf\n ", this);

				printf("\nSin of %.2lf = %lf\n", in, sin(in));
				printf("Cos of %.2lf = %lf\n", in, cos(in));
				printf("Tan of %.2lf = %lf\n", in, tan(in));
				printf("Cosec of %.2lf = %lf\n", in, 1/ (sin(in)));
				printf("Sec of %.2lf = %lf\n", in, 1/ (cos(in)));
				printf("Cot of %.2lf = %lf\n", in, 1/ (tan(in)));
			}
			else 
				error
		}
		else
		{
			error
		}
						
	}
	else
	{
		printf("Not enough arguments.\n");
	}
	
	return 0;
}

void factorial (int unsigned long long x)
{
	unsigned long long f = 1; // stores product
	unsigned long long i; 
	for (i=x;i>=1;i--) // loop decrements from number till 1
		f= f*i; 
	printf("Factorial of %llu = %llu\n",x,f);
}

long long hcf (long long p,long long q) { //recursive function based on Euclid's algorithm to calculate HCF/GCD of two nos. 
	if(q==0) 
		return p; 
	else 
		return hcf(q, p%q); // recursion 
}

void trcalc (char * func,double angle)
{
    if(strcmp(func,"sin")==0)
        printf("Result = %lf\n",sin(angle));

    else if(strcmp(func,"cos")==0)
        printf("Result = %lf\n",cos(angle));

    else if (strcmp(func,"tan")==0)
        printf("Result = %lf\n",tan(angle));

    else if(strcmp(func,"cosec")==0)
        printf("Result = %lf\n",1/ (sin(angle)));

    else if(strcmp(func,"sec\n")==0)
        printf("Result = %lf\n",1/ (cos(angle)));

    else if(strcmp(func,"cot\n")==0)
        printf("Result = %lf",1/ (tan(angle)));

    else
        error
}

/*_______________________________
MathHack & AnPyCalc & AnCalc by Anant Prem Joshi / apjo@tuta.io
_______________________________
AnPyCalc v0.1(+, -, *, /, **)
 v0.2(Fixed Auto-Termination on Windows Cmd)
 v0.3(Added Facorisation)
 v0.4(Added Average)
 v0.4.1(Made easier to enter list for AVERAGE with 'enter number'string)
 v0.4.2(Added ability to enter decimal numbers for AVERAGE)
_______________________________
AnCalc v1.0 (Re-written in C and distributed as .exe + shortened user input)
 v1.1 (used while(1) )
 v2.0 (removed extra " , " @ Ln20 Col81 Ch72, changed message from 'Enter to Restart' to Enter to Reset', removed intro text from loop, fixed bug: every alternate Reset causes invalid input, CALC added moduluo division %, added PRIME)
 v2.1 (added PMFACT)
 v2.2(used continue instead of enter to continue, changed intro text to reflect changed features, removed inessential string.h inclusion)
_______________________________
 AnCalc renamed MathHack

_______________________________

MathHack v1.0 (added TAB : multiplication tables from 2 to 19)
 v1.1 (CALC if staments-->switch table for readability + performance)
 v1.2 (Open-sourcing of code, Binaries for Linux, Streamlining CALC to take expression, '----' after each iteration of while loop)
 v1.3 (added FCTRL,CALC added ' | ' feature, ints to longs & floats to doubles)
 v1.4 (short ints and register variables for loop counters, added error msg when attempting to compute > than 20!)
 v1.5 (#define error, Added EQ & HCF & SMP, enabled selection of function with or without capitlisation)
 v1.5.1 (Spell-correction, whitespace adjustment, Allowing user-defined no. of values in AVG, Replacing * with x in CALC)
 v1.5.2 (Code commenting, code-corrections for minor duplicacy and word choice)
_______________________________

 v2 (Working beyond simple arithmetic -> added Trigonmetric capabilities with TCALC and TTAB, also expanded EQ to complex and non-real roots)
 v2.1 (PRIME loop condition n/2-->sqrt(n), made TAB num double,'degreees'-->'degrees',CALC-->CAL,CAL - % - unisgned int-->long long, ~ all ints-->long long,AVG removed unneccasry arr, Changed Functions display style to be clearer,  Release-Notes-Comments restyled for clarity, scanf(choice) given size limit, added eat() to clear stdin)
 _______________________________
 v3 (Intended as final version)
 * Modified all input to be via command line arguments : Removed all old input code and eat(), added parsing code + stdlib.h , removed infinite while loop + continues.
 * Removed all instances of "register" in var declaration
 * Changed output to not use unnecessary amount of newline. Simle printf("...\n") format.
 * Removed brain-dead obvious comments and improved block-spacing and paranthesis usage for better readability
 * Tested to work.
 */ 
