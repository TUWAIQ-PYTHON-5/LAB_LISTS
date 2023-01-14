numbers = [2,3,4,5,15,1,43,20]

def sun(numbers):
    total = 0


    for x in numbers:

        total += x

    return total

print(sum(numbers))

#max
def myMax(list1):
    max = list1 [0]
    for x in list1:
        print("Number =", x)
        if x > max:
          max = x
    return max

list1 = [10,20,4,45,99]
print("Largest element is:", myMax(list1))

#odd numbers
odd = []
for i in range(1200,2000):
    if (i % 2!=0):
        odd.append(i)
    print(odd)
#list slicing
Lst = [50,70,30,20,90,10,50]
print(Lst[0:5])