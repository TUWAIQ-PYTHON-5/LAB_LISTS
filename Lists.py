
## Given the following list : [2, 3, 4, 5, 15, 1, 43, 20]
### Q1: Write a function that takes a list as a parameter, and then returns  the sum  of all the items in that list.
### Q2: Write a function that takes a list as a parameter, and then returns the largest number from a list of numbers.
### Q3: Create an odd numbers list from the elements of a range from 1200 to 2000 with steps of 125, using [ list comprehension ].
### Q4: use list slicing to get a new list from the previous list starting from the start to the 5th element in the list.


given_list=[2, 3, 4, 5, 15, 1, 43, 20] 
  
  
# A1 
def sumList(list): 
    sum = 0 
    for x in list: 
        sum += x 
    return sum 

print(sumList(given_list))   
  
# A2 
def findLargest (list): 
    largest= list[0] 
    for x in list:
        if largest <= x: 
            largest = x 
    return largest 
  
print(findLargest(given_list)) 
  
# A3 
oddList = [x for x in range(1200, 2000, 125) if x % 2 != 0 ] 

print(oddList) 
  
# A4   
def sliceList(list): 
    newList = list[5:] 
    return newList 
  
print(sliceList(oddList))