#CHECK PALINDROME OR NOT USING FUNCTION
"""
s=input()
if s==s[::-1]:
      print(True)
else:
    print(False)"""

#reverse string using function
"""
def reverse_string(s):
    rev = ""
    for ch in s:
      rev = ch + rev
    return rev
s = input()
print(reverse_string(s))"""

#vowel count using functions
"""
def vowel_count(s):
  count=0
  for i in s:
    if i in "aeiou":
        count+=1
  return count
s=input()
print(vowel_count(s))"""

#return factorial of 5
"""
def factorial(n):
    result=1
    for i in range(1, n+1):
        result*=i
    return result
n=int(input())
print(factorial(n))"""

#print total count
"""
def total_count(arr):
   total=0
   for i in arr:
       total+=I
   return total
n=int(input())
arr=list(map(int,input().split()))
print(total_count(arr))"""


#return total count
"""
def digits(arr):
 count=0
 for i in arr:
    if i in arr:
        count+=1
 return count
n = int(input())
arr = list(map(int,input().split()))
print(digits(arr))"""


#return maximum of two numbers
"""def find_max(arr):
   maximum=arr[0]
   for i in arr:
        if i>maximum:
            maximum=I
   return maximum
   n = int(input())
   arr = list(map(int,input().split()))
   print(find_max(arr))"""

#check number positive or negative
"""def check(n):
    if n > 0:
        return "Positive"
    elif n < 0:
        return "Negative"
    else:
        return "Zero"

#n = int(input())
res = check(7)
print(res)"""