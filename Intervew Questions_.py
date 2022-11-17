#1.Add all zero's at last....

# a=[1,2,0,4,0,5,0]
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

# a=[1,0,3,0,4,4,0,3,2,0]
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

#2.Finde which one's length is big....

# a=["aa","aaa","aaaa","aaaaa","cccccc","sssss"]
# i=0
# max=0
# while i<len(a):
#     if len(a[i])>=max:
#         max=len(a[i])
#         c=a[i]
#     i=i+1
# print(max,":",c)

#3.Remove all the duplicate....

# a=[1,3,2,3,1,4,4,5,6,7,2,2,3]
# i=0
# b=[]
# while i<len(a):
#     if a[i] not in b:
#         b.append(a[i])
#     i=i+1
# print(b)

#4.Remove all the zero's and do sum of all....

# a=[10101,234110,115780,11606]
# i=0
# while i<len(a):
#     sum=0
#     b=str(a[i])
#     j=0
#     d=" "
#     while j<len(b):
#         if (b[j])!=str(1):
#             d=d+(b[j])
#             sum=sum+(int(b[j]))
#         j+=1
#     print([sum],end=" ")
#     i=i+1
    
    
#5.Remove all the duplicates and do sum....

# a=[4, 6, 4, 3, 3, 4, 3, 4, 6, 6]
# i=0
# b=[]
# sum=0
# while i<len(a):
#     if a[i] not in b:
#         b.append(a[i])
#         sum=sum+a[i]
#     i=i+1
# print(b,":",sum)

    
#6.Take the no. which are more then two times and do sum....

# a=[4, 6, 1, 2, 4, 1, 3, 4, 3, 1, 4, 6]
# i=0
# b=[]
# k=2
# sum=0
# while i<len(a):
#     j=0
#     count=0
#     while j<len(a):
#         if a[i]==a[j]:
#             count=count+1
#         j=j+1
#     if count>k and a[i] not in b:
#         b.append(a[i])
#         sum=sum+a[i]
#     i=i+1
# print(b,sum)       


    
    
    
    
    
    
    
    
    
    
    
    
    
    