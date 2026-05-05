

"""def square(n):
    return n ** 2
res=square(5)
print(res)"""


"""
s=input()
res=""
for ch in s:
    if ch in res:
        print(ch)
    else:
        res+=ch"""

#remove duplicate character from string programming
"""s=input()
res=""
for ch in s:
    if ch in res:
        continue
    else:
        res+=ch
print(res)"""

#find letters and digits from a string:he23ll4
"""
s=input()
count=0
letters=""
digits=""
for ch in s:
    if '0'<=ch<='9':
        digits+=ch
    else:
        letters+=ch
print("letters","=",letters)
print("digits","=",digits)"""


#check if string contains only digits(input:1234 output:true)
"""s=input()
output=True
for ch in s:
    if not('1'<=ch<='9'):
         output=False
         break
print(output)
"""

#replace vowels with *
"""
s=input()
for ch in s:
    if ch in "aeiou":
        print("*",end="")
    else:
        print(ch,end="")"""

#count repeated one of a character
"""
s = input()
res=[]
for ch in s:
    if ch in res:
        continue
    count=0
    for c in s:
        if c==ch:
            count+=1
    if count>1:
     print(ch,">",count)
    res.append(ch)"""


#if hello input find l count
"""s=input()
ch=input()
count=0
for c in s:
    if c==ch:
       count+=1
print(count)"""

#REMOVE SPACE FROM H E LLO
"""s=input()
result=""
for ch in s:
    if ch!=" ":
        result+=ch
print(result)"""

#count digits
"""
s=input()
count=0
for ch in s:
    if ch.isdigit():
        count+=1
        print(ch)"""

#COUNT UPPER CASE
"""
s=input()
count=0
for ch in s:
   if 'A'<=ch<='Z':
       count+=1
print(count)
"""

#check palindrome
"""s=input().lower()
if s==s[::-1]:
    print("yes")
else:
    print("no")"""
#(or)
"""
#check palindrome
s = input().lower()

is_palindrome = True

for i in range(len(s)//2):
    if s[i] != s[len(s)-i-1]:
        is_palindrome = False
        break

if is_palindrome:
    print("YES")
else:
    print("NO")"""

