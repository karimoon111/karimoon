
# COLLECTIONS:are derived data type which stores multiple data type
# -----------
# There are 3 default collections are available and 2 special collections
# *lists
# *tuples
# *dictionaries
# *sets
# *frozensets
# Features of collections:
# ------------------------
# All collections are heterogeneous in python unlike java where arrays stores single type of data.
# *heterogeneous
# *indexed
# *sliced
# *concatenated
# *iterated
# they follow stack architecture.
# stack-->FILO or LIFO
# queue-->FIFO
# in pyhton all collections are 1 dimensional-->1 row, n collections
# collections are also called as sequences.
# Lists:<classlist>
# lists are mutable
# modify
# delete
# add element
# indexing,slicing,iterations,concatenation are possible
# lists stores repetative elements
# syntax
# ------
# <listname>=[<ele1>,<ele2>,<ele3>,<ele4>....]
# nested lists are also possible
# numslist=[10,13,19,7,25,23,35,10,13,7]
# print(numslist)
# print(type(numslist))
# nameslist=["khan","honey","dharu","sari","umar"]
# print(nameslist)
# print(type(nameslist))

# mixedlist=[7,25,36,"ravi","honey",47,54,2]
# print(mixedlist)
# print(type(mixedlist))

# indexing:,
# <listname>[<index>]
# print(mixedlist[0])
# print(mixedlist[-1])
# print(mixedlist[6])

# slicing:
# <listname>[<startindex>:<endsindex>]
# print(mixedlist[2:6])
# print(mixedlist[:6])
# print(mixedlist[2:])

# iterate:
# for <dummy> in <listname>:
# 	<statements>
# for i in range(0,7):
#  	print(mixedlist[i])
# for ele in mixedlist:
# 	print(ele)

# Nested lists:

# mixedlist=[7,25,[36,"khan","hira",85],56,10,28,"dharu","teja",54,46]
# print(mixedlist[0])
# print(mixedlist[2])
# print(mixedlist[2[2])
# nlist=[[[[[[[[10]]]]]]]]
# print(nlist[0][0][0])

# mixedlist=[7,25,33,"khan","hari",47,56,10,30]
# for i in mixedlist:
# 	if type(i) is int:
# 		print(i)
# for i in mixedlist:
# 	if type(i)is str:
# 		print(i)

# deleting
# --------
# del<listname>[<index>]
# del<listname>
# del mixedlist[3]
# print(mixedlist)
# del mixedlist[-1]
# print(mixedlist)
# del mixedlist
# print(mixedlist)

# change/modify
# --------------
# <listname>[<index>]=<newvalue>
# mixedlist[0]="hyderabad"
# print(mixedlist)
# mixedlist[2:5]="hyd","bom","kol"
# print(mixedlist)

# concatenation:
# l1=[10,20,3]
# l2=["honey","hira","teja"]
# l3=l1+l2
# print(l3)

# functions:
# length:number of elements in lists
# syntax:
# len(<listname>)
# print(len(mixedlist))
# a=len(mixedlist)
# print(a)

# count:count the frequency of element
# <listname>.count(<ele>)
# a=mixedlist.count(7)
# print(a)

# index:
# it returns the forward index of particular element in the list
# <listname>.index(<ele>)
# a=mixedlist.index("hari")
# print(a)

# adding of element:
# <listname>.append(<ele>)
# <listname>.insert(<ele>)
# append:is used to add the element in the end of the list because 
# list is the stack it can add only one element at a time.
# mixedlist.append(1000)
# print(mixedlist)
# mixedlist.append("hira")
# print(mixedlist)
# a=mixedlist.append(1000)-->none as output
# print(a)
# mixedlist.insert(3,"jami")
# print(mixedlist)
# a=mixedlist.insert(3,"jami")
# print(a)
# print(mixedlist)
# a=mixedlist.insert(3,"jami")
# print(mixedlist)

# removing of elements
# -------------------
# pop function:removes the last element from the list
# <listname>.pop()
# mixedlist.pop()
# print(mixedlist)
# a=mixedlist.pop()
# print(mixedlist)

# remove function:it removes a particular element in the list.
# <listname>.remove(<ele>)
# mixedlist.remove(7)
# print(mixedlist)
# a=mixedlist.remove(7)-->output as none
# print(a)

