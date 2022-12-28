# Copyright 2022 Stepanov Dmitriy
# Task C module 1 -- vulnerableDeps

# Functions ###################################################################

# Parsing input data function
def parser():
    # Vulnerable libs input
    set_libs = set(input().split())

    # Direct dependencies input
    set_dependencies = set(input().split())

    # "graph" initialisation
    # values with type "set" better?
    map_data = dict()

    # Parsing data
    while True:
        try:
            input_text = input()
            if not len(input_text):
                continue

            in_str_list = input_text.split()

            # in_str_list[0] -- dependence
            for lib in in_str_list[1:]:
                if lib not in map_data:
                    map_data[lib] = [in_str_list[0]]
                elif in_str_list[0] not in map_data[lib]:
                    map_data[lib].append(in_str_list[0])

        except EOFError:
            break

    return set_libs, set_dependencies, map_data


# Function plotting a route for one vulnerability
def voyager(route, used_deps):
    cur_dep = route[-1]

    # Checking whether a direct dependency has been achieved
    if cur_dep in dir_deps:
        print(*route[::-1])

    if cur_dep in data_graph:
        # Continuation of paths
        for next_dep in data_graph[cur_dep]:
            if next_dep not in used_deps:
                used_deps.add(next_dep)
                route.append(next_dep)
                voyager(route, used_deps)
                route.pop()
                used_deps.discard(next_dep)


# Entry point #################################################################

vuln_libs, dir_deps, data_graph = parser()

for vuln_lib in vuln_libs:
    cur_route = [vuln_lib]
    cur_set = {vuln_lib}
    voyager(cur_route, cur_set)
