# funtional programming
# ---------------------
# use of function for special modulalisation  in could be done.
# they are two types of function 
# 1.pre defined 
# 2.over defined
# function has 3 main components
# 1.definition
# 2.implementation 
# 3.function call 
# A function is class function the definition+implememtation
# are manditory component the function call is optional.

# *definition +implementation occur only once where as call 
# can occur multiple time.
# *Each function is written for ingle function

# function are classified into 4 types based on parameter + return types

# syntax:
# def<function name>():<implementation>
# <function name>()

# *If the multiple function are defined with same name then the latest
# implementation taken into the function.

# *call trigers the function to get the output.

# def sayhello():
# 	print("hello")
# 	print("hi")
# sayhello()
# print(sayhello)
# print(sayhello())
# print(type(sayhello))
# print(type(sayhello()))

# parameter
# --------
# parameter are also terms as argument they are input that passes
# to functions.
# *python function accept two types of parameter
# 1.formal parameter
# 2.actual parameter

# *The formal parameter are nomial+variables defined in the function defination.
# *actual parameter are the values those are passed to the formal parameter.
# Actual parameter are written in function call
# 4 kinds of parameters
# 1.positional
# 2.default
# 3.variables
# 4.keyword

# POSITIONAL:
# no.of formal parameter=no.of actual parameter
# def addnums(a,b):
# 	ans=a+b
# 	print(ans)
# addnums(10,20)


# def addnums(a,b):
# 	ans=a+b
# 	return ans
# ans=addnums(20,30)
# print(ans)

# def addnums(a,b):
# 	ans=a+b
# 	return 100
# ans=addnums(20,30)
# print(ans)

# return of a function is the output of a particular function
# mostly.It can be used in 4 ways
# 1.return of values
# 2.return of variables
# 3.return of function name
# 4.return of function call

# enter a number 40
# enter a number 10

# addnums 40,10-->50
# subnums 50,10-->40
# mulnums 40,10-->400
# divnums 400,10-->40

# def addnums(a,b):
# 	ans=a+b
# 	return ans
# def subnums(a,b):
# 	ans=a-b
# 	return ans
# def mulnums(a,b):
# 	ans=a*b
# 	return ans
# def divnums(a,b):
# 	ans=a/b
# 	return ans
# addans=addnums(40,10)
# subans=subnums(addans,10)
# mulans=mulnums(subans,10)
# divans=divnums(mulans,10)
# print(divans)

# function can have any return if multiple returns is passed
# the first returns will be considered.

# Default parameter:is used to pass the default values to variables in the function
# here we use variable in actual parameter and values in formal parameter.

# def login(user,role):
# 	print("the user is "+ user)
# 	print("the role is "+ role)
# login("khan","pd")
# login(role="pd",user="khan")


# def makecake(flvr="vennila",wei="2",shape="square"):
# 	print("the flavour of cake " +flvr)
# 	print("the weight of cake " +wei)
# 	print("the shape of cake "+shape)
# makecake("choc","3","round")
# makecake(flvr="pine",shape="round")
# makecake(flvr="choc",wei="3")
# makecake(wei="3")
# makecake()

# Variable parameter:
# Variable parameter are dynamic parameter which change according to the parameter
# passed in the function call.
# they are given by"args" where args is atuple they are passed in the function definition"*args".
# def avg(*args):
# 	print(args)
# 	print(type(args))
# avg(10,20,30,40)

# average of numbers
# def avg (*args):
# 	mean=sum(args)/len(args)
# 	print(mean)
# avg(10,20,30,40,50)

# def avg(a,b,*args):
# 	print(a)
# 	print(b)
# 	print(args)
# avg(10,20,30,14,7)
# avg(10,20)
# NOTE:
# The function belongs to class function and function call belongs
# to class of the return type.

# def addnums(a,b):
# 	ans=a+b
# 	return(ans)
# print(addnums)
# print(type(addnums))
# print(addnums(100,200))
# print(type(addnums(100,200)))

# getindex("pyhton and machine language"," ")
# checkchar()

# stmt="python and machine language"
# char=" "
# def checkchar(statement,character):
# 	if character in statement:
# 		return statement.count(character)
# 	else:
# 		return 0
# def getindex(stmt,char):
# 	reps=checkchar(stmt,char)
# 	if reps>0:
# 		i=-1
# 		while reps>0:
# 			i=stmt.index(char,i+1)
# 			reps=reps-1
# 			print(i)
# getindex(stmt,char)

# calsum([1,2,3,4],[100,200,300,400])
# [(1,100)(2,200)(3,300)(4,400)]
# [101,202,303,404]

