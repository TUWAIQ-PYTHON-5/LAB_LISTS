
#
# function that returns sum of elements 
def sumElementsList(listOfnum : list) -> int :
    """return sum of the list """
    sum = 0
    for i in range(0 , len(listOfnum)):

        sum = sum + listOfnum[i]
    return sum

print("The sum of the list elements = " ,sumElementsList([2, 3, 4, 5, 15, 1, 43, 20]))
print("----------------------")


#
# function that returns the maximum element
def maxNumberOfList(listOfnumber : list) -> int :
    """return Max int of list """
    maxNumber = 0
    for i in range(0 ,len(listOfnumber)):
        if listOfnumber[i] > maxNumber:
            maxNumber = listOfnumber[i]
            
    return maxNumber
        
print("The max number of list = " , maxNumberOfList([2, 3, 4, 5, 15, 1, 43, 20]))
print("----------------------")



#Create an odd numbers list from the elements of a range from 1200 to 2000
OddNUmbers = [_OddNUmbers for _OddNUmbers in range(1200 , 2000 , 125) if _OddNUmbers % 2 != 0] 
print("odd numbers of list = " , OddNUmbers)
print("----------------------")


#use list slicing to get a new list from the previous list starting from the start to the 5th element in the list.

_list = [2, 3, 4, 5, 15, 1, 43, 20]
_slicingList = _list[:5]
print("The list = ", _list)
print("The new list after slicing = " , _slicingList)




