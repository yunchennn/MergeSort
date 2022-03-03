# from operator import le
# from turtle import left, right


# numlist = "IntegerArray.txt"
# file = open(numlist, 'r')

# with file as f:
#     numList = [int(integers.strip()) for integers in f.readlines()]
    
# count = 0

# def invercount(x):
#     global count
#     mid = len(x)//2
#     leftarray = x[:mid]
#     rightarray = x[mid:]

#     if len(x)>1:
#         invercount(leftarray)
#         invercount(rightarray)

#     i, j = 0, 0

#     a= leftarray
#     b= rightarray

#     for k in range(len(a)+len(b)+1):
#         if a[i] <= b[j]:
#             x[k] = a[i]
#             i = i + 1
#             if i == len(a) and j != len(b):
#                 while j != len(b):
#                     k = k +1
#                     x[k] = b[j]
#                     j = j+1
#                 break
#         elif a[i]>b[j]:
#             x[k] = b[j]
#             count = count + (len(a) - i)
#             j = j +1
#             if j == len(b) and i != len(a):
#                 while i != len(a):
#                     k+= 1
#                     x[k] = a[i]
#                     i += 1                    
#                 break   
#     return x

# invercount(numList)
# print (count)

NUMLIST_FILENAME = "IntegerArray.txt"
inFile = open(NUMLIST_FILENAME, 'r')

with inFile as f:
    numList = [int(integers.strip()) for integers in f.readlines()]
    
count = 0

def inversionsCount(x):
    global count
    midsection = len(x) // 2
    leftArray = x[:midsection]
    rightArray = x[midsection:]
    if len(x) > 1:
        # Divid and conquer with recursive calls
        # to left and right arrays similar to
        # merge sort algorithm
        inversionsCount(leftArray)
        inversionsCount(rightArray)
        
        # Merge sorted sub-arrays and keep
        # count of split inversions
        i, j = 0, 0
        a = leftArray; b = rightArray
        for k in range(len(a) + len(b) + 1):
            if a[i] <= b[j]:
                x[k] = a[i]
                i += 1
                if i == len(a) and j != len(b):
                    while j != len(b):
                        k +=1
                        x[k] = b[j]
                        j += 1
                    break
            elif a[i] > b[j]:
                x[k] = b[j]
                count += (len(a) - i)
                j += 1
                if j == len(b) and i != len(a):
                    while i != len(a):
                        k+= 1
                        x[k] = a[i]
                        i += 1                    
                    break   
    return x
# call function and output number of inversions
inversionsCount(numList)
print (count) 