# def calsum(l1,l2):
# 	zo=zip(l1,l2)
# 	ans=list(zo)
# 	print(ans)
# 	for i in range (len(ans)):
# 		sumTuple=sum(ans[i])
# 		ans.remove(ans[i])
# 		ans.insert(i,sumTuple)
# 	print(ans)
# calsum([1,2,3,4],[100,200,300,400])

# DOCSTRING:
# Docstring is matadata of a function it is return just after the definition
# as multiline comment it is store in variable __ doc __
# <functionname>.__doc__

# def demo():
# 	'''
# 	this is demo function
# 	'''
# demo()
# print(demo.__doc__)

# print(len.__doc__)
# print(list.append__doc__)
# print(.__doc__)

# def convert(a):
# 	str="".join(a)
# 	return str
# a=("s","a","r","i")
# str=(convert(a))
# print(str)

# def reverse (a):
# 	b=a[::-1]
# 	return b
# a=("dharmateja")
# print(reverse(a))

# KEYWORD PARAMETER:
# -----------------
# keyword parameter stores the excess values in the 
# parameter as pair of keys and values in a dictionaries.
# The name of dictionaries is "kwargs".It is given in the function
# definition as "**kwargs".

# def makecake(flvr="vannila",shape="square",wei="3",**kwargs):
# 	print("flavour of cake"+flvr)
# 	print("shape of cake"+shape)
# 	print("weight of cake"+wei)
# makecake("choc","round","3")
# makecake("choc","round","3",toppings="almond")

# LAMBDA FUNCTION/ANONYMOUS FUNCTION:
# It is used to havea one line implementation of the code.
# lambda function is auto return .
# it is both parameterised and non parameterised.
# syntax:
# <functionname>=lambda<parameter>:<implementation>

# addnums=lambda a,b:a+b
# print(addnums(10,20))

# makemail=lambda user ,cname:"user"+"@"+"cnmae"+".com"
# print(makemail("hira","hcl"))

# def first (name):
# 	print("hello "+ name)
# def second(name):
# 	print("bye "+ name)
# 	return first
# print(first("hira"))
# print(second("hira"))

# a=second("john")
# a("khan")


# def first (name):
# 	print("hello "+name)
# def second(name):
# 	print("bye "+name)
# 	return first(name)
# print(type(second("khan")))-->class none

# def first(name):
# 	print("hello "+name)
# 	return 100
# def second(name):
# 	print("bye "+name)
# 	return first(name)
# print(type(second("khan")))-->class int

# MAP:
# map is the pre-defined function that returns the map
# object it takes function name and collections of its parameter.
# It is used to calculate the associate operation of the collections.
# <mapobject>=map(<functionname>,<collection(s)>)

# NOTE:
# The functionname passes it needs the return type.

# square of number
# l1=[i for i in range(10)]
# def square (num):
# 	return num**2
# print(list(map(square,l1)))

# l1=[i for i in range(10)]
# l2=[i for i in range(10,20)]
# print(list(map(lambda a,b:a+b,l1,l2)))

# stmt="python is easy programming language"
# print(list(map(len,stmt.split())))

# def addnums(a,b):
# 	return a+b
# mo=map(addnums,l1,l2)
# l=list(mo)
# print(l)

# FILTER:filter function is used to return filter object
# which has all the truth values of a collection for a 
# condition it takes a function name and collection as input.
# syntax:
# <filtername>-filter(<filtername>,<collection>)

# l1=[i for i in range (30)]
# f=filter(lambda a:a%2==0,l1)
# print(list(f))
# f=filter (lambda a:a%2!=0,l1)
# print(list(f))

# Reduce:-Reduce is an  internal imported function
# *It is imported from functools.it  performs cumulative operation.
# *It takes functionname and collection as input and it returns cumulative output.
# ex:sum of list, product of list,sub of list.

# syntax:
# <ans>=reduce(<functionname>,<collection>)

# l1=[i for i in range (1,31)]
# from functools import reduce
# pro=reduce(lambda a,b:a*b,l1)
# print(pro)
# ans=reduce(lambda a,b:a+b,l1)
# print(ans)


# import sys
# def getargs(l):
# 	if len(l)==3:
# 		if int(l[1])<=26 and int(l[2]) in(1,2):
# 			return (int(l[1]),int(l[2]))
# 	else:
# 		print("invalid input")

