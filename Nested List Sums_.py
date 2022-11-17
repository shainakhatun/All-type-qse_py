#1.Nested LIst Sum....

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


#2.NESTED LIST SUM WITH 3 LISTS....

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


#3.NESTED LIST SUM WITH 4 LISTS....

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
                

# 4.NESTED LIST SUM WITH 5 LIST....

# a=[2,4,1,8,9,6,[6,8,7,[7,4,[8,8,[4],],],],]
# i=0
# sum=0
# while i<len(a):
#     if type (a[i])!=list:
#         sum=sum+a[i]
#     else:
#         j=0
#         while j<len(a[i]):
#             if type (a[i][j])!=list:
#                 sum+=a[i][j]
#             else:
#                 k=0
#                 while k<len(a[i][j]):
#                     if type (a[i][j][k])!=list:
#                         sum=sum+a[i][j][k]
#                     else:
#                         s=0
#                         while s<len(a[i][j][k]):
#                             if type (a[i][j][k][s])!=list:
#                                 sum+= a[i][j][k][s]
#                             else:
#                                 r=0
#                                 while r<len(a[i][j][k][s]):
#                                     if type(a[i][j][k][s][r])==list:
#                                         sum=sum+a[i][j][k][s][r]
#                                     r=r+1
#                             s=s+1
#                     k=k+1
#             j=j+1
#     i=i+1
# print(sum)








