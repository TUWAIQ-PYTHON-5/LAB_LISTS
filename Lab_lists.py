# LAB_LISTS
## Given the following list : [2, 3, 4, 5, 15, 1, 43, 20]
### Q1: Write a function that takes a list as a parameter, and then returns  the sum  of all the items in that list.
number_lists = [2, 3, 4, 5, 15, 1, 43, 20]
def sum_function(Numbers):

      Sum = sum(Numbers)
      print(Sum)


sum_function(number_lists)

### Q2: Write a function that takes a list as a parameter, and then returns the largest number from a list of numbers.

def largest_function(Numbers):
    print(max(Numbers))

largest_function(number_lists)


### Q3: Create an odd numbers list from the elements of a range from 1200 to 2000 with steps of 125, using [ list comprehension ].

check_odd_list = [x for x in range(1200,2000,125) if x % 2 != 0 ]
print(check_odd_list)

### Q4: use list slicing to get a new list from the previous list starting from the start to the 5th element in the list.

new_list = number_lists[0:5]
print(new_list)
