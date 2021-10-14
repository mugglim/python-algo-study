n = 5

def printStar(n):
	mid = n // 2
	for i in range(n):
		if i == 0 or i == n -1:
			print("*" * n)
		else:
			tmp = ["*" if j == 0 or j == n-1 else " " for j in range(n)]
			l,r = 0,0
			if i <= mid:
				l,r = [i,n-i-1]
			else:
				l,r = [2*mid-i, i]

			tmp[l], tmp[r] = ["*", "*"]
			print(''.join(tmp))


printStar(8);

# 1) start or end => all
# 2-1) idx <= (n/2)
# 	s = [idx+n, n-idx]
# 2-2) idx  [n//2-idx, n//2+idx]