# def generator ():
# 	inps=getargs(sys.argv)
# 	op=" "
# if inps[1]==1:
# 	for i in range (inps[0]):
# 		op=op+str(i)
# else:
# 	for i in range (97,97+int(inps[0])):
# 		op=op+str(i)
# 	print("op")
# generator()
# file handing:
# ------------
#  file is the data storage component which stores in various form.
#  file contain 3 components:
#  1:location
#  2:file name
#  3:extension
# *By default python works with txt files it can also
# handle "html"files
# *If excel csv needs to use  "pandas"
# *if csv alone needs to use"csv"
# *if excel alone needs to use "xlsxwriter"
# *if pdf alone needs to use"pypdf2"
# NOTE:
# using of file helps to stores history  of data unlike
# collection which initailze each timr and run the code.
# *The encoding format for the files in windows is CP1252
# LINUX/UNIX is utf-8
# There are 7 modes of operation of a file
# 1.read-->r
# 2.write-->w
# 3.append-->a
# 4.read binary-->rb
# 5.write binary-->wb
# 6.update-->multiple purpose-->rb+,wb+

# *files in python is autosaved and explicit buffer is absent.
# *python creates file object for each file instant.

# OPEN FUNCTION:
# open function is used to create and open aa file if file 
# doesn't  exists or to open a file if file exists,and it takes
# 2 inputs.

# if file should be created and open mode should be write as
# <fileobject>=open("<filename>","<mode>")


# *fileobject should be closed aftera write code.
# <operation>
# <fileobject>.close()

# fo=open("first.txt","w")
# fo.close()


# writing data onto the file :-
# we have 2 object 
# 1.fileobject .write
# 2.fileobject

# we can only write strings on to the file 
# *write are used to write a single stirng writelines is used to 
# write a collection of lines.

# fo=open ("hira.txt","w")
# fo.write("first\n")
# fo.write("second\n")
# lines=["python\n","java\n","html\n"]
# fo.writelines(lines)
# fo.close()

# fo=open("hira.txt","w")
# lines=[str(i) for i in range (0,n)]
# fo.writelines(lines)
# print(lines)
# fo.close()



# append mode:-
# append mode is used to write the data without erase
# the previous data it does not make the file empty before 
# data unlike write,writelines function.


# fo=open("hira.txt","a")
# fo.write("first\n")
# fo.write("second\n")
# fo.close()

# n=8
# fo=open("hira.txt","w")
# a=[chr(i)+"\n" for i in range(97,97+n)]
# fo.writelines(a)
# fo.close()


# n=5
# fo=open("hira.txt","w")
# a=[chr(i)*(i-96)+"\n" for i in range(97,97+n)]
# fo.writelines(a)	
# fo.close()

# n=5
# fo=open("hira.txt","w")
# a=[str(i)*i+"\n" for i in range(1,n+1)]
# fo.writelines(a)
# fo.close()

# reverse of num:
# n=5
# fo=open("hira.txt","w")
# a=[" "*(n-i)+str(i)*i+"\n" for i in range(1,6)]
# fo.writelines(a)
# fo.close()

# ascii
# n=5
# fo=open("hira.txt","w")
# for i in range(0,n+1):
# 	for j in range(97,97+i):
# 		fo.write(chr(j))
# 	fo.write("\n")
# fo.close()

# n=5
# fo=open("hira.txt","w")
# for i in range(1,6):
# 	for j in range(1,i+1):
# 		fo.write(str(j))
# 	fo.write("\n")
# fo.close

# reverse of star
# n=5
# fo=open("hira.txt","w")
# a=[" "*(n-i)+"*"*i+"\n" for i in range(1,6)]
# print(a)
# fo.writelines(a)
# fo.close()

# star 
# fo=open("hira.txt","w")
# a=["*"*i +"\n" for i in range(1,6)]
# fo.writelines(a)
# fo.close()

# Reading file :
# we have 3 functions in python to read the python file.
# 1.fo.read :it reads enter data from file from starting to end.

# fr=open ("hira.txt","r")
# data=fr.read()
# print(data)

# A Numeric parameter is passed to read only "n" character from the file.
# data=fr.read(5)

# Readline:it is used to print first line of data from current curser position.
# the default position of curser is at the start of file.

# Readlines: it is used to read enter data as a list of all the lines.
# print(fr.readlines())

# fr=open("hira.txt","r")
# data1=fr.read().split(",")
# print(data1[:6])
# print(data1[5:11])
# print(data1[10:17])
# fr.close()

# n=18
# fo=open("hira.txt","w")
# for i in range(0,17):
# 	fo.write(str(i)+",")
# fo.close()
# fr=open("hira.txt","r")
# data1=fr.read().split(',')
# for i in range(6):
# 	print(data1[i],end=' ')
# print()
# for i in range(5,11):
# 	print(data1[i], end = ' ')
# print()
# for i in range(10, n):
# 	print(data1[i], end = ' ')
# fo.close()

