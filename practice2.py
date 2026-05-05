#reverse a number
"""
n=int(input())
rev=0
while n>0:
    digit=n%10
    rev=rev*10+digit
    n=n//10
print(rev)"""
#find gcd using loop
"""
n1=int(input())
n2=int(input())
gcd=1
for i in range(1,min(n1,n2)+1):
    if n1%i==0 and n2%i==0:
        gcd=i
print(gcd)"""
#(or)
"""
n1=int(input())
n2=int(input())
while n2!=0:
    remainder=n1%n2
    n1=n2
    n2=remainder
print(n1)"""

#find lcm
"""
def gcd(a, b):
    while b != 0:
        remainder = a % b
        a = b
        b = remainder
    return a

def lcm(a, b):
    return (a * b) // gcd(a, b)

# Example
n1 = 12
n2 = 30

print("LCM =", lcm(n1, n2))"""
#find ams number or not
"""
def digits(a):
 if a==0:
    return 1
 count=0
 while a>0:
    count+=1
    a=a//10
 return count
def number(a):
 x=a
 total=0
 n=digits(a)
 while x>0:
    temp=x%10
    total=total+(temp**n)
    x=x//10
 if total==a:
    return "armstrong"
 else:
    return "not armstrong"

a=int(input())
print(number(a))"""




#LEVEL 1

"""
#count digits
n = int(input())
n = abs(n)
if n == 0:
    print(1)
else:
    count = 0
    while n > 0:
        count += 1
        n //= 10
    print(count)"""
#reverse number
"""
n=int(input())
rev=0
while n>0:
    x=n%10
    rev=rev*10+x
    n=n//10
print(rev)"""
#sum of digits
"""
n=int(input())
n=abs(n)
if n==0:
   print(0)
else:
   total=0
   while n>0:
      digit=n%10
      total=total+digit
      n=n//10
   print(total)"""
"""
#palindrome
n=int(input())
x=0
d=n
while d>0:
    x=x*10+d%10
    d=d//10(reassignment happens here)
if n==x:
    print("palindrome")
else:
    print("not palindrome")
"""
#number is prime or not
"""
n = int(input())

if n <= 1:
    print("Not Prime")
else:
    is_prime = True
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            is_prime = False
            break

    if is_prime:
        print("Prime")
    else:
        print("Not Prime")"""
#print all divisors
"""
n=int(input())
for i in range(1,n+1):
    if n%i==0:
        print(i,end=" ")"""

#fibonacci numbers program
"""
n = int(input())
a = 0
b = 1
for i in range(n):
    print(a, end=" ")
    a, b = b, a + b"""



