with open("Day 1/day1input.txt") as infile:
    highest_cals = 0
    current_cals = 0
    for line in infile.readlines():
        if(line.strip() == ""):
            current_cals = 0
        else:
            current_cals = current_cals + int(line)
            if(current_cals > highest_cals):
                highest_cals = current_cals
    print(highest_cals)
# End Part 1

#%%

with open("Day 1/day1input.txt") as infile:
    highest_cals = [0, 0, 0]    # Rank 1, 2, 3 in cals
    current_cals = 0
    for line in infile.readlines():
        if(line.strip() == ""):
            if(current_cals > highest_cals[2]):
                highest_cals[2] = current_cals
            if(current_cals > highest_cals[1]):
                highest_cals[2] = highest_cals[1]
                highest_cals[1] = current_cals
            if(current_cals > highest_cals[0]):
                highest_cals[1] = highest_cals[0]
                highest_cals[0] = current_cals
            current_cals = 0
        else:
            current_cals = current_cals + int(line)
    print(highest_cals[0] + highest_cals[1] + highest_cals[2])