# time="08:34:56PM"
# hh=time[0:2]
# mm=time[3:5]
# ss=time[6:8]
# ff=time[8:]
# print("Hours is: "+hh)
# print("Minutes is: "+mm)
# print("Seconds is: "+ss)
# print("Form is: "+ff)

# import datetime
# time=datetime.datetime.now()
# print("Hours is: %d " %time.hour)
# print("Mins is: %d " %time.minute)
# print("Seconds is: %d " %time.second)
# for row in range (7):
#     for col in range(5):
#         if ((col==0 or col==4) and (row!=0) or ((row==0 or row==3)and(col>0 and col<4))):
#             print("*",end="")
#         else:
#             print(end=" ")
#     print()

# alphabet pattern 

# n=5
# for i in range (0,6):
# 	for j in range(97,97+i):
# 		a=chr(j)
# 		print(a,end=" ")
# 	print()

# n=6     
# for i in range(97,102):
#     print(chr(i)*(i-96))


# n=5
# for i in range(1,6):
#     print(str(i)*i)

# n=5
# for i in range (1,n+1):
#     for j in range (1,i+1):
#         print(j,end=" ")
#     print()

# num=5
# for i in range(0,num):
#     for j in range(0,num-i-1):
#         print(end=" ")
#     for j in range(0,i+1):
#         print("*",end=" ")
#     print()


# n=5
# for  i in range(1,6):
#     print(" "*(n-i)+str(i)* i)

# n=5
# a=0
# while a<5:
#     a=a+1
#     print(" "*(n-a)+str(a)*a)

# a=1
# while a<6:
#     print("*"*a)
#     a=a+1




# a=97
# b=122
# while a<=b:
#     print(chr(a)*(a-96))
#     a=a+1

# for num in range(1,13):
#     if num%2==0:
#         print(num,"is composite")
#     else:
#         print(num,"is prime")

# a=input("Enter a value")
# if a.isdigit():
#     a=int(a)
#     if a%3==0  and a%5==0 :
#         print(str(a)+"Is a multiple of both ")
    
#     elif a%3==0 and a%5!=0:
#         print(str(a)+"is a multiple of 3")
#     elif a%3!=0 and a%5==0:
#         print(str(a)+"is a multiple of 5")
#     else:
#         print(str(a)+"is not multiple of both")
                    
# n=10
# if n%2==0:
#     print("number is even")
# else:
#     print("number is odd")

# i=2
# while i<13:
#     i=i+1
#     if (i%2!=0):
#         print(str(i)+"is odd")
#     else:
#         print(str(i)+"is even")


# i=2
# while i<13:
#     i=i+1
#     if (i%2!=0):
#         print(str(i)+"is odd")
#     else:
#         print(str(i)+"is even")

      
# n=5
# for i in range(1,11):
#     print("5"+"*"+str(i)+"="+str(i*n))
     
# n=5
# a=1
# while a<10:
#     print("5"+"*"+str(a)+"="+str(a*n))
#     a=a+1

# task 1 file:
# a=6
# while(a>0):
# 	a=a-1	
# 	print("*"*a)

# multiple of 9
# n=9
# a=1
# while(a<11):
# 	print("9"+"*"+str(a)+"="+str(a*n))
# 	a=a+1

# sum of digit
# n="234578"
# sum=0
# for i in range(0,len(n)):
# 	sum=sum+int(n[i])
# print(sum)

# fibonacci series
# a=0
# b=1
# for i in range(1,10):
# 	print(a)
# 	c=a
# 	a=b
# 	b=c+a

# check prime or not
# n=11
# if n>1:
# 	for i in range(2,11):
# 		if (n%i)!=0:
# 			print(n, "is not a prime number")
# 			break
# 		else:
# 			print(n,"is a prime number")

# armstrong number

# n=112
# sum=0
# temp=n
# while temp>0:
# 	a=temp%10
# 	sum=sum+a**3
# 	temp=temp//10
# if n==sum:
# 	print(n,"is an armstrong number")
# else:
# 	print(n,"is not an armstrong number")
	
 
# divisible by either 2 or 3
 
# for i in range(0,51):
# 	if (i%2==0 or i%3==0):
# 	 print(i)

# even and add

# even=0
# odd=0
# for i in range(1,51):
# 	if (i%2==0):
# 		even=even+1
# 	if(i%2==1):
# 		odd=odd+1
# print("number of even:",even)
# print("number of odd:",odd)

# variables and data types:

# L=["digital","lync","hyderabad","gachibowli","kukatpally"]
# print("gachibowli" in L)

