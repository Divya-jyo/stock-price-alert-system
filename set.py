#Find missing numbers using set
"""
arr = [1, 2, 4, 6]
full_set = set(range(1, max(arr) + 1))
arr_set = set(arr)
missing = full_set - arr_set
print(missing)"""



#Check if two lists are equal (ignore order)
"""
a=[1,2,3]
b=[3,2,1]
if set(a) == set(b):
    print("True")"""

#Find unique elements from both sets (no common)
"""a={1,2,3}
b={2,3,4}
y=a.symmetric_difference(b)
print(y)"""

#Check if two lists have any common element
"""
a = [1, 2, 3]
b = [5, 6, 3]

if set(a) & set(b):
    print("Yes")
else:
    print("No")"""

#Find elements only in first set
"""
a=set(map(int,input().split()))
b=set(map(int,input().split()))
set3=a.difference(b)
print(set3)"""

#Find common elements
"""a=set(map(int,input().split()))
b=set(map(int,input().split()))
set3=a.intersection(b)
print(set3)"""

#length of this list elements using set
"""
arr=[1,2,2,3,4,4]
e=set(arr)
print(len(e))"""
