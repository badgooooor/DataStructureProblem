adj = [ [0,2,0,1,0,0,0,0],
        [0,0,0,3,10,0,0],
        [4,0,0,0,0,5,0],
        [0,0,2,0,2,8,4],
        [0,0,0,0,0,0,6],
        [0,0,0,0,0,0,0],
        [0,0,0,0,0,1,0] ]



node = 7
visited = []
distance = [float('inf')] * node
path = [None] * node

start = 0
distance[start] = 0
def printList(start, finish, distance, path):
    print('From V',start,' to V',finish)
    print('Distance : ', distance[finish])

    p = path[finish]
    while p is not None:
        print('V', p,end=', ')
        p = path[p]
    print('\n')

while len(visited) != node:
    shortest = float('inf')
    shortest_idx = start
    
    for i in range(node):
        if i not in visited and distance[i] < shortest:
            shortest = distance[i]
            shortest_idx = i
    
    visited.append(shortest_idx)

    for i in range(node):
        way = adj[shortest_idx][i]
        if way and way + shortest < distance[i]:
            distance[i] = way + shortest
            path[i] = shortest_idx

finish = 6

print(path)
print(distance)
printList(start, finish, distance, path)