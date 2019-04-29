
# l1=[2,4,5,7,98,41,423,7,5,4,7,98,4]
# uni=[]
# for i in l1:
# 	if i not in uni:
# 		uni.append(i)
# print(uni)
# tech="python"
# chars=[ ]
# for i in tech:
# 	chars.append(i)
# print(chars)
# tech="python language is easy"      
# word=tech.split()
# for tech in word:
# 	print(len(tech),end=" ")
# l1=[1,2,3]
# l2=[10,20,30]
# l3=[]
# for i in l1:
# 	l3.append(l2[l1.index(i)]+(i))
# print(l3)
# without using append:
# l1=[1,2,3]
# l2=[10,20,30] 
# for i in range(0,3):
# 	print((l1[i]+l2[i]))
# l1=("khan","hira","lovely","dharu","teja","umar")
# l2=(0,3,5)
# l3=[]
# for i in l2:
# 	l3.append(l1[i])
# print(l3)

# nums=[ ]
# num=int(input("enter a number"))
# if num.isdigit():
# 	for i in range(0,num+1):
# 		print(nums)

# tech="python"
# chars=[i for i in tech]
# print(chars)

# second largest number
# l1=[10,20,30,40,50,8,45]
# l1.sort()
# print("second largest number",l1[-2])

# import statistics 
# l1=[2,5,4,4,4,6,7]
# print("mode of given of l1 ",(statistics.mode(l1)))	

# l1=[2,4,5,5,8,4,58,45,7,6,2]
# uni=[]
# for i in l1:
# 	if i not in uni:
# 		uni.append(i)
# print(uni)

# l1=[1,4,9,16,25,36,49,64,81,100]
# a=[a for a in l1 if a%2==0]
# print(a)

# x=[[1,2,3],
#   [5,6,8],
#   [4,5,6]] 
# y=[[2,4,5],
#   [4,8,9],
#   [3,6,7]]
# result=[[0,0,0],
#        [0,0,0],
#        [0,0,0]]
# for i in range(len(x)):
# 	for j in range(len(x[0])):
# 		result [i][j]=x[i][j]+ y[i][i]
# for r in result:
# 	print(r)

# for i in range(1,15):
# 	for j in range(1,11):
# 		print("{0}*{1}={2}".format(i,j,i*j))


# tuples

# a=("tuple",32,3.2)
# print(a)
# print(type(a))

# convert tuple to string

# a=("s","a","r","i")
# " " .join(a)

# reverse of a string

# a=("dharmateja")
# print(a[::-1])

# a=(1,27,30,47,57)
# n=3
# a=a[:n]+a[n+1:]
# print(a)    

# a=[10,20,10,(20,30),40]
# count=0
# for n in a:
# 	if isinstance(n,tuple):
# 		break
# 	count +=1
# print(count)

# l1=[1,2,3,4]
# l2=[10,20,91,93]
# d={}
# if len(l1)==len(l1):
# 	for i in range(len(l1)):
# 		d[l1[i]]=l2[i]
# print(d)

