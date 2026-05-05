"""
class Solution:
    def whichWeekDay(self, day):
        match day:
            case 1:
                print("Monday")
            case 2:
                print("Tuesday")
            case 3:
                print("Wednesday")
            case 4:
                print("Thursday")
            case 5:
                print("Friday")
            case 6:
                print("Saturday")
            case 7:
                print("Sunday")
            case _:
                print("Invalid")


s=Solution()
num=int(input())
s.whichWeekDay(num)"""


"""
i=int(input())
m=int(input())
total=0
for i in range(i,m+1):
    total+=i
print(total)"""
"""
#print first 20numbers by adding them
num = 1
while True:
    if num>20:
        break
    print(num)
    num += 1"""
#Take numbers from user Stop when you encounter 0 Print the sum of numbers before 0
"""
arr=map(int,input().split())
total=0
for i in arr:
    if i==0:
        break
    total+=i
print(total)"""

"""
n=int(input())
total=0
for i in range(3,n+1,3):
    if(i%3==0):
        total+=i
print(total)"""
#Take numbers from user Stop when you encounter 0 Print the sum of numbers before 0 take user input one by one
"""
total = 0
while True:
    num = int(input())
    if num == 0:
        break
    total += num
print(total)"""
"""
num=1
total=0
while total<=20:
    total+=num
    num+=1
print(num-1)"""
# reverse array
"""
class Solution:
    def reverse(self, arr: list) -> None:
        arr.reverse()
        print(arr)
s=Solution()
n=int(input())
arr=list(map(int,input().split()))
s.reverse(arr)"""
#(or)
"""
arr = [1, 2, 3, 4, 5]
left = 0
right = len(arr) - 1
while left < right:
    arr[left], arr[right] = arr[right], arr[left]
    left += 1
    right -= 1
print(arr)"""
#given string is palindrome or not
"""
arr="hello"
left=0
right=len(arr)-1
is_palindrome=True
while left < right:
    if arr[left]!=arr[right]:
        is_palindrome=False
        break
    left += 1
    right -= 1
print(is_palindrome)"""