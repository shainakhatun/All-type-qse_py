# What is list?
# List is collection of different data types in a single Variable with square brakets....

# Features of list....
# We can store more than one data types in a single variable.
# It is mutable we can change the elements of the list when ever we want.
# It is ordered because each elements have spacefic index value.
# When ever we want we can make changes in the list and modify it.
# We can create a list with square brakets.

# Difference between append and extend.

# APPEND                                    EXTEND

#1.Append can add a single element at the   1.Extend can add two lists together.
# last if the list.
#2.Length increase by one elements.         2.Length increse by number of elements.


# Pop                                          Remove

#1.Pop remove the elements with the help of  1.Remove removes the whole list's elements
# indexing.                                   and give a empty list as output.
#2.By default pop remove the last elements   2.Remove also remove's the element 
# if we did not mention indext number.         which we mwntion.


# Indexing                                     Slicing

#1.Indexing is used to obtain individual       1.Slicing is used to obtain a sequence 
#element.                                        of elements.
#2.Indexing can be be done in Python Sequences  2.Slicing can be be done in Python Sequences
#types like list, string, tuple, range objects.  types like list, string, tuple, range objects.


# List                                            Tuple
#1.Lists are denoted by the square brackets.       1.tuples are denoted as parenthesis.
#2.The list is dynami.                             2.The tuple has static characteristics.
# 3.lists can be modified when ever we want any    3.tuples cannot be modified. 
# changes we can make changes.                     4.Tuple is faster than the list because
#4.List is slower than tuple.                        of static in nature.


# List Methods....
# There are 19 method in list they are....

# 1.Length-:It helps to find the total element in a list.
# 2.Insert-:It helps to insert an element in a list with the help of indexing.
# 3.Append-:It helps to add a single element at the last of a list.
# 4.Extend-:It helps to add two lists together.
# 5.Remove-:It helps to remove an element with other element.
# 6.Pop-:It helps to remove an element with the help of indexing by default it remove's last element.
# 7.Del-:It helps to delete with the help of slicing, indexing and can delete the whole list.
# 8.Clear-:It helps to clear the whole list and give output as an empty list.
# 9.Sort-:It helps to arrange the elements in assending order and alphaberts in sequance.
# 10.Sort desending-:It helps to arrange the elements in desending order.
# 11.Reverse-:It helps to reverse the elements present in a list.
# 12.Coppy-:It hepls to coppy the elements same as.
# 13.Join tow lists-:It helps to join two list together with the help of extend.
# 14.Min-:It helps to find the minimum number present in a list.
# 15.Max-:It helps to find the maximum number present in a list.
# 16.Sum-:It helps to find the sum of all the elements present in a list.
# 17.Count-:It helps to count the elements present in a list.
# 18.Slicing-:It helps to obtain a sequenc of elements from a list.
# 19.Index-:It helps to obtain individual element from a list.
# 20.Sorted-:It helps to returns a sorted list of the specified iterable object. 


# a=[1,2,3,4,5,6]
# # a=[2,4,52,4,2,4]
# print(tuple(reversed(a)))
# a.reverse()
# print(a)

# a=[1,2,3,4,5,6]
# a.copy()
# print(a)


# Questions....

# 1.Dublicate remove....
# a=[2,3,4,5,2,5,4,6,4,6,4,7,5,7,8,9]
# i=0
# b=[]
# while i<len(a):
#     if a[i] not in b:
#         b.append(a[i])
#     i=i+1
# print(b)

#2.Add all the zeros at the last oif the list....
# a=[2,3,7,10,9,0,7,0,7,0,3,40,3,5,0]
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

#3.Do sum of all elements present in the list....
# a=[3,5,67,34,2,3,4,5,4,5,56,6,8]
# i=0
# sum=0
# while i<len(a):
#     sum=sum+a[i]
#     i=i+1
# print(sum)

# Find second max from the list....
# a=[3,5,67,34,2,3,4,5,4,5,56,6,8]
# i=0
# max=0
# secondmax=0
# while i<len(a):
#     if a[i]>max:
#         secondmax=max
#         max=a[i]
#     i=i+1
# print(secondmax)

# Find third max from the list....
a=[3,5,2,4,8,67,6]
i=0
max=0
thirdmax=0
while i<len(a):
    if a[i]>max:
        thirdmax=max
        max=a[i]
    i=i+1
print(thirdmax)


 








