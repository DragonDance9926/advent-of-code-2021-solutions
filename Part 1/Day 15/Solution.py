import sys
inf = sys.argv[1] if len(sys.argv) > 1 else 'input'
mapping = []
with open("input.txt") as f:
    for line in f:
        mapping.append(list(map(int,line[:-1])))

def inr(pos, arr):
	return pos[0] in range(len(arr)) and pos[1] in range(len(arr[0]))

q = [(0, 0, 0)]
costs = {}
while True:
	cost,x,y = q[0]
	if x==len(mapping)-1 and y==len(mapping[0])-1:
		print(cost)
		break
	q=q[1:]
	for xx,yy in [(x+1,y),(x-1,y),(x,y-1),(x,y+1)]:
		if inr((xx,yy),mapping):
			nc = cost + mapping[xx][yy]
			if (xx,yy) in costs and costs[(xx,yy)]<=nc:
				continue
			costs[(xx,yy)]=nc
			q.append((nc,xx,yy))
	q = sorted(q)