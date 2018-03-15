# 1. Find the Square root of a number. 
def square_root(num):
    if num < 0 or isinstance(num, int) == False :
        return "Invalid Input. Please enter a positive number."
    end = num / 2 +1   #We are just checking till the half number according to the multiplication rule.
    for i in range(0,end+1): # range is not inclusive so we add +1
        if i * i == num:
            return i
    
    return "Not a square."

print "Square root: ",square_root(25) #calling method
print "Square root: ",square_root("hi") #calling method
print "Square root: ",square_root(100) #calling method

