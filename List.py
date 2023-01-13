
### Q1: Write a function that takes a list as a parameter, and then returns  the sum  of all the items in that list.

def sumOfList(mylist : list):
    sumofindex : int =0
    for element in mylist:
         sumofindex = sumofindex + element 
    return sumofindex
         
print(sumOfList([2, 3, 4, 5, 15, 1, 43, 20]))        

### Q2: Write a function that takes a list as a parameter, and then returns the largest number from a list of numbers.

def maxOfList(mylist:list):
    maxNumber : int = 0
    for element in mylist:
        if element > maxNumber:
            maxNumber = element
    return maxNumber        
        
        
                
print(maxOfList([2, 3, 4, 5, 15, 1, 43, 20]))

### Q3: Create an odd numbers list from the elements of a range from 1200 to 2000 with steps of 125, using [ list comprehension ].



oddList = [i for i in range(1200 , 2000 , 125) if i % 2 !=0 ]

print(oddList)    
 



### Q4: use list slicing to get a new list from the previous list starting from the start to the 5th element in the list.

sliceList = [2, 3, 4, 5, 15, 1, 43, 20]
newList = sliceList[ : 5 ]
print(newList)