#Q1
mylist = [2, 3, 4, 5, 15, 1, 43, 20]

# using sum() function
total = sum(mylist)
print("Sum of all elements:", total)



#Q2
# sorting the list
mylist.sort()
print("Largest element is:", mylist[-1])



#Q3
def odd_numbers(n):
    return [x for x in range(1200,2000,125) if x%2 != 0]
print(3,odd_numbers(0))


#Q4
sliced_list = mylist[0:5]
print(4,sliced_list)

