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
only_odd = [number for number in mylist if number % 2 == 1]
print(only_odd)



#Q4
print(mylist[:6])


