
#reverse tuple
"""t=(1, 2,3, 4, 5)
print(t[::-1])"""

#Convert tuple to list and modify
"""
t=("apple","banana","orange")
y=list(t)
y[1]="melon"
h=tuple(y)
print(h)"""

#count all elements using tuple/list do not allow duplicates
"""
t = tuple(map(int, input().split()))
seen = ()
for i in t:
    if i not in seen:
        print(i, "=", t.count(i))
        seen += (i,)"""

#count all elements using tuple/list allows duplicates

"""t=tuple(map(int,input().split()))
for i in t:
    if t.count(i)>0:
        print(i,"=",t.count(i))"""


#count repeated element in a tuple
"""
t = tuple(map(int, input().split()))
x = int(input())

count = t.count(x)
print(count)"""


#thistuple = ("apple", "banana", "cherry")
#print(thistuple)


#length of the tuple
"""
t=int(input())
arr=tuple(map(int,input().split()))
print(len(arr))"""

# skipping middle elements
"""
t=int(input())
arr=tuple(map(int,input().split()))
print(arr[1::2])"""