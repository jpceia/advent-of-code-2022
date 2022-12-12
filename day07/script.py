class File:
    def __init__(self, name, size):
        self.name = name
        self.size = size

class Dir:
    def __init__(self, name="/"):
        self.parent = None
        self.name = name
        self.dirs = []
        self.files = []

    def print(self, indent=0):
        print(" " * indent + self.name)
        for d in self.dirs:
            d.print(indent + 2)
        for f in self.files:
            print(" " * (indent + 2) + f.name, f.size)

    def size(self):
        size = 0
        for d in self.dirs:
            size += d.size()
        for f in self.files:
            size += f.size
        return size

    def recursive_subdirs(self):
        subdirs = []
        for d in self.dirs:
            subdirs.append(d)
            subdirs += d.recursive_subdirs()
        return subdirs

root = Dir()
cwd = root

with open("input.txt", "r") as f:
    for line in f:
        line = line.strip()
        print(line)
        line = line.split()
        if line[0] == "$": # command
            cmd = line[1]
            if cmd == "cd":
                dir = line[2]
                if dir == "..":
                    cwd = cwd.parent
                elif dir == "/":
                    cwd = root
                else:
                    for d in cwd.dirs:
                        if d.name == dir:
                            cwd = d
                            break
                    else:
                        raise ValueError("Directory not found: " + dir)
            elif cmd == "ls":
                if len(line) > 2:
                    raise ValueError("Too many arguments")
            else:
                raise ValueError("Unknown command: " + cmd)
        elif line[0] == "dir":
            name = line[1]
            for d in cwd.dirs:
                if d.name == name:
                    break
            else:
                d = Dir(name)
                d.parent = cwd
                cwd.dirs.append(d)
        else: # file
            size = int(line[0])
            name = line[1]
            for f in cwd.files:
                if f.name == name:
                    break
            else:
                file = File(name, size)
                cwd.files.append(file)
                
root.print()
dirs = root.recursive_subdirs()
max_size = 100000
dirs = [d for d in dirs if d.size() <= max_size]
tot_size = sum(d.size() for d in dirs)

# Part 1
print("Part 1:", tot_size)

# Part 2
dirs = root.recursive_subdirs()
# sort by size, then by name
used_disk_space = root.size()
needed_disk_space = 40000000
min_disk_space_to_free  = used_disk_space - needed_disk_space
print("Used disk size:", used_disk_space)
print("Needed disk size:", needed_disk_space)
print("Min space to free:", min_disk_space_to_free)
dirs = filter(lambda d: d.size() >= min_disk_space_to_free, dirs)
dirs = sorted(dirs, key=lambda d: (d.size(), d.name))
print("Dir to delete:", dirs[0].name, dirs[0].size())