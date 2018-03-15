# Write a Python program to check that a string contains only a certain set of characters (in this case a-z, A-Z and 0-9)
import re

# def check_string(str):
#     regex = re.compile(r"[^a-zA-Z0-9]")
#     check = regex.search(str)
#     return not bool(check)

# print check_string("string")
# print check_string("@$gjhs90")

#  Write a Python program that matches a string that has an a followed by zero or more b's

# def check_ab(str):
#     regex = re.compile(r"a*")
#     if regex.search(str):
#         return "match"
#     else:
#         return "not a match"
def text_match(text):
        # patterns = 'ab*?'
        patterns = '^a.b*$'
        if re.search(patterns,  text):
                return 'Found a match!'
        else:
                return('Not matched!')
    
print text_match('abbbbb')