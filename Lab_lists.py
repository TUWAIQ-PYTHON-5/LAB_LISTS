# LAB_LISTS
## Given the following list : [2, 3, 4, 5, 15, 1, 43, 20]
### Q1: Write a function that takes a list as a parameter, and then returns  the sum  of all the items in that list.

def sum_function(Numbers):

    Sum = sum(Numbers)
    print(Sum)

sum_numbers_list = [2, 3, 4, 5, 15, 1, 43, 20]
sum_function(sum_numbers_list)

### Q2: Write a function that takes a list as a parameter, and then returns the largest number from a list of numbers.

def largest_function(Numbers):
    print(max(Numbers))

largest_numbers_list = [2, 3, 4, 5, 15, 1, 43, 20]
largest_function(largest_numbers_list)


### Q3: Create an odd numbers list from the elements of a range from 1200 to 2000 with steps of 125, using [ list comprehension ].

check_odd_list = [x for x in range(1200,2000,125) if x % 2 != 0 ]

print(check_odd_list)

### Q4: use list slicing to get a new list from the previous list starting from the start to the 5th element in the list.

slicing_list = [2, 3, 4, 5, 15, 1, 43, 20]
new_list = slicing_list[0:6]
print(slicing_list[0:6])
