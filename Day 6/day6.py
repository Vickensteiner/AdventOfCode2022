with open('Day 6/day6input.txt', 'r') as infile:    # Added comments so Zachy-wacky can read :)
    packet = infile.read(3)     # Reads the first three characters of the string
    new_letter = infile.read(1) # Stores the next character
    marker = 4                  # Holds the current index at which we're checking
    while(new_letter):          # While there are still characters in the string
        packet = packet + new_letter    # Add the next character on to the end of the packet
        if(len(set(packet)) == len(packet)):    # If there are as many unique characters as there are characters in the string
            print(marker)       # Output the index at which we find the solution
            if(len(set(packet)) == 14): # If we have found the solution to Part 2
                break           # End the program
            new_letter = infile.read(11)    # After the solution to Part 1 is found (only 4 unique characters), increase the size of the packet to 14 characters
            marker = marker + 11            # Move the marker accordingly
        else:                   # If there was at least one duplicate character in the string
            marker = marker + 1             # Move the marker up by one
            new_letter = infile.read(1)     # Read the next character
        packet = packet[1:]                 # Take off the first character of the packet to get ready for the next loop