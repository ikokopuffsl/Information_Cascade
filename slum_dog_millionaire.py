import random
import sys


# which well acutally has it
# 3 categories of households, good, middle, bad

class HouseHold():
    def __init__(self, p1, p2, p3):
        self.neighbors = []
        self.p1 = 0.0
        self.p2 = 0.0
        self.p3 = 0.0


def bayes_prob_update(q, other, stuff):

    pass

# TODO: implement how good, middle, and else calculates the P values
def vary_p_fortune(fortune, well):
    result = (0, 0, 0)
    if fortune == "good":
        pass
    elif fortune == "middle":
        pass
    else:
        pass

    return result


def create_village(salvation):
    village = []
    for i in range(15): # Create the households

        if i < 5:
            p_results = vary_p_fortune("good", salvation)
            family = HouseHold(p_results[0], p_results[1], p_results[2])
        elif i >= 5 and i < 10:
            p_results = vary_p_fortune("middle", salvation)
            family = HouseHold(p_results[0], p_results[1], p_results[2])
        else:
            p_results = vary_p_fortune("bad", salvation)
            family = HouseHold(p_results[0], p_results[1], p_results[2])
    
        village.append(family)
    random.shuffle(village)
    return village

def run_world():
    salvation = choose_well() 

    q = sys.argv[1] # Trust value

    village = create_village(salvation)

    # Part 1

    # Part 2

    # Part 3



# Returns 1,2, or 3
def choose_well():
    return random.randint % 2 + 1
