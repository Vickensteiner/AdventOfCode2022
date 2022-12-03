with open("Day 3/day3input.txt") as infile:
    sum_priorities = 0
    for line in infile.readlines():
        line = line.strip()
        left, right = "".join(sorted(line[:int(len(line)/2)])), "".join(sorted(line[int(len(line)/2):]))
        counter_left, counter_right = 0, 0
        while(counter_left < len(left) and counter_right < len(right)):
            if(left[counter_left] < right[counter_right]):
                counter_left = counter_left + 1
            elif(left[counter_left] > right[counter_right]):
                counter_right = counter_right + 1
            else:
                sum_priorities = sum_priorities + (ord(left[counter_left]) - 65) % 32
                if(ord(left[counter_left]) > 95):
                    sum_priorities = sum_priorities + 1
                else:
                    sum_priorities = sum_priorities + 27
                break
    print(sum_priorities)
# End Part 1

#%%

with open("Day 3/day3input.txt") as infile:
    sum_priorities = 0
    lines = infile.readlines()
    for i in range(0, len(lines), 3):
        counter_a = 0
        counter_b = 0
        lines[i] = "".join(sorted(lines[i])).strip()
        lines[i + 1] = "".join(sorted(lines[i + 1])).strip()
        lines[i + 2] = "".join(sorted(lines[i + 2])).strip()
        while(counter_a < len(lines[i]) and counter_b < len(lines[i + 1])):
            if(lines[i][counter_a] < lines[i + 1][counter_b]):
                counter_a = counter_a + 1
            elif(lines[i][counter_a] > lines[i + 1][counter_b]):
                counter_b = counter_b + 1
            else:
                if(lines[i][counter_a] not in lines[i + 2]):
                    counter_a = counter_a + 1
                else:
                    sum_priorities = sum_priorities + (ord(lines[i][counter_a]) - 65) % 32
                    if(ord(lines[i][counter_a]) > 95):
                        sum_priorities = sum_priorities + 1
                    else:
                        sum_priorities = sum_priorities + 27
                    break
    print(sum_priorities)