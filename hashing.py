#this is brute force approch its time complexity is O(n*2)
"""
def count_frequency(nums):
    result = []

    for i in range(len(nums)):
        count = 0
        for j in range(len(nums)):
            if nums[i] == nums[j]:
                count += 1

        # avoid duplicates
        if [nums[i], count] not in result:
            result.append([nums[i], count])

    return result"""
#this is done using dictionaries "Counting Frequencies of Array Elements"
"""
def count_frequency(nums):
    freq = {}

    for num in nums:
        if num in freq:
            freq[num] += 1
        else:
            freq[num] = 1
# freq[num]=freq.get(num,0)+1

    result = []
    for key in freq:
        result.append([key, freq[key]])

    return result
nums=list(map(int,input().split()))
print(count_frequency(nums))
"""
#Highest Occurring Element in an Array

def count_occurrences(nums):
    occurrences = {}

    for num in nums:
        if num in occurrences:
            occurrences[num] += 1
        else:
            occurrences[num] = 1

    max_count = 0
    answer = None

    for key, value in occurrences.items():
        if value > max_count:
            max_count = value
            answer = key

    return answer
nums = list(map(int,input().split()))
print(count_occurrences(nums))

def is_anagram(s1, s2):
    if len(s1) != len(s2):
        return False

    freq = {}

    for ch in s1:
        freq[ch] = freq.get(ch, 0) + 1

    for ch in s2:
        if ch not in freq:
            return False
        freq[ch] -= 1

    for value in freq.values():
        if value != 0:
            return False

    return True


# Example
s1 = "listen"
s2 = "silent"
print(is_anagram(s1, s2))  # True



