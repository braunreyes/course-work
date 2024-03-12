from collections import deque

graph = {}
graph["you"] = ["alice", "bob", "claire"]
graph["bob"] = ["anuj", "peggy"]
graph["alice"] = ["peggy"]
graph["claire"] = ["thom", "jonny"]
graph["anuj"] = []
graph["peggy"] = []
graph["thom"] = []
graph["jonny"] = []


def person_is_seller(person):
    return person[-1] == "m"


def bfs(graph: dict, start: str):

    search_queue = deque()
    search_queue += graph[start]
    searched = set()
    while search_queue:
        person = search_queue.popleft()
        if person not in searched:
            if person_is_seller(person):
                print(f"{person} is a seller")
                return True
            else:
                search_queue += graph[person]
                searched.add(person)
    return False


# shortest path

paths = {}
paths["cab"] = ["cat", "car"]
paths["cat"] = ["mat", "bat"]
paths["car"] = ["bar", "cat"]
paths["mat"] = ["bat"]
paths["bat"] = []
paths["bar"] = ["bat"]


def bfs_shortest_path(graph: dict, start: str, goal: str):
    search_queue = deque()
    search_queue.append([start])
    searched = set()

    if start == goal:
        return "start == goal!"

    while search_queue:
        path = search_queue.popleft()
        # last node from the path
        node = path[-1]
        if node not in searched:
            neighbours = graph[node]
            # go through all neighbour nodes, construct a new path and
            # push it into the queue
            for n in neighbours:
                new_path = list(path) # needs to be a copy
                new_path.append(n)
                search_queue.append(new_path) 
                # return path if neighbour is goal
                if n == goal:
                    return new_path
 
            # mark node as explored
            searched.add(node)
        print(search_queue)
 
    # in case there's no path between the 2 nodes
    return "So sorry, but a connecting path doesn't exist :("


if __name__ == "__main__":
    bfs(graph, "you")
    print(bfs_shortest_path(paths, "cab", "bat"))
