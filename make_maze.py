import random
n = int(input("arithmos grammwn kai sthlwn(< 30): "))
start_x = int(input("start x: "))
start_y = int(input("start y: "))
seed = input("seed: ")
outputfile = input("onoma arxeiou: ")
grafos = {};
visited = {};
for i in range(0,n):
    for j in range(0,n):
        visited.update({(i,j) : False});
        if i == 0:
            if j == 0:
                grafos.update({(i,j) : [(i+1,j), (i,j+1)]});
            elif j == n-1:
                grafos.update({(i,j) : [(i+1,j), (i,j-1)]});
            else:
                grafos.update({(i,j) : [(i+1,j), (i,j+1), (i,j-1)]});
        elif j == 0:
                if i == 0:
                     grafos.update({(i,j) : [(i+1,j), (i,j+1)]});
                elif i == n-1:
                     grafos.update({(i,j) : [(i-1,j), (i,j+1)]});
                else:
                     grafos.update({(i,j) : [(i+1,j), (i,j+1),(i-1,j)]});
         elif i == n-1:
                if j == 0:
                    grafos.update({(i,j) : [(i-1,j), (i,j+1)]});
                elif j == n-1:
                    grafos.update({(i,j) : [(i-1,j), (i,j-1)]});
                else:
                    grafos.update({(i,j) : [(i-1,j), (i-1,j-1), (i-1,j+1)]});
        elif j == n-1:
                if i == 0:
                    grafos.update({(i,j) : [(i+1,j), (i,j-1)]});
                elif i == n-1:
                    grafos.update({(i,j) : [(i-1,j), (i,j-1)]});
                else:
                    grafos.update({(i,j) : [(i-1,j), (i,j-1), (i+1,j)]});
        else:
                grafos.update({(i,j) : [(i+1,j), (i,j+1), (i-1,j), (i,j-1)]});

file = open(outputfile, "w")
def firstsearch(adj, start_x, visit, visited={}):
    if start_x == visit:
        return True
    if adj[start_x]:
        for komvos in filter(lambda x: x not in visited, graph[start_x]):
            visited.append(komvos)
            if firstsearch(adj, komvos, vidit, visited):
                return True
            return False
        file.write('maze')

file.close();
        
