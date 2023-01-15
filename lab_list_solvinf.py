# Q1
def my_function_list():
    my_list = [2,3,4,5,15,1,43,20]
    list_sum = sum(my_list)
    sliced_list = (list_sum[0:5])  # Q4 
    print(sliced_list)
    return list_sum
my_function_list()

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
def odd_numbers(x):
    return [x for x in range(1200,2000,125 ) if x % 2 ==1]
print(odd_numbers(0)) 
odd_numbers()