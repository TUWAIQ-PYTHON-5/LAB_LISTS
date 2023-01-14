def totalOflists(numbers):
    '''Return total numbers of list'''

    total:float = 0
    for number in numbers:
        total += number

    #OR YOU CAN USE SUM FUNCION #return sum(numbers)
    return total 
   

def largestNumberinlist(numbers):
    '''Return the largest number in the list'''

    largest:int = numbers[0]
    for number in numbers:
        if number > largest:
            largest = number
    
    return largest


numbers:list = [2, 3, 4, 5, 15, 1, 43, 20]

print("TOTAL OF NUMBERS : ",totalOflists(numbers))
print("LARGE NUMBER IS : ",largestNumberinlist(numbers))


oddNumber:list = [i for  i in range(1200,2000,125) if i%2 !=0]
print("ODD LIST : ",oddNumber,  end="\n")

copyOddNumber:list = numbers[:5]
print("COPY NUMBERS FROM ODD LIST : ",copyOddNumber, end=" ")


