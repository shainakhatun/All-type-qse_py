# 1.Output:["t","a","n","u","j","a"]....

# a=["tanuja"]
# n=input("entre the name:")
# i=0
# b=[]
# while i<len(n):
#     j=0
#     while j<len(n[i]):
#         b.append(n[i][j])
#         j=j+1
#     i=i+1
# print(b)


# 2.Output:18....

# a=["2","5","7","4"]
# i=0
# sum=0
# while i<len(a):
#     sum=sum+int(a[i])
#     i=i+1
# print(sum)


# 3.Output:odd indexing and even indexing....

# a=[2,5,3,4,9,8,7]
# i=0
# b=[]
# b1=[]
# while i<len(a):
#     if a[i]%2!=0:
#         b1.append(a[i])
#     else:
#         b.append(a[i])
#     i=i+1
# print(i,b1)
# print(i,b)


# 4.Output:["b",5,"l",10,"a",15,"c",20,"k",25]....

# a=[5,10,15,20,25]
# c="black"
# b=[]
# i=0
# while i<len(a):
#     s=(a[i],c[i])
#     b.append(c[i])
#     b.append(a[i])
#     i=i+1
# print(b)


# 5.Do sum of all user inputs....

# a=int(input("entre the 1st month bill:"))
# b=int(input("entre the 2nd month bill:"))
# c=int(input("entre the 3rd month bill:"))
# d=int(input("entre the 4th month bill:"))
# e=int(input("entre the 5th month bill:"))
# f=a+b+c+d+e
# print(f)


#6.Take a user input and insert the table of 5 after each letter....

# a=input("enter the name:")
# # l=[a]
# # print(l)
# k=5
# i=0
# list1=[]
# while i<len(a):
#     j=0
#     while j<len(a[i]):
#         list1.append(a[i][j])
#         list1.append(k)
#         j=j+1
#         k=k+5
#     i=i+1
# print(list1)


#7.Add the zero's at the last....

# a=[3,4,6,0,8,0,8,0,7,0,7,0,7,0]
# i=0
# b=[]
# c=[]
# while i<len(a):
#     if a[i]==0:
#         b.append(a[i])
#     else:
#         c.append(a[i])
#     i=i+1
# # print(b)
# # print(c)
# c.extend(b)
# print(c)


#8.Find which are the pallindroms elements....

# a=["tannu","mom","shaina","shivani","nitin","civic"]
# i=0
# while i<len(a):
#     j=0
#     k=-1
#     l=""
#     while j<len(a[i]):
#         l=l+a[i][k]
#         k=k-1
#         j=j+1
#     if l==a[i]:
#         print("palidrom",a[i],i)
#     i=i+1


#9.Find whether the user input is prime no. or not....

# a=int(input("entre the no:"))
# i=1
# c=0
# while i<=a:
#     if a%i==0:
#         c=c+1
#     i=i+1
# if c==2:
#     print("p")
# else:
#     print("n")



#10.Remove all the duplicates and find their count....

# a=[1,2,3,2,1,4,5,4]
# i=0
# c=0
# b=[]
# while i<len(a):
#     if a[i] not in b:
#         b.append(a[i])
#         c=c+1
#     i=i+1
# print(c,b)



a=int(input("entre the no:"))
b=int(input("entre the no:"))
c=int(input("entre the no:"))
if a>b and a<c or a<b and a>c:
    print(a,"second max")
elif b>a and b<c or b<a and b>c:
    print(b,"second max")
else:
    print(c,"second max")




