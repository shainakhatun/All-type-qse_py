

# a=[4,5,6,[8,9],5,2,9]
# i=0
# sum=0
# while i<len(a):
#     if type(a[i])!=list:
#         sum=sum+a[i]
#     else:
#         j=0
#         while j<len(a[i]):
#             sum=sum+a[i][j]
#             j=j+1
#     i=i+1
# print(sum)


    
# print(sum)



# a=[2,4,6,4,3,8]
# i=0
# max=0
# while i<len(a):
#     if a[i]>max:
#         max=a[i]
#     i=i+1
# print(max)

# a=[3,4,2,4,[46,78,5,8,[45,6,8,3,3,6,[4,5,7,3,[3,4,,4,6,43]]]]




# a=[2,4,3,2,3]
# b=a
# print(a)
# print(b)


# a=["shaina"]
# print(a*2)


# a=[0,0,3,4,2,0,5,5]
# i=0
# b=[]
# c=[]
# while i<len(a):
#     if a[i]!=0:
#         b.append(a[i])
#     else:
#         c.append(a[i])
#     i=i+1
# b.extend(c)
# print(b)

# a=[1,4,3,6,3,0,0,8,0,9,0]
# i=0
# while i<len(a):
#     if a[i]==0:
#         print(a[i],",",end="")
#     else:
#         print(a[i],",",end="")
    # i=i+1

# a.remove(2)
# print(a)


# Make a list according to the user....
# a=[]
# i=0
# b=int(input("entre:"))
# while i<b:
#     c=int(input("entre:"))
#     i=i+1
#     a.append(c)
# print(a)


# Trik....
# a=[8,4,6,7,3,8,9]
# b=a[::-1]
# print(b)
# n=7
# print(a[-n])

# a=["shaina","geetika","roopa"]
# b="shaina" not in a
# print(b)

# a=[8,4,6,7,3,8,9]
# b=a[::-1]
# print(b)

# NESTED LIST SUM WITH 3 LISTS....
# a=[1,2,3,[4,5,[6,7],8],9]
# i=0
# sum=0
# while i<len(a):
#     if type(a[i])!=list:
#         sum+=a[i]
#     else:
#         j=0
#         while j<len(a[i]):
#             if type(a[i][j])!=list:
#                 sum+=(a[i][j])
#             else:
#                 k=0
#                 while k<len(a[i][j]):
#                     sum+=(a[i][j][k])
#                     k+=1
#             j+=1
#     i=i+1
# print(sum)



# NESTED LIST SUM WITH 4 LISTS....
# a=[3,4,5,[5,4,3,[7,9,0,[8],],],]
# i=0
# sum=0
# while i<len(a):
#     if type (a[i])!=list:
#         sum=sum+a[i]
#     else:
#         j=0
#         while j<len(a[i]):
#             if type(a[i][j])!=list:
#                 sum=sum+a[i][j]
#             else:
#                 k=0
#                 while k<len(a[i][j]):
#                     if type(a[i][j][k])!=list:
#                         sum=sum+a[i][j][k]
#                     else:
#                         s=0
#                         while s<len(a[i][j][k]):
#                             sum+=(a[i][j][k][s])
#                             s+=1
#                     k=k+1
#             j=j+1
#     i=i+1
# print(sum)
                

# a=[203,305,606,305,201]
# i=0
# b=[]
# while i<len(a):
#     k=str(a[i])
#     g=""
#     c=""
#     j=0
#     while j<len(k):
#         if k[j]!="0":
#             g=g+k[j]
#         else:
#             c=c+k[j]
#         j=j+1
#     b.append(int(g+c))
#     i=i+1
# print(b)



# a=[204,608,405,304,304]
# i=0
# b=[]
# while i<len(a):
#     c=str(a[i])
#     s=""
#     r=""
#     j=0
#     while j<len(c):
#         if c[j]!="0":
#             s=s+c[j]
#         else:
#             r=r+c[j]
#         j=j+1
#     b.append(int(s+r))
#     i=i+1
# print(b)





# a=[203,508,608,404,402]
# i=0
# b=[]
# while i<len(a):
#     c=str(a[i])
#     d=""
#     e=""
#     j=0
#     while j<len(c):
#         if c[j]!="0":
#             d=d+c[j]
#         else:
#             e=e+c[j]
#         j=j+1
#     i=i+1
#     b.append(int(d+e))
# print(b)
        




# a=[2,4,0,9,0,9,0,8,0,7,0]
# i=0
# b=[]
# c=[]
# while i<len(a):
#     if a[i]!=0:
#         b.append(a[i])
#     else:
#         c.append(a[i])
#     i=i+1
# print(b+c)



# a=[2,4,6,3,6,3,6,3,4,35,7,8]
# i=0
# b=[]
# while i<len(a):
#     if a[i]not in b:
#         b.append(a[i])
#     i=i+1
# print(b)



