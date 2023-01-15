# Q1
my_list=[2,3,4,5,15,1,43,20]


def my_function_list(my_list: list):
    return sum(my_list)
print(my_function_list(my_list))



#Q2
def theLargest(my_list):
	max = my_list[0]
	for x in my_list:
		if x > max:
			max = x
	return max

print(2,"Largest element is:", theLargest(my_list))
theLargest(my_list)




def odd_numbers(n):
    return [x for x in range(1200,2000,125) if x%2 != 0]
print(3,odd_numbers(0))



#Q4
sliced_list = my_list[0:5]
print(4,sliced_list)

