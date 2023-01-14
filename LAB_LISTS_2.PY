
lst=[2, 3, 4, 5, 15, 1, 43, 20]
def large(n):
    largest_number =lst[6]
    for i in lst:
        if i> largest_number:
            largest_number=i
    return largest_number
print(large(lst))