# a=[2,0,4,0,5,0,7,0,7,0]
# i=0
# l=len(a)-1
# while i<len(a):
#     j=i+1
#     while j<len(a):
#         if a[i]==0:
#             a[i],a[j]=a[j],a[i]
#         j+=1
#     i+=1
# print(a)










# a=[1,4,3,5,2,3]
# p=6
# i=0
# b=[]
# while i<len(a):
#     j=1
#     while j<len(a):
#         if a[i]+a[j]==p:
#             b.append(a[i])
#         j=j+1
#     i=i+1
# print(b)






# a=[2,3,6,3,6]
# b=[3,5,3,7,9]
# i=0
# while i<len(a):
#     j=0
#     while j<len(b):
#         if len(a)==len(b):
#             b.extend(a)
#         j=j+1
#     i=i+1
# print(b)
# s=sorted(b)
# print(b)


# i=1
# for i in range 



# a=[2,4,3,6,3,6,6,3,2,4,8]
# i=0
# b=20
# while i<len(a):
#     j=i+2
#     if a[i]+a[j]==b:
#         j=j=1
#     i=i+1
# print(a[i])





# n=input("entre the name:")
# a="aeiou"
# i=0
# c=0
# while i<len(n):
#     if n[i] in a and c!=2:
#         c=c+1
#         print(n[i])
#     i=i+1


# Add all the numbers bigger than 5....

# a=[6,1,4,5,6,3,4,6,7]
# i=0
# sum=0
# while i<len(a):
#     if a[i]>5:
#         sum=sum+a[i]
#     i=i+1
# print(sum)


# Output should be like:[40,10,30,20,25,55,30]

# a=[8,2,6,4,5,11,6]
# i=0
# b=[]
# while i<len(a):
#     if a[i]in a:
#         c=a[i]*5
#         b.append(c)
#     i=i+1
# print(b)



#Remove all the zeros-Output should be like:[4,5,6,3]

# a=[400,500,600,300]
# i=0
# b=[]
# while i<len(a):
#     c=str(a[i])
#     j=0
#     while j<len(c[j]):
#         if c[j]!=0:
#             b.append(int(c[j]))
#             j=j+1
#     i=i+1
# print(b)




#Do sum of each element-Output should be like:[3,4,3,1,2]

# a=[1011,1111,1011,1000,1100]
# i=0
# b=[]
# while i<len(a):
#     c=str(a[i])
#     j=0
#     sum=0
#     s=""
#     while j<len(c):
#         if c[j]!="0":
#             s=s+c[j]
#             sum=sum+int(c[j])
         
#         j=j+1
#     b.append(sum)
#     i=i+1
# print(b)
    




#Except 1 add all the elements present in the list....

# a=[10101,234110,115780,11606]
# i=0
# b=[]
# sum=0
# while i<len(a):
#     b=str(a[i])
#     j=0
#     d=""
#     while j<len(b):
#         if b[j]!="1":
#             sum=sum+int(b[j])
           
#         j=j+1
#     b.append(sum)
#     i=i+1
# print(b)



# a=int(input("entre the no. of elements:"))
# i=0
# b=[]
# while i<a:
#     n=int(input("entre the nested list no."))
#     r=[]
#     j=0
#     while j<n:
#         s=int(input("entre the no:"))
#         r.append(s)
#         j=j+1
#     b.append(r)
#     i=i+1
# print(b)



# a=int(input("enter how many number you want:"))
# i=0
# b=[]
# while i<a:
#     n=int(input("enter your numbers:"))
#     if n%2==0:
#         print("even")
#         c=n%2==0
#         b.append(c)
# print(n,b)




# a=int(input("enter how many number you want:"))
# i=0
# even=[]
# while i<a:
#     n=int(input("enter your numbers:"))
#     if n%2==0:
#         even.append(n)
#     i+=1
# print(even)


# With the useing slicing....

# a=["c","i","v","i","c"]
# b=a[::-1]  
# print(b)
# if a==b:
#     print("palidrome")
# else:
#     print("not palindrome")


# Without useing slicing....

# a=input("entre the name:")
# b=len(a)
# i=b-1
# rev=""
# while i>=0:
#     rev=rev+a[i]
#     i-=1
# if a==rev:
#     print("palindrom")
# else:                           
#     print("not palindrome")


# a=int(input("entre the no:"))
# b=int(input("entre the no:"))
# i=1
# sum=0
# while i<=a:
#     sum=sum+b
#     i=i+1
# print(sum)



# a=["pune", 5 ,10 ,20, 25 ,"navgurukul"]
# i=0
# sum=0
# c=[]
# b=[]
# while i<len(a):
#     if type(a[i])==int:
#         sum=sum+a[i]
#         b.append(sum)
#     else:
#         c.append(a[i])
#     i=i+1
# print(b,c)




# Output:["my","name","shaina"]

a="my name is shaina"
i=0
b=""
c=""
d=""
e=""
while i<len(a):
    if a[i]:
        b.append(a[i])
    i=i+1
print(b)






















 

        
        










