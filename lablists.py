#Q1
def list_sum(lst):
    return list_sum + (lst[1:]) 
lst = [2, 3, 4, 5, 15, 1, 43, 20]
print(sum(lst))



#َQ2
def largest_number(numbers):
     
    biggest_num = numbers[0]

    for num in numbers:
        if num > biggest_num:
            biggest_num = num

    return biggest_num

print(largest_number([2, 3, 4, 5, 15, 1, 43, 20]))

#Q3
odd_num = [x for x in range(1200, 2000) if x %2 != 0 ]

#Q4
list1 = [2, 3, 4, 5, 15, 1, 43, 20]
new_list = list1[:5]
print(new_list)




