lst=[2, 3, 4, 5, 15, 1, 43, 20]
def func(l):
    total=0
    for i  in range(len(lst)):
        total+=lst[i]
    return total 


print("The sum of the list ",func(lst))
