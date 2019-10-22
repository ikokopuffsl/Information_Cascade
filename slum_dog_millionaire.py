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
        self.final_choice = None

    def make_choice(self, choice_val):
        my_choice = "Household {} with choice_val of {} and p1 = {} p2 = {}, and p3 = {} chose well: ".format(self.type_of_house, choice_val, self.p1, self.p2, self.p3)
        string = ""
        min_vals = {}
        if choice_val < self.p1:
            min_vals["one"] = self.p1
        if choice_val < self.p2:
            min_vals["two"] = self.p2
        if choice_val < self.p3:
            min_vals["three"] = self.p3
            
        string = min(min_vals, key=min_vals.get)
        if string == "one":
            self.final_choice = 1
        elif string == "two":
            self.final_choice = 2
        else:
            self.final_choice = 3
        return my_choice + string

def bayes_prob_update(villager, actual_well, previous_choices):
    # Update the probability for the current villager for each of the wells once for each of the previous person
    for choice in previous_choices:
        # Need new q depending on the previous villagers choice
        q = find_q(choice, actual_well)
        # Calculate all at once so that our p1, p2, and p3 remain the same for one iteration and don't affect each other
        new_prob = (((q*villager.p1) / ((q*villager.p1) + (q*villager.p2) + (q*villager.p3))), ((q*villager.p2) / ((q*villager.p1) + (q*villager.p2) + (q*villager.p3))), ((q*villager.p3) / ((q*villager.p1) + (q*villager.p2) + (q*villager.p3))))
        # Pass by reference, right?
        village.p1 = new_prob[1]
        village.p2 = new_prob[2]
        village.p3 = new_prob[3]
    
def simulation(village, actual_well):
    neighbor_choice = 0 # Need to modify, what is the first neighbor_choice value?
    neighbor_choices = []
    for villager in village:
        # q = find_q(neighbor_choice, actual_well)
        bayes_prob_update(villager, actual_well, neighbor_choices)

        # now this will be new choice for the current villager
        choice_value = random.uniform(0,1)
        villager.make_choice(choice_value)
        neighbor_choice = villager.final_choice
        neighbor_choices.append(neighbor_choice)

    return neighbor_choices    

def find_q(neighbor_choice, actual_well):
    if actual_well == neighbor_choice:
        return 0.8
    else: 
        return 0.1

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
        
        choice_value = random.uniform(0,max(household.p1,household.p2,household.p3))
        choice = household.make_choice(choice_value)
        with open(result_file, "a+") as f:
            f.write(choice + "\n\n")
            
    # Part 1

    # Part 2


    # Part 3



# Returns 1,2, or 3
def choose_well():
    return random.randint(0,2)

run_world()
