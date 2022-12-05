with open("Day 5/day5input.txt", 'r') as infile:
    lines = infile.readlines()
    break_index = 0
    for line in lines:
        if(len(line.strip()) == 0):
            break_index = lines.index(line) # In case other inputs have a different height of crates
            break
    starting_arrangement, moves = lines[:break_index - 1], lines[break_index + 1:]  # Separate starting arrangement and moves list

    # Processing initial arrangement
    num_cols = len(starting_arrangement[-1].strip().split())    # In case other inputs have a different number of columns
    stacks = [[] for _ in range(num_cols)]
    for line in reversed(starting_arrangement):
        crates = []
        for crate in line.split(']')[:-1]:  # Ignores empty string at end of list
            crates = crates + [' ' for _ in range((crate.count(' ') - 1) // 4)] # Includes empty spots in each row of crates
            crates = crates + [crate[-1:]]  # Stores name of each crate
        for index in range(num_cols):
            if(crates[index] != ' '):
                stacks[index] = stacks[index] + [crates[index]] # Adds all non-empty crates into their corresponding stack
    
    # Performing moves
    for line in moves:
        current_move = [int(entry) for entry in line.replace("move ", "").replace("from ", "").replace("to ", "").split()]
        for repetitions in range(current_move[0]):
            stacks[current_move[2] - 1] = stacks[current_move[2] - 1] + stacks[current_move[1] - 1][-1:]
            stacks[current_move[1] - 1] = stacks[current_move[1] - 1][:-1]
    
    # Printing top level crates, excluding empty stacks
    for stack in stacks:
        if(len(stack) > 0):
            print(stack[-1:][0], end = '')
    print()
# End Part 1

#%%

with open("Day 5/day5input.txt", 'r') as infile:
    lines = infile.readlines()
    break_index = 0
    for line in lines:
        if(len(line.strip()) == 0):
            break_index = lines.index(line) # In case other inputs have a different height of crates
            break
    starting_arrangement, moves = lines[:break_index - 1], lines[break_index + 1:]  # Separate starting arrangement and moves list

    # Processing initial arrangement
    num_cols = len(starting_arrangement[-1].strip().split())    # In case other inputs have a different number of columns
    stacks = [[] for _ in range(num_cols)]
    for line in reversed(starting_arrangement):
        crates = []
        for crate in line.split(']')[:-1]:  # Ignores empty string at end of list
            crates = crates + [' ' for _ in range((crate.count(' ') - 1) // 4)] # Includes empty spots in each row of crates
            crates = crates + [crate[-1:]]  # Stores name of each crate
        for index in range(num_cols):
            if(crates[index] != ' '):
                stacks[index] = stacks[index] + [crates[index]] # Adds all non-empty crates into their corresponding stack
    
    # Performing moves
    for line in moves:
        current_move = [int(entry) for entry in line.replace("move ", "").replace("from ", "").replace("to ", "").split()]
        stacks[current_move[2] - 1] = stacks[current_move[2] - 1] + stacks[current_move[1] - 1][-current_move[0]:]
        stacks[current_move[1] - 1] = stacks[current_move[1] - 1][:-current_move[0]]
    
    # Printing top level crates, excluding empty stacks
    for stack in stacks:
        if(len(stack) > 0):
            print(stack[-1:][0], end = '')
# End Part 2