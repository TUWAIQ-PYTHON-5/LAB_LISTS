given_list=[2, 3, 4, 5, 15, 1, 43, 20] 

def sumList(list): 
    sum = 0 
    for x in list: 
        sum += x 
    return sum 

print(sumList(given_list))

def findLargest (list): 
    largest= list[0] 
    for x in list:
        if largest <= x: 
            largest = x 
    return largest 

print(findLargest(given_list)) 

oddList = [x for x in range(1200, 2000, 125) if x % 2 != 0 ] 

print(oddList) 

def sliceList(list): 
    listToprint = list[:5] 
    return listToprint 

print(sliceList(oddList))