# sort function:sorts the lists in an ascending order of the element it only sort homogenous.
# <listname>.sort()
# l1=[2,4,5,98,41,243,7,45]
# l1.reverse()
# print(l1)
# a=l1.reverse()
# print(l1)
# l1.sort(reverse=True)
# print(l1)
# a=l1.sort(reverse=True)
# print(a)
# l=("hira","honey","jami","teja","dharu")
# l.sort()
# print(l)

# extend:<list1>.extend<list2>
# l1=[10,20,30,]
# l2=["khan","honey","hira"]
# l1.extend(l2)
# print(l1)
# print(l2)

# NOTE:-the functions append,insert,reverse,sort do not return any 
# value hence the assignment is none.

# list comprehensions:making of list using initialisation,iteration,condition,operation
# and assignment in a single line comprehension is possible with mutable list.
# syntax:<listname>=[<var>.<iteration>]
# ex:-
# num=[i for i in range(1,8)]
# print(num)
# evens=[i for i in range(1,8) if i%2==0]
# print(evens)
# odds=[i for i in range(1,8) if i%2!=0]
# print(odds)
# sqs=[i**2 for i in range(1,8)]
# print(sqs)
# evensqs=[i**2 for i in range(1,8) if i%2==0]
# print(evensqs)

# tech="pyhton"
# chars=[i for i in tech]
# print(chars)

# stmt="i love python programming"
# wordlen=[len(word) for word in stmt.split()]
# print(wordlen)
# words=[(word) for word in stmt.split() if len(word)>5]
# print(words)

# TUPLES:
# Tuples are immutable collections in python they are object of class tuples.
# they are called as default collection data type they can be index,slice, concatenation,iterate
# it is a heterogeneous collections which allows repeation.
# syntax: 
# <tuplename>=(<ele1>,<ele2>,<ele3>)
# nums=(4,5,6,7,47,68,54,88,97,12,44)
# print(nums)
# print(type(nums))

# a,b=10,20
# print(a)
# print(b)

# a=10,20,30
# print(a)
# print(type(a))
# tuple-->list-->change-->tuple
# indexing:
# print(nums[4])

# slicing:
# print(nums[4:10])

# xxx modify xxx
# len() count() index()-->valid
# sort() append() pop()-->invalid


# fees=(20,30,40,50,60,71)
# print(fees)
# print(type(fees))

# fees=list(fees)
# print(fees)
# print(type(fees))

# fees[2]=55
# print(fees)
# print(type(fees))

# fees=tuple(fees)
# print(fees)
# print(type(fees))

# Tuple comprehension: it is not possible in tuple becoz tuple is inmutable collection data type.

# DICTIONARIES:
# <class dict>
# * arbitary
# *customise indices
# *dictionaries are mutable
# dictionaries are keys,values, pairs were the customise indices are consider as keys and elements
# are stored  in those indices elements are called as values .

# keys
#     unique 
#     inmutable
# values
#      anything
# syntax:
# <dictname>={<k1>:<v1>,<k2>:<V2>,<k3>:<v3>}

# end={}
# print(end)
# print(type(end))

# nums={1:10,2:20,3:30,4:40}
# print(nums)
# print(type(nums))

# names={"khan":50,"hira":40,"honey":55,"hisba":65,(1,2,3):70}
# print(names)
# print(type(names))

# names={"khan":50,"hira":40,"kiran":88,"hira":74}
# print(names)
# print(type(names))

# *slicing ,split are not possible.

# ACCESSING:
# <dictname>[<keys>]
# print(names["khan"])
# print(names["hira"])
# print(names["honey"]

# *delete:
# del<dict name>
# del<dict name>[<keys>]
# del names["hira"]
# print(names)

# Modify:
# <dict name>[<keys>]=<newvalues>
# print(names)
# names["khan"]=35
# print(names)
# names["hira"]=58
# print(names)

# <dict names>.keys()
# <dict names>.values()
# <dict names>.items()
# print(names.keys())
# print(names.values())
# print(names.items())

# for keys in names.keys():
# 	print(keys,end=" ")

