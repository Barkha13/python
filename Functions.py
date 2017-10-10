#odd-even function
# def odd_even(start,end):
#     for i in range(start,end):
#         if i%2 == 0:
#             print "Number is",i , "This is an even number."
#         else:
#             print "Number is",i , "This is an odd number."

# odd_even(1,2001)

#Multiply function
list1 = [2,4,10,16]
def multiply(list1,multiplier):
    for i in range(len(list1)):
        list1[i] = list1[i] * multiplier
    return list1

# b = multiply(list1,5)
# print b

#Hacker challenge
def layered_multiples(arr):
    for i in range(len(arr)):
        arr[i] = [1]*arr[i]
    return arr
        
x = layered_multiples(multiply([2,4,5],3))
print multiply([2,4,5],3)
print x  