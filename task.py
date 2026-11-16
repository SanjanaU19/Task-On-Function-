# count frequency of word

text = "java python java programming python java"
freq = {}

for word in text.split():
    if word in freq:
        freq[word] += 1
    else:
        freq[word] = 1
print(freq)


# find duplicates numbers from list 

nums = [10,20,30,10,40,20,10]
res = []

for num in nums:
    if nums.count(num) > 1 and num not in res:
        res.append(num)
print(res)

# second largest number from the list 
nums = [10,20,30,10,40,20,10]

largest = float('-inf')
second_largest = float('-inf')

for num in nums:
    if num > largest:
        second_largest = largest
        largest = num
    
    elif num > second_largest and num != largest:
        second_largest = num

print("Second Largest :", second_largest)

# # count freq of each character 
text = "hello"

freq1 = {}

for char in text:
    if char not in freq1:
        freq1[char] = 1
    else:
        freq1[char] += 1
print("Frequency of each character :",freq1)

for val,freq in freq1.items():
    print(val ,":" ,freq)


# common elements from two list
nums1 = [10,20,30,40,50,20]
nums2 = [20,30,60,70.30]

common_ele = []
for num in nums1:
    if num in nums2 and num not in common_ele:
        common_ele.append(num)

print("Common Element : ",common_ele)