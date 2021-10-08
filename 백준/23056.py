# 청팀=홀수, 백팀=짝수
# 1) 청팀을 먼저, 백팀을 나중에 출력한다.
# 2) 각각의 팀에 대해 학급을 오름차순으로 출력한다.
# 3) 각각의 학급에 대해 학생의 이름을 길이가 짧은 것부터, 길이가 같다면 사전 순으로 출력한다.

n,m = map(int,input().split())
team = [[] for _ in range(n)]


while True:
	a,b = input().split()
	if a == '0' and b == '0': break

	if len(team[int(a)-1]) < m:
		team[int(a)-1].append(b)

for i in range(n//2):
	t = sorted(team[2*i], key=lambda x:len(x));
	for player in t:
		print(f'{2*i+1} {player}')

for i in range(n//2):
	t = sorted(team[2*(i+1)-1], key=lambda x:(len(x),x));
	for player in t:
		print(f'{2*(i+1)} {player}')