# fr=open("hira.txt","r")
# data=fr.read()
# print(data)
# data1=fr.read(2)
# print(data[-1]+data1)
# fr.close()


# n=8
# fo=open("hira.txt","w")
# a=[chr(i) for i in range(97,97+n)]
# fo.writelines(a)
# fo.close()
# fr=open("hira.txt","r")
# data=fr.read()
# for i in range(0,4):
# 	print(data[i],end=" ")
# print()
# for i in range(3,6):
# 	print(data[i],end=" ")
# fr.close()


# Modules and packages:
# There are 3 kinds of Modules
# 1.internal default
# 2.internal import
# 3.external

# module-->any python file is called module.-->(.py,.ipynb,.pyc)

# internal default: Module have their components on every module by default.
# ex: print,len,sort.

# Internal import:these are available in library but not on the module
# ex:reduce--> from functools import reduce
#    kw-->import sys
#    argb-->import keyword
# External:- There are not available either on the module or in the default
# python libraries we need to download the modules,install them then import
# and use.we use packages manager for this purpose pyhton have pre-defined
# package manager .python packaging index[pip]

# * pip need installed to using it is available to install during installation.
# * if unavailable run "get-pip.py" file available externally.

# pip list:- it shows  all the modules in the curent installation.

# pip list-->all modules(pip,setuptools)

# *pip install<modulename>
# *pip unstall<modulename>

# pip freeze:-returns the moduleds or packages that are manually installed.
# The installed packages using pip gets installed "site-packages location".

# packages:-package is a collection of python modules along with the special
# module[installation__ int__.py]

# complete importing: it import all components from module it can
# be access to using complete import module refrence.

# <modulename>.<component>

# import module4
# print(module4.d)
# print(module4.mixed)

# NOTE:it import all the components but module reference are not need.

# from module4 import*
# print(d)
# print(mixed)

# Specific import:
# Specificcomponents are imported but reference are not

# from<modulename>import<component>

# from module4 import d,mixed
# print(d)
# print(mixed)

# ALISING:
# import<modulename> as <mn>
# <mn>,<component>

# Random module:
# It is used to generation of pseudo random number it work 
# with random module is used with number and collection.it is an internal 
# interperted module.
# import random
# print(random.random())
# it generate random float between 0 and 1.

# randint:it generate the random numbers between the range inclusive
# of end points.
# print(random.randint(2,10))

# randrange:it generate the random numbers between the range inclusive of 
# end points.
# print(random.randrange(2,10))
# random for collections:

# shuffle function :it randomly shuffles the collections
# import random
# l1=[i for i in range(12)]
# random.shuffle(l1)
# print(l1)

# choice function :it returns one random number from the collections
# print(random.choice(l1))

# sample function:it returns "k" randomnumbers from the collections. where "k"
# is called population.
# print(random.sample(l1))
           # or
# print(random.sample(l1,k=3))
# os module:
# os module is used for 2 purpose 
#         1.working with directories
#         2.system path manipulation
# * os is an internal import module 
# import os
# print(os.name)-->nt is family of windows os
# print(os.getcwd)-->current working directory

# making of directories 1.os.mkdir
#                       2os.makedirs

# mkdir: mkdir is used to createan single empty directory in the cwd location
# print(os.mkdir("demo"))

# os.makedirs:makedirs is used to create tree of empty directories in cwd location.
# print(os.makedirs(r" dir1\dir2\dir3"))


# Removing of directories:
# To remove directoriesfrom cwd we have 2 functions 
#          1. os.rmdir
#          2.os.removedirs
# python can remove only empty directories
# print(os.rmdir("demo"))
# print(os.removedirs(r" dir1\dir2\dir3"))

# print(os.path.split(r"C:\Users\Mohammad\Desktop"))
# print(os.path.split(r"C:\Users\Mohammad\Desktop\hira"))
# print(os.path.splitext(r"C:\Users\Mohammad\Desktop\hira"))

# os.walk
# for paths,dirs,files in os.walk(r"C:\Users\Mohammad\Desktop"):
# 	print(paths)
# 	print(dirs)
# 	print(files)
# 	print()

# print(os.path.isfile(r"C:\Users\Mohammad\Desktop\module1"))
# print(os.path.isdir(r"C:\Users\Mohammad\Desktop"))
# print(os.path.exists(r"C:\Users\Mohammad\downloads"))



# class double:
# 	def __init__(self,last):
# 		self,last=last
# 	def __iter__(self):
# 		self.n=0
# 		return self
# 	def __next__(self):
# 		if self.n<=self.last:
# 			res=2*self.n
# 			self.n +1
# 			return res
# 		else:
# 			rise stopiteration
# for i in double(10):
# 	print(i,end=" ")
print(5^7)


