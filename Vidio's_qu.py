#1.small calculater(only for sum)....

# (1)
# n=int(input('entre rhe no:'))
# s=int(input('entre the no:'))
# print(n+s)

# (2)
# print('entre the first no:')
# n1=input()
# print('entre the second no:')
# n2=input()
# print("sum of these no:",int(n1)+int(n2))




#2.Arrange the list elements in assending order....
# Output:[12,15,18,19,21]

# With sort method....
# a=[19,12,18,21,15]
# a.sort()
# print(a)


# By using bubble sort method....

# a=[19,12,18,21,15]
# i=0
# while i<len(a):
#     j=0
#     while j<len(a):
#         if a[i]<a[j]:
#             a[i],a[j]=a[j],a[i]
#         j=j+1
#     i=i+1
# print(a)


                                   
#3.Find the duplicate values....

# a=[1,1,2,3,4,5,2,3,4]
# i=0
# b=[]
# while i<len(a):
#     j=i+1
#     while j<len(a):
#         if a[i]==a[j]:
#             b.append(a[i])
#         j=j+1
#     i=i+1
# print(b)



#4.Do sum of all elements....

# a=[12,15,103,151,157]
# i=0
# sum=0
# while i<len(a):
#         sum=sum+a[i]
#         i=i+1
# print(sum)
    

#5.Do sum of each elements separately....

# a=[15, 81, 11, 234]
# i=0
# b=[]
# while i<len(a):
#     n=str(a[i])
#     j=0
#     sum=0
#     while j<len(n):
#         sum+=int(n[j])
#         j=j+1
#     b.append(sum)
#     i=i+1
# print(b)



# Output:[15,105,105,5,505,11]

a=[150,1050,10500,500,5050,1100]
i=0
b=[]
while i<len(a):
    j=0
    while j<len(a):
        if a[i]!=0:
            b.append(a[i])
        i=i+1
print(b)


# a=[150,1050,10500,500,5050,1100]
# a.reverse()
# print(a)


