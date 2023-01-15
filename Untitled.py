num =[2, 3, 4, 5, 15, 1, 43, 20]
def number():
    return num


total = 0
for num in num:
    total=total+num
print(total)


def maxNumber():
    return('The biggest number is:', max(num))


newList=[]
x=0
def odd():
    for odd in range(1200,2000,125):
        if x % odd == 1 :
            print(x)
odd()