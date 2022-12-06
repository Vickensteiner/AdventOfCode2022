with open('Day 6/day6input.txt', 'r') as infile:
    packet = infile.read(3)
    new_letter = infile.read(1)
    marker = 4
    while(new_letter):
        packet = packet + new_letter
        if(len(set(packet)) == len(packet)):
            print(marker)
            new_letter = infile.read(11)
            marker = marker + 11
            if(len(set(packet)) == 14):
                break
        else:
            marker = marker + 1
            new_letter = infile.read(1)
        packet = packet[1:]