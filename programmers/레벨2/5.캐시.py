from collections import deque
def solution(cacheSize, cities):
    answer = 0
    queue = deque([])
    for city in cities:
        city = city.lower()
        if len(queue) < cacheSize and city not in queue:
            queue.appendleft(city)
            answer += 5
        elif len(queue) <= cacheSize and city in queue:
            queue.remove(city)
            queue.appendleft(city)
            answer += 1
        elif len(queue) == cacheSize and city not in queue:
            if len(queue) > 0:
                queue.pop()
                queue.appendleft(city)
            answer += 5

    print(answer)

    return answer



solution(2, ["Jeju", "Pangyo", "NewYork", "newyork"])