from copy import deepcopy

def solution(tickets):
    answer = []
    graph = {}
    for ticket in tickets:
        a,b = ticket
        if a not in graph:
            graph[a] = []
        graph[a].append(b)


    def dfs(curr,visited):
        if curr not in graph and len(visited) != len(tickets):
            return

        if len(visited) == len(tickets):
            result = [k for k in visited.keys()]
            result = result[0].split("->") + [l.split("->")[-1] for l in result[1:-1]]+ [result[-1].split("->")[-1]]
            answer.append(result)
            return
        for next in graph[curr]:
            if f"{curr}->{next}" not in visited:
                tmp = deepcopy(visited)
                tmp[f"{curr}->{next}"]= True
                dfs(next, tmp)

    dfs("ICN",{})


    return sorted(answer,key=lambda x:(x[1:]))[0]


print(solution([['ICN','B'],['B','ICN'],['ICN','A'],['A','D'],['D','A']]))