import random
import sys


# which well acutally has it
# 3 categories of households, good, middle, bad
# Run with python3

class HouseHold():
    def __init__(self, p1, p2, p3, type_of_house):
        self.neighbors = []
        self.p1 = p1
        self.p2 = p2
        self.p3 = p3
        self.type_of_house = type_of_house
    
    def make_choice(self, choice_val):
        my_choice = "Household {} with p1 = {} p2 = {}, and p3 = {} chose well: ".format(self.type_of_house, self.p1, self.p2, self.p3)
        if choice_val <= self.p1:
            my_choice += "one\n"
        elif choice_val <= (self.p2 + self.p1):
            my_choice += "two\n"
        else:
            my_choice += "three\n"
        return my_choice


def bayes_prob_update(q, other, stuff):

    pass

# TODO: implement how good, middle, and else calculates the P values
def vary_p_fortune(fortune, well):
    result = [0, 0, 0]
    if fortune == "good":
        result[well] = .8
    elif fortune == "middle":
        result[well] = .5
    else:
        result[well] = .2
    random_num = random.uniform(0, (1 - (result[well])))
    random_num2 = (1 - (random_num+result[well]))
    # find all indices i where result[i] == 0
    arr = [i for i, e in enumerate(result) if e == 0]
    result[arr[0]] = random_num
    result[arr[1]] = random_num2
    return result


def create_village(salvation):
    village = []
    for i in range(15): # Create the households

        if i < 5:
            p_results = vary_p_fortune("good", salvation)
            family = HouseHold(p_results[0], p_results[1], p_results[2], "good")
        elif i >= 5 and i < 10:
            p_results = vary_p_fortune("middle", salvation)
            family = HouseHold(p_results[0], p_results[1], p_results[2], "middle")
        else:
            p_results = vary_p_fortune("bad", salvation)
            family = HouseHold(p_results[0], p_results[1], p_results[2], " bad")
    
        village.append(family)
    random.shuffle(village)
    return village

def run_world():
    salvation = choose_well() 

    #q = sys.argv[1] # Trust value
    result_file = sys.argv[1]
    # minus well by one to get an index
    village = create_village(salvation)
    with open(result_file, "a+")as f:
        f.write("Correct well is: " + str(salvation + 1) + "\n")
    for household in village:
        choice_value = random.uniform(0,1)
        choice = household.make_choice(choice_value)
        with open(result_file, "a+") as f:
            f.write(choice)
            
    # Part 1

    # Part 2

    # Part 3



# Returns 1,2, or 3
def choose_well():
    return random.randint(0,2)

run_world()
