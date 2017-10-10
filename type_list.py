list1 = ['magical unicorns',19,'hello',98.98,'world']
# list1 = [1,2,4,5.0,7,'sdhgf']
int_type = 0
str_type = 0
float_type = 0
sum = 0
new_str = ""

for i in list1:
    if type(i) is int:
        int_type = int_type+1
        sum = sum+i
    elif type(i) is float:
        float_type = float_type+1
        sum = sum+i
    else:
        str_type = str_type+1
        new_str = new_str + i
if int_type==len(list1):
    print "list is of integer type"
elif float_type==len(list1):
    print "list is of float type"
elif str_type==len(list1):
    print "list is of string type"
else:
    print "list is of mixed type"

print sum
print new_str

    
        
