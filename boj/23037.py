n = int(input())
dic = {}

for _ in range(n):
	book = input()
	
	if book in dic: dic[book] += 1
	else: dic[book] = 1

bookList = list(zip(dic.keys(),dic.values()))

bookList.sort(key=lambda x:(-x[1],x[0]))

print(bookList[0][0])