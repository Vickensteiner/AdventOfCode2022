with open("Day 2/day2input.txt") as infile:
    i_play = ['X', 'Y', 'Z']            # Rock, Paper, Scissors
    opponent_plays = ['A', 'B', 'C']    # Rock, Paper, Scissors
    score = 0
    for line in infile.readlines():
        strategy = line.split()
        score = score + i_play.index(strategy[1]) + 1
        score = score + 3 * (((i_play.index(strategy[1]) - opponent_plays.index(strategy[0]) + 1) % 3))
    print(score)
# End Part 1

#%%

with open("Day 2/day2input.txt") as infile:
    outcome = ['X', 'Y', 'Z']           # Lose, Draw, Win
    i_play = ['A', 'B', 'C']            # Rock, Paper, Scissors
    opponent_plays = ['A', 'B', 'C']    # Rock, Paper, Scissors
    score = 0
    for line in infile.readlines():
        strategy = line.split()
        score = score + outcome.index(strategy[1]) * 3
        score = score + (opponent_plays.index(strategy[0]) + (outcome.index(strategy[1]) - 1)) % 3 + 1
    print(score)
# End Part 2