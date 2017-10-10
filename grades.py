import random
def Grades(count):
    for i in range(1,count):
        score = random.randint(1,100)
        if score >=60 and score <70:
            print "Score: ",score ,"Youe Grade is D"
        elif score >=70 and score <80:
            print "Score: ",score ,"Youe Grade is B"
        elif score >=80 and score <90:
            print "Score: ",score ,"Youe Grade is C"
        elif score >=90 and score <100:
            print "Score: ",score ,"Youe Grade is A"
        else:
            print "Score: ",score,"Sorry!!!!!But you are failed"
    print "End of the program.Bye!!"


Grades(10)
    