# bitwise operations
# a=45
# b=65
# c=a&b,a|b,a>>b,a<<b,a^b
# print(c)
# z=65.33
# import math
# # print(int(z),complex(z),float(z))
# # print(math.factorial(int(z)))
# # print(math.sqrt (65))
# # print(math.exp(z))
# print(abs(z))

# sum of digits in an integer
# n=65
# a=n//10
# b=(n-a*10)
# print("sum of the digits in number:",a+b)

# comparision
# a=15
# b=2
# c=a>b,a<b,a>=b,a<=b,a==b,a!=b
# print(c)

# control flow

# for i in range(1,50):
# 	if(i%3==0 or i%5==0 ):
# 		continue
# 	else:
# 		print(i)

# even number squares
# for i in range(1,5):
# 	if(i%2!=0):
# 		continue
# 	else:
# 		print(i*i,end=" ")

# odd number divisible by 7
# for i in range(1,100):
# 	if (i%2==1 and i%7==0):
# 		print(i,end=" ")

# print vowels in agiven string
# n="sari is a good girl"
# vowels="aeiou"
# for char in n:
# 	if char not in vowels:
# 		pass
# 	else:
# 		print(char)
# CONDITIONAL:

# n=int(input("enter n"))
# if (n%4==0 and n%100!=0 or n%400==0):
#     print("n is a leap year")
# else:
#     print("n is not a leap year")


# n=int(input("enter n"))
# if(n%2==0):
#     print("n is a even")
# else:
#     print("n is odd")

# largest of 3 numbers
# num1=int(input("enter the first number"))
# num2=int(input("enter the second number"))
# num3=int(input("enter the third number"))
# if(num1>num2) and (num1>num3):
# 	largest=num1
# elif(num2>num1) and(num2>num3):
# 	largest=num2
# else:
# 	largest=num3
# print("the largest number",largest)
	
# grading system of marks
# sub1=int(input("enter marks of the first subject:"))
# sub2=int(input("enter marks of the second subject:"))
# sub3=int(input("enter marks of the third subject:"))
# avg=(sub1+sub2+sub3)/3
# if (avg>=90):
# 	print("Grade:A")	
# elif(avg>=80 and avg<90):
# 	print("Grade:B")
# elif(avg>=70 and avg<80):
# 	print("Grade:C")
# elif(avg>=60 and avg<70):
# 	print("Grade:D")
# else:
# 	print("Grade:E")

# multiples of 3 position of a input
# tech="python is best for beginners"
# print(tech[0::3])


# strings

# str="pythonbestforbeginners"
# string=str[1::2]
# print(string)

# tech="python"
# print("".join(reversed(tech)))

# tech="python"
# print(tech.replace("h","@"))

# string = "geeks for geeks geeks geeks geeks"
# print(string.replace("geeks","Sari"))

# swap of two numbers
# a=int(input("enter first value"))
# b=int(input("enter second value"))
# a=a+b
# b=a-b
# a=a-b
# print("a is:",a,"b is:",b)

# name="karimoon"
# marks=400
# percentage=78
# print("marks obtained is:", marks,"marks")
# print("percentage secured: ", percentage,"percentage")
# print("student name is: " +name)

# palindrome or not:

# def isPalindrome(s):  
#     rev = ''.join(reversed(s)) 
#     if (s == rev): 
#         return True
#     return False 
# s = "moon"
# ans = isPalindrome(s) 
  
# if (ans): 
#     print("Yes") 
# else: 
# 	print("No")

# fibonacci series using recursion
# def fibonacci(n):
# 	if(n<=1):
# 		return n
# 	else:
# 		return(fibonacci(n-1) + fibonacci(n-2))
# n=10		
# for i in range(n):
	# print(fibonacci(i))

# import random
# def pwd():
#     pwd = ''
#     pwd = pwd + str(random.randint(1000, 9999))
#     for i in range(4):
#         pwd = pwd + chr(random.randint(ord('a'), ord('z')))
#     pwd = pwd + str(random.randint(1000, 9999))
#     for i in range(4):
#         pwd = pwd + chr(random.randint(ord('a'), ord('z')))
#     return pwd
                                 
# name = input('Enter a name :')
# pwd = pwd()
# fo = open("pwd.txt", 'a')
# fo.close()
# fo = open("pwd.txt", 'r')
# count = 0
# while 1:
#     ln = fo.readline()
#     li = ln.split('-')
#     if ln == '':
#         break
#     elif li[0] == name:
#         count = 1
#         print("already exists")
#         break
# fo.close()
# fo = open("pwd.txt", 'a')
# if count != 1:
#     fo = open("pwd.txt", 'a')
#     fo.write(name)
#     fo.write('-')
#     fo.write(pwd+'\n')
# fo.close()
