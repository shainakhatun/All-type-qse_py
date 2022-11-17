#1.Print all the elements present in the list....

# a=[4,8,2,1,9,3]
# i=0
# while i<=len(a):
#     print(a[i])
#     i=i+1


#2.Find the avg. and sum of the list....

# a=[1,2,3,4,9,6,7]
# i=0
# sum=0
# count=0
# avg=0
# while i<len(a):
#     sum=sum+a[i]
#     count=count+1
#     avg=sum//count
#     i=i+1
# print("Avg",":",avg)
# print("sum",":",sum) 


#3.According to user input print a list....

# a=int(input("entre the list no.:"))
# i=0
# b=[]
# while i<a:
#     c=int(input("entre the no.:"))
#     b.append(c)
#     i=i+1
# print(b)

    

#4.Output:[3,4,7,9,1,6]....

# a=[3,4,7,9,1,5,6,3,5,4]
# i=0
# b=[]
# while i<len(a):
#     if a[i] not in b:
#         b.append(a[i])
#     i=i+1
# print(b)        
    

#5.Output:[1,6,5,4]....

# a=[1,2,3,3,2,6,5,4]
# i=0
# v=[]
# while i<len(a):
#     if a[i]==1 or a[i]==6 or a[i]==4 or a[i]==5:
#         v.append(a[i])   
#     i=i+1
# print(v)        


#6.Find who is karorpati,lakhpati,and dilvale....

# a= [3000, 600000, 324990909, 90990900, 30000, 5600000, 690909090, 31010101, 532010, 510, 4100]
# i=0
# c=0
# c1=0
# c2=0
# while i<len(a):
#     if a[i] >= 10000000:
#         c=c+1
#     elif a[i] >=100000:
#         c1=c1+1
#     else:
#         c2=c2+1
#     i=i+1
# print(c,"karorpati")   
# print(c1,"lakhpati")
# print(c2,"dilbale")


