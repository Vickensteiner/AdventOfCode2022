class globals:
    small_dirs_size = 0

class dir:
    def __init__(self, name, parent = None):
        self.name = name
        self.children = []
        self.parent = parent
        self.size = 0

    def calc_size(self):
        self.size = self.size if self.children is None else self.size + sum([child.calc_size() for child in self.children])
        if(self.size <= 100000):
            globals.small_dirs_size = globals.small_dirs_size + self.size
        return self.size

    def get_child(self, name):
        return list(child for child in self.children if child.name == name)

    def add_file(self, file):
        self.size = self.size + file

    def add_child(self, child):
        self.children = self.children + [child]

with open("Day 7/day7input.txt", 'r') as infile:
    lines = infile.readlines()
    toplevel = dir('/')
    current_dir = toplevel

    for i in range(2, len(lines)):
        if(lines[i][0] == '$'):
            if(lines[i][2] == 'c'):
                destination = lines[i][5:].strip()
                if(destination == '/'):
                    current_dir = toplevel
                elif(destination == '..'):
                    current_dir = current_dir.parent
                else:
                    current_dir = current_dir.get_child(destination.strip())[0]
        elif(lines[i][0] == 'd'):
            current_dir.add_child(dir(lines[i][4:].strip(), parent = current_dir))
        else:
            current_dir.add_file(int(lines[i][:lines[i].index(' ')]))

    toplevel.calc_size()
    print(globals.small_dirs_size)
    # End Part 1

#%%
    
    size_to_clear = 30000000 - (70000000 - toplevel.size)
    
    to_check = [toplevel]
    optimal_dir = toplevel

    while(len(to_check) > 0):
        current_dir = to_check.pop(0)
        if(current_dir.size < optimal_dir.size):
            optimal_dir = current_dir
        to_check = to_check + list(child for child in current_dir.children if child.size > size_to_clear)
    
    print(optimal_dir.size)
    # End Part 2