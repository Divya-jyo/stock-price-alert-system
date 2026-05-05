"""
#print 1 to N using recursion
def f(n):
    if n==0:
        return
    f(n-1)
    print(n)
f(3)"""
#print N to 1 using recursion
"""
def f(n):
    if n==0:
        return
    print(n)
    f(n-1)
f(3)"""

#sum of first n numbers
"""
def f(n):
    if n==0:
        return 0
    return n+ f(n-1)
f(3)
print(f(3))
"""
#factorial of a given number
"""
def f(n):
    if n==0:
        return 1
    return n*f(n-1)
print(f(5))
"""

#reverse an array using recursion
"""
def reverse(arr, left, right):
    if left >= right:
        return
    arr[left], arr[right] = arr[right], arr[left]
    reverse(arr, left + 1, right - 1)
arr = [1, 2, 3, 4, 5]
reverse(arr, 0, len(arr) - 2)
print(arr)"""
#finding string is palindrome or not like converting string into list
""""
def reverse(a,left,right):
    if left>=right:
        return
    a[left],a[right]=a[right],a[left]
    reverse(a, left+1, right - 1)
x=input()
a=list(x)
reverse(a,0,len(a)-1)
if a==list(x):
    print("palindrome")
else:
    print("not palindrome")"""

#(or)
"""
def is_palindrome(s, left, right):
    if left >= right:
        return True
    if s[left] != s[right]:
        return False
    return is_palindrome(s, left + 1, right - 1)
s=input()
print(is_palindrome(s, 0, len(s)-1))"""


