
# #Q1
def sum_list(number) -> int :
  i = 0
  for x in number:
    i = i + x
  return i
number = [2, 3, 4, 5, 15, 1, 43, 20]
print ("sum my_list", sum_list(number))


# #Q2
def large_Number(list):

	max = list1[0]
	for x in list1:
		if x > max:
			max = x
	return max
list1 = [2, 3, 4, 5, 15, 1, 43, 20]
print("Large number is:", large_Number(list))


#Q3
number_list = [ x for x in range(1200,2000,125) if x % 2 != 0]
print(number_list)


#Q4
slic_List = [2, 3, 4, 5, 15, 1, 43, 20]
new_list = slic_List[0:5]
print(slic_List[0:5])
