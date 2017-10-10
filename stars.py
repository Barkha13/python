#Part-1
def draw_stars(list1):
    for i in list1:
        print "* " * i
       
x = [4,6,1,3,5,7,25]
draw_stars(x)

#part-2
def draw_stars2(list1):
    for i in list1:
        if type(i) is str:
            # low_list = list1[i].lower()
            # #list1[i] = list1[i].lower()
            print i[0].lower() * len(i)
            # print i[0].lower * i
            
        else:
            print "* " * i

x = [4,"Tom",1,"Michael",5,7,"Jimmy Smith"]
draw_stars2(x)