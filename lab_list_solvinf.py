# Q1
my_list=[2,3,4,5,15,1,43,20]
def my_function_list(my_list: list):
    list_sum = sum(my_list)
    return list_sum
print(my_function_list(my_list))


#Q2
def theLargest(list1):
	max = list1[0]
	for x in list1:
		if x > max:
			max = x
	return max
list1 = [10, 20, 4, 45, 99]
print("Largest element is:", theLargest(list1))
theLargest(list1)


#Q3
def odd_numbers(n):
    return [x for x in range(1200,2000,125) if x%2 != 0]
print(odd_numbers(1))
sliced_list = my_list[0:5]  # Q4 
print(sliced_list)