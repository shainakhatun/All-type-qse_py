#1.Output:[1,"S",2,"h",3,"a",4,"i",5,"n",6,"a"]....

# a=[1,2,3,4,5,6]
# b="Shaina"
# i=0
# s=[]
# while i<len(a):
#    n=(a[i]),b[i]
#    s.append(a[i])
#    s.append(b[i])
#    i=i+1
# print(s)   


#2.Sum of all elements:....

# a=[1,2,3,4,5,6]
# i=0
# sum=0
# while i<len(a):
#     sum=sum+a[i]
#     i=i+1
# print(sum)


#3.Output:[3,6,8,3,6]....

# a=[12,15,17,21,51,11]
# i=0
# s=[]
# while i<len(a):
#     b=a[i]%10
#     d=a[i]//10
#     n=b+d
#     s.append(n)
#     i=i+1
# print(s)    
    

#4.Add the zero at the last of the element....
# Output:[120,130,140,150]

# a=[102,103,104,105]
# i=0
# c=[]
# while i<len(a):
#     k=str(a[i])
#     g=""
#     h=""
#     j=0
#     while j<len(k):
#         if k[j]!="0":
#             g=g+k[j]
#         else:
#             h=h+k[j]            
#         j=j+1
#     c.append(int(g+h))
        
#     i=i+1
# print(c)


#5.Output:Even length [tanu,shaina]....

# a=["tanu","khose","shaina","shivani"]
# i=0
# while i<len(a):
#     if len(a[i])%2==0:
#         print(i,":","even =",a[i])
#     # else:
#     #     print(i,"odd = ",a[i])
#     i=i+1


#6.Output:len(3)-[richa ,muskan,tanu]....

# a=["Ri$ch@a","m9u$s*k@an","t@a6n4u"]
# i=0
# list1=[]
# while i<len(a):
#     j=0
#     str=""
#     while j<len(a[i]):
#         if (a[i][j]>="a" and a[i][j]<="z" ) or (a[i][j]>="A" and a[i][j]<="Z"):
#             str+=(a[i][j])
#         j+=1
#     list1.append(str)
#     i+=1
# print(i,":",list1)
        

#7.Find whether the user input is alpha. or not....

# n=input("entre the alpha: ")
# if n>= "a" and n<="z" or n>="A" and n<="Z":
#     print(n,":","alpha")
# else:
#     print(n,":","not alpha")


#8.Find whether the eliments is present in second list or not. If not then print them....
# Output:[1,34,9]

# a=[1,2,34,6,7,4,9]
# b=[3,5,6,2,4,8,7,8]
# i=0
# c=[]
# while i<len(a):
#         if a[i] not in b:
#             c.append(a[i])
#         i=i+1       
# print(c)


#9.Find the vowels....
# Output:["a","o","i","e"]

# a=["tanu","khose","shivani","shaina"]
# c=["a","e","i","o","u"]
# i=0
# b=[]
# while i<len(a):
#     j=0 
#     while j<len(a[i]):
#         if a[i][j]in c:
#             b.append(a[i][j])
#         j=j+1
#     i=i+1
# print(b)


# 10.Splite each alphaword in separate strings....
# Output:["t","a","n","u","j","a"]

# a=["tanuja"]
# b=[]
# i=0
# while i<len(a):
#     j=0
#     while j<len(a[i]):
#         b.append(a[i][j])
#         j=j+1
#     i=i+1
# print(b)


                    