#1.Example of : Append

# a=[5,7,9]
# a.append(17)
# print(a)


#2.Example of: Insert

# a=[5,7,9]
# a.insert(2,7)
# print(a)


#3.Print the elements with their indext no....

# a=[2,3,7,9,4]
# i=0
# while i<len(a):
#     print(i,":",a[i])
#     i+=1


#4.Output:3,9,4....

# a=[2,3,7,9,4]
# i=0
# while i<len(a):
#     if a[i]==3 or a[i]==9 or a[i]==4:
#         print(a[i],end=",")
#     i=i+1



#5.Output should be:n

# a="teena"
# i=3
# while i<len(a):
#     print(a[i])
#     i=i+2  


#6.Output should be:
# 10:400
# 20:300
# 30:200
# 40:100

# a=[10,20,30,40]
# b=[100,200,300,400]
# i=0
# c=0
# while i<len(a):
#     c=c+1
#     print(a[i],b[-c])
#     i=i+1


#7.Output:20j punenavgurukul 26.2513.0....

# a="2.5"
# b="2+2j"
# c="navgurukul"
# d="5+5j"
# e="pune"
# f="10.5"
# _a="10"
# b=complex(b)
# d=complex(d)
# b=b*d
# e=e+c
# f=float(f)
# a=float(a)
# x=str(f*a)
# z=str(a+f)
# print(b,e,x+z)


#8.Output:13

# a=2.5
# b=10.5
# c=int(a+b)
# print(c)


#9.Output:20.0(while multiplying .5 will not considerd)

# a=2
# b=10.5
# print(a*b)


#10.Output:[12,12.2,2]

# a=[12,12.2,"teena",2]
# a.pop(2)
# print(a)


#11.Output:0 shaina
        #  1 8
        #  2 8

# a=["shaina",8,8,]
# i=0
# while i<len(a):
#     print(i,a[i])
#     i=i+1


#12.Output:6

# a=[1,2,[4,5,6,]]
# print(a[2][2])


#13.maximum number:9     

# a=[3,6,7,4,5,9,0]
# i=0
# max=0
# while i<len(a):
#     if a[i]>max:
#         max=a[i]
#     i=i+1
# print(max)


#14.Output:[0,9,1,3,2,7,5,2]

# k=[2,5,7,2,3,1,9,0]
# k.reverse()
# print(k)


#15.Reverse....

# k=[0,9,1,3,2,7,5,2]
# k.reverse()
# print(k)


#16.Find the all odd and even no. from the user input....

# a=int(input("entre the no."))
# i=1
# b=[]
# b1=[]
# while i<a:
#     if i%2==0:
#         b.append(i)
#     else:
#         b1.append(i)
#     i=i+1
# print("even no:",b)
# print("odd no:",b1)


#17.Find all the even no. from the user input....

# n=int(input("enter the num : "))
# i=1
# while i<=n:
#     if i%2==0:
#         print(i)
#     i+=1



#18.Take one user input and it should ask for user input upto the no.... 
# then it should be printed in one list:

# n=int(input("entre the no:"))
# i=1
# b=[]
# while i<=n:
#      a=int(input("entre the no:"))
#      b.append(a)
#      i=i+1
# print(b)



#19.Print the tables according to user input:....(not done)

# n=int(input("entre the no:"))
# i=1
# while i<=10:
#     j=0
#     while j<n:
#         print(i*j)
#         j=j+1

#     i=i+1


#20.Find the index no. of the following list....

# a=["carrot","reddish","flour"]
# i=0
# while i<len(a):
#     print(i,a[i])
#     i+=1


#21.Take a list and do sum of those no. which is greater than the user input....

# a=[3,5,26,8,3,8,9,5,8,4]
# n=int(input("entre the no:"))
# i=0
# sum=0
# while i<len(a):
#         if a[i]>n:
#                 sum=sum+a[i]
#         i=i+1
# print(sum)


#22.Without useing sort method sort the list....
#(Assending order)

# a=[4,6,3,6,2,8,6,9,1,0,2]
# i=0
# while i<len(a):
#         j=i
#         while j<len(a):
#                 if a[i]>a[j]:
#                         s=a[i]
#                         a[i]=a[j]
#                         a[j]=s
#                 j=j+1
#         i=i+1
# print(a)      


# (Disanding order)

# a=[4,6,3,6,2,8,6,9,1,0,2]
# i=0
# while i<len(a):
#         j=0
#         while j<len(a):
#                 if a[i]>a[j]:
#                         s=a[i]
#                         a[i]=a[j]
#                         a[j]=s
#                 j=j+1
#         i=i+1
# print(a)      





