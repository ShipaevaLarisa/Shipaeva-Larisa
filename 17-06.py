def from_string_to_list(string, container):
    for i in range(len(string.split())):
        container.append(int(string.split()[i - 1]))
