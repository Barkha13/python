import random   
def coin_tosses():
    head = 0
    tail = 0
    for i  in range(1, 5001):
        toss = random.randint(0, 1)
        if toss == 0:
            head = head + 1
            print "Attempt #" ,i, "Throwing a coin...it's a head!...Got " ,head, "(s) so far and" ,tail, "(s) so far"
        else:
            tail = tail + 1
            print "Attempt #",i, "Throwing a coin...it's a tail!...Got ",head, "(s) so far and",tail, "(s) so far"   
coin_tosses()