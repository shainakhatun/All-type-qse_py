#1.Duplicate remove....

# a=[4,6,3,6,2,4,9]
# i=0
# b=[]
# while i<len(a):
#     if a[i] not in b:
#         b.append(a[i])
#     i=i+1
# print(b)


#2.count....

# a=[4,5,6,7,8,9,4,6,8,7,7,9]
# i=0
# c=0
# while i<len(a):
#     c=c+1
#     i=i+1
# print(c)


#3.sum.... 

# a=[4,5,6,7,8,9,4,6,8,7,7,9]
# i=0
# sum=0
# while i<len(a):
#     sum=sum+(a[i])
#     i=i+1
# print(sum)


#4.Minimum....

# a=['456','692','448','967']
# i=0
# min=a[0]
# while i<len(a):
#     if a[i]<min:
#         min=a[i]
#     i=i+1
# print(min)
    

#5.Nested list sum....

# a=[4,[6,9],3,[4,5],9]
# i=0
# sum=0
# while i<len(a):
#     if type (a[i])==list:
#         j=0
#         while j<len(a[i]):
#             sum=sum+a[i][j]
#             j=j+1
#     else:
#         sum=sum+a[i]
#     i=i+1
# print(sum)


#6.sum....

# a=['456','692','448','967']
# i=0
# sum=0
# while i<len(a):
#     sum=sum+int(a[i])
#     i=i+1
# print(sum)


# 7.Sum with strings....

# a=['456','692','448','967']
# i=0
# sum=0
# b=[]
# while i<len(a[i]):
#     sum=sum+int(a[i])
#     # b.append(a[i])
#     i=i+1
# print(sum)
        
        
#8.duplicate remove....

# a=[3,6,5,4,3,4,5,6,3]
# i=0
# b=[]
# while i<len(a):
#     if a[i] not in b:
#         b.append (a[i])
#     i=i+1
# print(b)

    
#9.sum seperetly of each element number....
   
# a=['456','692','448','967']
# i=0
# while i<len(a):
#     j=0
#     sum=0
#     while j<len(a[i]):
#         sum=sum+int(a[i][j])
#         j=j+1
#     i=i+1
#     print(sum)


#10.Output dhould be like:[4,5,7,9,6,1]....

# a=[4,5,6,7,9,5,6,1]
# a.remove(a[2]) and (a[5])
# print(a)
# # i=0
# b=[]
# while i<len(a):
#     if a[i] not in b:
#         b.append(a[i])
#     else:
#         a.remove(a[2])
#     i=i+1
# print(b)


#11.Output:[4,5,6,7]....

# a=[4,5,6,7,9,5,6,1]
# i=0
# b=[]
# while i<len(a):
#     if i not in b:
#         b.append(a[i])
#     i+=1
# print(b)


# 12.Find the present students number....

# a=int(input("entre the no. of toatal students:"))
# b=int(input("entre the no. of absent students:"))
# if a>b:
#     # print(a-b)
#     c=a-b
#     print(c)     
                    


#13.Output:[11,17,23,2]....(not done)

# a=[11,15,17,18,21,23,22,2]
# i=1
# b=[]
# while i<len(a):
#     j=1
#     c=0
#     while j<len(a):
#         if a[i]%a[j]==0:
#             c+=1
#         j=j+1
#     i=i+1
#     if c==2:
#         b.append(a[i])
# print(b)


#14.Find the even numbers till hundread....(not done)

# i=1
# while i<=100:
#     j=1
#     c=0
#     while j<=(i):
#         if i%j==0:
#             c+=1
#         j+=1
#     i+=1
#     if c==2:
#         print(i)


#15.Take a user input and it should repeate that times and at the last append in one 
# list:

# n=int(input("entre the no:"))
# i=1
# b=[]
# while i<=n:
#     a=int(input("entre the no:"))
#     b.append(a)
#     i=i+1
# print(b)   


#16.Output should be like:["my","name","shaina"]....

# s="my5 name10 is shaina20"
# d=[]
# for i in s:
#     if not i.isdigit(): 
#         d.append(i)
# r=''.join(d)
# print(r)

# a="my5 name10 shaina20"
# i=0
# b=[]
# c=""
# for i in a:
#     if i==" ":
#         b.append(c)
#         c=""
#     else:
#         c+=i
# b.append(c)
# print(b)





# f=b
# s=0
# r=[]
# while s<len(f):
#     if f[s]!=int:
#         r.append(f[s])
#     s=s+1
# print(r)








# a=["m1y","na@me","is6","shaina1@"]
# i=0
# b=[]
# while i<len(a):
#     j=0
#     s=" "
#     while j<len(a[i]):
#         if a[i][j]>="a" and a[i][j]<="z":
#             s=s+a[i][j]
#         j=j+1
#     b.append(s)
#     i=i+1
# print(b)




    
# a="12hours"
# b=str(12*2)+str("hour")
# print(b)


# import datetime
# now=datetime.datetime.now()
# print("current date and time:")
# print(now.strftime("%y-%m-%d| %H:%M:%S:"))