# for values in names.values():
# 	print(values,end=" ")

# for items in names.items():
# 	print(items,end=" ")

# functions:
# len()
# print(len(names))
# names.popitem()
# print(names)
# names.pop("khan")
# print(names)

# d1={1:3,2:5,5:6,8:9}
# d2={8:2,3:8,7:9,99:77}
# print(d1)
# print(d2)
# d1.update(d2)
# print(d1)
# print(d2)

# d2.update(d1)
# print(d1)
# print(d2)

# tasK
# inp=10
# {1:1,2:4,3:9,4:16.......10:100}
# inp="python"
# {"p":101,"y":102,"t":103,"h":104,"o":105,"n":106}
# inp="pyhton is easy programming language"
# {"pyhton":6,"is":2,"easy":4,"programming":11,"language":8}


# d={}
# inp=input("enter the input")
# if inp .isdigit():
# 	inp=int(inp)
# 	for i in range(1,inp+1):
# 		d[i]=i**2

# elif " "in inp():
# 	for word in inp.split():
# 		d[word]=len(word)
# else:
# 	for char in inp:
# 		d[char]=ord(char)
# print(d)


# l1=[1,2,3,4]
# l2=[20,30,40,50]
# d={}
# if len(l1)==len(l2):
# 	for i in range (len(l1)):
# 		d[l1[i]]=l2[i]
# print(d)

# zip:-
# zip function takes two list as input  and returns zip of object which needs
# type casted to the collection.
# z0=zip(l1,l2)
# print(z0)
# d=dict(z0)
# print(d)
# l=list(z0)
# print(l)
# t=tuple(z0)
# print(t)
# * zip object consider the minimum length of two list for pairing the data

# sets:-
# * sets are mutable unordered collections
# * sets can be iterated and concatenated.
# * sets are unique storage components.
# *sets comes from the class set.
# *sets is also a heterogeneous.
# syntax:
# -------
# nums={1,2,3,4,5,6}
# print(nums)
# print(type(nums))

# mixedset={10,"khan","hyd",50,90,"python",40,"lync"}
# print(mixedset)
# print(type(mixedset))

# emp={}
# print(emp)
# print(type(emp))

# emp=set(())
# print(emp)
# print(type(emp))

# nums=set((1,2,3,4,5,6,7))
# print(nums)
# print(type(nums))
# for i in nums:
# 	print(i)


# convert list to set:

# l=[1,2,4,6,8,4,8,6,369,1,87,28,87]
# l=set(l)
# l=list(l)
# print(l)
# function:
# nums.add(1000)
# print(nums)

# nums.remove(4)
# print(nums)

# nums.remove(200)
# print(nums)

# note:
# remove function removes the element if available else it returns the error.

# discard function removes the element if available it aviods the error.

# s1={10,20,30,40}
# s2={80,70,50,60}
# s3={30}
# s4={400}
# print(s1.union(s2))
# print(s1.intersection(s2))

# print(s1.difference(s2))
# print(s2.difference(s1))

# print(s1.issubset(s2))
# print(s3.issubset(s1))

# print(s1.issuperset(s2))
# print(s1.issuperset(s3))

# print(s1.isdisjoint(s3))
# print(s1.isdisjoint(s4))
# print(s4.isdisjoint(s3))

# frozenset:
# frozenset is an immutable while elements of a set can be modified at any time
# but in frozenset remains the same after creation so fs is used as keys in dictionary
# but like sets,it is not ordered.

# syntax
# frozenset [iterable]

# vowels=("a","e","i","o","u")
# fset=frozenset(vowels)
# print(fset)

# empfset={}
# print(empfset)
# dictionary comprehension:
# d={i:i**2 for i in range (1,11)}
# print(d)

# stmt="pyhton is an easy programming language"
# d={word:len(word) for word in stmt.split()}
# print(d)

# stmt="python is an programming language"
# d={word:len(word) for word in stmt.split() if len(word)>5}
# print(d)

# sets symbols:
# print(s1|s2)--> union
# print(s1&s2)-->intersection
# print(s2-s1)-->difference
# print(s1-s2)-->difference
# print(s1>s2)
# print(s1>s3)
# print(s1<s2)
# print(s1<s3)



