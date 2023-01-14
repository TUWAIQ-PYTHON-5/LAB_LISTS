
## function (1)
def sum_list(list_numbers : list):
    total=0
    for number in list_numbers:
        total+=number

    return total

print (sum_list([2, 3, 4, 5, 15, 1, 43, 20]))



## function (2)

def largest_num(list_numbers : list):
        num =0
        for number in list_numbers:
          num = max((list_numbers))

        return num

print (largest_num([2, 3, 4, 5, 15, 1, 43, 20]))



## list comprehension (3)
odd_list= [num for num in range(1200,2000,125) if num % 2 !=0]
print (odd_list)


## slicing 
list1=[2, 3, 4, 5, 15, 1, 43, 20]
new_list=list1[:5]
print (new_list)


