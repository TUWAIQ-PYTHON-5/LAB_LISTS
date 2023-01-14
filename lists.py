list = [2, 3, 4, 5, 15, 1, 43, 20]

#Q1
def sumList(list):
    sum = 0
    for item in list:
        number = int(item)
        sum += number
    return sum

print(sumList(list))

#Q2
def largestNumber(list):
    largest = 0
    for number in list:
        if number > largest:
            largest = number
    return largest

print(largestNumber(list))

#Q3
oddList = [x for x in range(1200,2000,125) if x%2 != 0]
print(oddList)

#Q4
slicedList = list[:5]
print(slicedList)
