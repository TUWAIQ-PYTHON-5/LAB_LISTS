## Given the following list : [2, 3, 4, 5, 15, 1, 43, 20]
newList = [2, 3, 4, 5, 15, 1, 43, 20]

### Q1: Write a function that takes a list as a parameter, and then returns  the sum  of all the items in that list.
def sum(list):
    result = 0
    for number in list:
        result += number
    return result

print(sum(newList))

### Q2: Write a function that takes a list as a parameter, and then returns the largest number from a list of numbers.
def largestNumber(list):
    largest = list[0]
    for number in list:
        if number >largest:
            largest=number
    return largest

print(largestNumber(newList))

### Q3: Create an odd numbers list from the elements of a range from 1200 to 2000 with steps of 125, using [ list comprehension ].
oddList = [number for number in range(1200,2000,125) if number % 2 != 0]
print(oddList)

# without using list comprehension 
# oddList = list()
# for number in range(1200,2000,125):
#     if(number % 2 != 0 ):
#         oddList.append(number)

### Q4: use list slicing to get a new list from the previous list starting from the start to the 5th element in the list.
slicingList = newList[:5]
print(slicingList)

