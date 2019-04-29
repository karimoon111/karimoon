
# introduction
# ------------
# python-->programming language
#       -->script language
# it develop in 1991 by rossum
# current version of pyhton is 3.7
# use cases of python(major)
# --------------------------
# web application-->run with network and browser
# gul application-->run without network and browser
# scripting in develop(automation)
# scientific computing-->which are not done by web app and gul app that will be done by scientific computing
# minor
# -----
# games
# 3D designs
# testing
# features of python
# ------------------
# open source
# easy syntax
# interpreted
# dynamically typed
# extensive library
# keywords
# --------
# -pre defined
# -xxx modify xxx
# -xxx delete xxx
# -xxx add xxx
# in python 3-->35 keywords
# in python 2-->31 keywords
#  import keyword
# keyword.kwlist
# identifiers
#------------
# identifiers are name defined components and these are user defined
# rules of identifiers
# small letter
# capital letter
# xxx start number xxx
# xxx start symbol xxx
# _,_ _(special)
# numbers can be used
# xxx use symbols xxx
# _,@(special)
# example
# -------
# a,name,age,mobile1,first_name,address2home[valid identifiers]
# %name,2mobile,*age,last&name[not valid identifiers]
# _username,_password,@classmethod[special]
# variables
# ---------
# data storage containers
# name/identifiers
# data/value
# location/address
# <varname>=<value>
# a=10
# type -->number
# type(<varname>)
# type(a)-->type of data in a
# id(a)-->address of a
# data types
# ----------
# numbers--> independent data type
# strings-->independent data type
# lists-->derived or collection data type
# tuples-->derived or collection data type
# dictionaries-->derived or collection data type
# sets
# frozensets(special)
# numbers(py3)
# int
# float
# complex
# numbers(py2)
# int
# float
# long
# complex
# sys.maxint(py2)
# sys.maxsize(py3)[2147483647]
# opertions
# ---------
# arithmetic-->numbers
# comparision-->numbers
# logical-->numbers
# bitwise-->numbers
# identity-->strings,lists,tuples,dictionaries
# membership-->strings,lists,tuples,dictionaries
# arithmetic-->7values
# + add
# - sub
# * mul
# / quo
# //floordiv
# % remainder
# comparision
# -----------
# >
# <
# <=
# >=
# ==
# !=
# logical-->3
# and
# or
# not
# ip1  ip2	ip1 and ip2
# t    t      t
# t    f      f
# f    t      f
# f    f      f
# ip1	  ip2	ip1 or ip2
# t      t     t
# t      f     t
# f      t     t
# f      f     f
# a=25
# b=10
# c=5
# a>b and b>c tt-t
# a<b and b>c ft-f
# a>b and b<c tf-f
# a<b and b<c ff-f
# a>b or b>c tt-t
# a<b or b>c ft-t
# a>b or b<c tf-t
# a<b or b<c ff-f
# bitwise opertors-->6-->return values
# ----------------
# BW and -&
# BW or  -|
# BW not -~
# BW leftshift-<<
# BW rightshift->>
# xor-^
# 10-->0001010
# 20-->0010100
# 30-->0011110
# not(10)
# not(10<5)
# ~(10)=-11-->-(x+1)
# 10=0001010
# 10>>2=0000010=2
# 10<<2=0101000=40
# strings
# -------
# immutable data types declared in single or group of character encloses in single and double quotes
# strings can be index-->forward,reverse indices --> <strname>[<index>]
#                slice-->extract substring is a part of string--><strname>[<startindex>:<endindex>:<stepvalue>]
#                literals
#                cancatenation
# immutable-->xxxmodifyxxx
#          -->xxxaddedxxx
#          -->xxxdeletexxx
# tech="python and machine language"
# print(tech)
# print(tech[2:10])
# print(tech[2:10:1])
# print(tech[10:1:-1])
# membership-->in,not in -->true/false
# ----------
# print("p" in tech)true
# print("P"Iin tech)false
# identity-->is,is not
# --------
# tech="python"
# print("python"is tech)
# print("Python"is not tech)
# special character: these are used to pass the string in next line
# -----------------
# and to generate a tab space in a string
# /n-->new line
# /t-->tab space
# tech="python and /n data science"
# print(tech)
# tech="tech/tand/tdata/tscience"
# print(tech)
# multi line string:used to define strings in multiple line not ending in the sameline
# -----------------
# comments--># will be placed in the starting
# multi line comment-->"' will be placed in starting and ending
# raw string-->nulify special characters which are available in string and used in web browser
# path=r"c\tech\python\programs\new\code\tasks"
# print(path)
# inputs-->keyboard input
#       -->CLI input
# py3
# user-->input-->code
# 10------------->'10'
# honey---------->'honey'
# 3.7------------>'3.7'
# py2
# user-->input-->code
# 10------------->10
# honey---------->honey
# 3.7------------>3.7
# py2
# user-->raw_input-->code
# 10---------------->'10'
# 3.7--------------->'3.7'
# honey------------->'honey'
# syntax--> <varname>=input("<dialogue>")
# a=input("enter a number:")
# print()
# string literals
# ---------------
# positional
# %d-->int
# %s-->str
# %f-->float
# example
# name="khan"
# grade="B"
# marks=80
# print(%s has secured %d(name,marks))
# concatenation
# --------------
# str,str-->+
# str,int-->,
# print("name of student"+name)
# print(name+"has secured",marks,"marks")
# type casting-->conversion of one data type to another data type if allowed
# int-->str-->str()
# str-->int-->int()
# ASCII:
# char-->ascii-->ord()
# ascii-->char-->chr()
# print(ord("m"))
# print(chr("100"))
# string function-->case based
#                -->checking
#                --->operation
# functions-->parameterised(<something>)
#          -->attribute fetching.
# case based
# ----------
# <strname>.lower()
# <strname>.upper()
# <strname>.title()
# <strname>.swapcase()
# <strname>.capitalize()
# stmt="python is an easy language"
# print(stmt)
# print(stmt.lower())
# print(stmt.upper())
# print(stmt.title())
# print(stmt.swapcase())
# print(stmt.capitalize())
# <strname>.startswith(<char/substring>)
# <strname>.endswith(<char/substring>)
# <strname>.isdigit()
# len(<strname>)
# print(len(stmt))
# count function : returns frequency of character or substring part
# <strname>.count(<char> / <substring>)
# print (stmt.count("p"))
# index function :
# <strname>.index (<char>/<substring>)
# index function retrurns index value of first occurence of character or substring part
# print (stmt.index("a"))
# print (stmt.index("z")) output=error
# find function : returns index value of 1st occurence of character or substring in a string
# it returns -1 if character is not found unless function returns error
# <strname>.find (<char>/substring)
# print (stmt.find("a")) 
# print (stmt.find("z"))->o/p=-1
# replace : it is used to replace parts of string with new substring
# <strname>.replace(<old>,<news)
# split : It returns collection of words from string separated at a space.
# <strname>.split()
# print (stmt.split())
# print (stmt.split("i"))
# words = stmt.split()
# print (words) 
# Join :
# ----
# <delimiter>.Join(<collection>)
# print (" ".join(words))
# print ("-".join(words))
# Strip :-
# strip function are used to remove whitespaces in the string
# lstrip
# rstrip
# stmt = "     in india we live     "
# print (stmt)
# print (stmt.strip())
# print (stmt.lstrip())
# print (stmt.rstrip())
# print (stmt.strip(" i "))
# Z fills :-
# <strname>.zfill(<len>)
# name="sari"
# print(name.zfill(8))
# name=100
# print(num.zfill(5))
# Conditional Statement :- are decision making components in python they required condition 
# and also statement every block of condition should be followed by stmt
# *Python has 3 kinds of condition format stmt.
# *if 
# *if else 
# *if elif elif elif -----else
# conditional statement can also be nested
# Syntax :-
# if <condition> :
# 	<statement>
# if <condition> :
# 	<statement>
# else:
# 	<statement 2>
# if <condition>:
# 	<statement1>
# elif <condition2>
# 	<statement2>
# else:
# 	<statement3>
# Loops :-Loops are used for making repetition there are 2 types of Loops
# 	* Finite Loops
# 	* Infinite Loops
# Python has two loops *for[finite]
# 					 	numbers 
# 					 	strings
# 					 	collections
# 					 *while[finite/infinite]
# For each loop * initialisation[start point]
# 				limit [end point]
# 				inc/dec [step]
# for with number :-
# Range function is used to literate the over numbers it can be used to numbers.
# It can be written in 3 ways
# 1. range(<end>)
# 2. range(<start>, <end>)
# 3. range(<start>,<end>,<step>)
# Syntax:-
# for <dummy> in range (<>):
# 	<statement>
# 	for i in range (10):
# 		print (i,end=" ")
# 	print()
# 	for i in range(5,22):
# 		print (i,end=" ")
# 	print()
# 	for i in range(5,100,5):
# 		print (i,end=" ")
# 	print()
# For---> strings
# tech = "python and machine language"
# for<dummy> in <stringname>
# 	<statement>
# for i in tech :
# 	print(i)
# While loop :
# <initialisation>
# while<condition> :
# 	<statement>
# 	<inc/dec>
# a=1
# while a<10:
# 	 print(a)
# 	 a=a+1
# a=0
# while a>0:
# print(a)
# 	a=a-1
# *a=1
# while a<10:
# 	print(a)
# while True:
# 	print ("hello")
# Control statement :-
#  { } ; --> control flow chars
#  : tab space --> control flow chars in python
#  3-Control statement:-
#   pass : It is used to control statement which can be used for an implemented blocks 
#   then there is no statement it skip the execution that particular block.
#   Ex: for i in range(10):
#   		pass 
#   Break : It is used to exit the loop at the condition 
#   Ex: for i in range (1,20):
#           if i==20:
#           		break 
#           print (i, end=" ")
#   stmt = "python and machine language"
#   for char in stmt :
#   	  if char is "d":
#   	  	break
#   	  print(char)
# Continue :- It is used to exit the loop and execute it again at a condition when it is true within the limit.
# Ex:- for i in range (1,20):
# 	     if i==10:
# 	     	Continue
# 	     print (i,end=" ")
# stmt = "Python and machine language"
# Ex:- for char in stmt :
# 		if char is "d":
# 			Continue
# 		print (char, end=" ")
# dir(<classmate>)
# all function in a class 
# print(dir(str))
# print(dir(int))
