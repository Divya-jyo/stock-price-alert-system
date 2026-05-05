#list concept this is and some problems solved

n=int(input())
arr=list(map(int,input().split()))
k = int(input())
result = []
min_diff = abs(arr[0] - k)
for i in arr:
    diff = abs(i - k)

    if diff < min_diff:
        min_diff = diff
        result = [i]      # reset list with new closer value

    elif diff == min_diff:
        result.append(i)  # add another equally close value
print(result)




#reverse
#for i in range(n-1, -1, -1):
 #print(arr[i], end=" ")


#for i in arr:
 #   if i>large:

  #      large=i

#print(large)




#total=0
#for i in arr:
# total+=i
#print(total)
#arr.sort()
#print(arr[2])

#count=0
#for i in arr:
 #   if i%2==0:
  #      count+=1
#print(count)


# remove duplicates
#newList=[]
#for i in arr:
#   if i not in newList:
#      newList.append(i)
#print(newList)


""""
second largest--

#minLarge=-999999
#large=arr[0]
#for i in arr:
#  if i>large:
#     minLarge=large
#     large=i
#  elif i>minLarge and i!=large:
#      minLarge=i
#print(minLarge)"""


"""
small=arr[0]
minSmall=0
for i in arr:
    if i<small:
        minSmall=small
        small=i

    elif i!=small and i<minSmall:
        minSmall=i
print(small)
print(minSmall)
"""



"""
count:=

visited = []
for i in range(n):
    if arr[i] in visited:
        continue

    count = 0
    for j in range(n):
        if arr[i] == arr[j]:
            count += 1

    print(arr[i], "→", count, "time(s)")
    visited.append(arr[i])"""



#finding closest equal distance numbers for k(compare)
"""
n=int(input())
arr=list(map(int,input().split()))
k = int(input())
result = []
min_diff = abs(arr[0] - k)
for i in arr:
    diff = abs(i - k)

    if diff < min_diff:
        min_diff = diff
        result = [i]      # reset list with new closer value

    elif diff == min_diff:
        result.append(i)  # add another equally close value
print(result)

"""