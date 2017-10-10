name = ["Anna", "Eli", "Pariece", "Brendan", "Amy", "Shane", "Oscar"]
favorite_animal = ["horse", "cat", "spider", "giraffe", "ticks", "dolphins", "llamas","dskcb"]
def make_dict(arr1,arr2):
    my_dict = {}
    if len(arr1)>=len(arr2):
        my_dict_tuple = zip(arr1,arr2)
        # print my_dict_tuple
        my_dict = dict(my_dict_tuple)
    
    else:
        my_dict_tuple = zip(arr2,arr1)
        my_dict = dict(my_dict_tuple)
    return my_dict

answer = make_dict(name,favorite_animal)
print answer