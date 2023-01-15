
## Given the following list : [2, 3, 4, 5, 15, 1, 43, 20]

num_list :int = [2 , 3 , 4 , 5 , 15 , 1 , 43 , 20] 


### Q1: Write a function that takes a list as a parameter, and then returns  the sum  of all the items in that list.

def sum_list (s:int):
    return sum(s)

print("The sum of all items in the list is :" ,sum_list(num_list))

### Q2: Write a function that takes a list as a parameter, and then returns the largest number from a list of numbers.

def largest_num_list (l:int):
    return max(l)

print("The largest number on the list is :",largest_num_list(num_list))

### Q3: Create an odd numbers list from the elements of a range from 1200 to 2000 with steps of 125, using [ list comprehension ].

odd_num_list = [o for o in range (1200,2000,125) if o % 2 == 1]
print("The odd numbers of the given range are :" , odd_num_list)
 
### Q4: use list slicing to get a new list from the previous list starting from the start to the 5th element in the list.

sub_num = num_list[0:5]
print("The new list from the start to the 5th element  is :", sub_num)



