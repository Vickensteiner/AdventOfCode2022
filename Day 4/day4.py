with open("Day 4/day4input.txt") as infile:
    fully_inclusive_ranges = 0
    for line in infile.readlines():
        left, right = line.split(",")[0].split('-'), line.split(",")[1].split('-')
        if((int(left[0]) <= int(right[0]) and int(left[1]) >= int(right[1])) or (int(left[0]) >= int(right[0]) and int(left[1]) <= int(right[1]))):
            fully_inclusive_ranges = fully_inclusive_ranges + 1
    print(fully_inclusive_ranges)
# End Part 1

#%%

with open("Day 4/day4input.txt") as infile:
    overlapping_ranges = 0
    for line in infile.readlines():
        left, right = line.split(",")[0].split('-'), line.split(",")[1].split('-')
        if(int(right[1]) > int(left[1]) and int(right[0]) <= int(left[1])):
            overlapping_ranges = overlapping_ranges + 1
        elif(int(left[1]) >= int(right[1]) and int(left[0]) <= int(right[1])):
            overlapping_ranges = overlapping_ranges + 1
        else:
            pass
    print(overlapping_ranges)
# End Part 2