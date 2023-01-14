def addition (element :int):
    sum :int=0
    for num in range(0, len(element)):
        sum = sum + element[num]
    return sum



def large(values: int):
    big_number: int = values[0]
    for val in values:
        if val > big_number:
            big_number = val
    return big_number #or max(values)




#Q1_//////////////////
number=[1,2,3,4,5]
print("The sum of the numbers:  ",addition(number))
#Q2_////////////////////////
print("the largest number is:  ",large(number))
#Q3_//////////////////////////////////
numbrts_list = [x for x in range(1200,2000,125) if(x % 2)!=0]
'''for x in range(1200,2000,125):
    if (x % 2)!=0:
        numbrts_list.append(x)'''
print(numbrts_list)
#Q4_////////////////////////////////////////
old_list=[2,4,56,8,2,7,4,7]
new_list = old_list[:5]
print(new_list)