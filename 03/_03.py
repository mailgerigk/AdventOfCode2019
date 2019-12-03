_a = open("input.txt").readlines()[0].split(',')
_b = open("input.txt").readlines()[1].split(',')

def between(v,a,b):
	return (a < b and a <= v and v <= b) or (b <= v and v <= a)

def get_lines(a):
	lines = [(0,0)]
	for cmd in a:
		if cmd[0] == "R":
			lines += [(lines[-1][0] + int(cmd[1:]), lines[-1][1])]
		elif cmd[0] == "L":
			lines += [(lines[-1][0] - int(cmd[1:]), lines[-1][1])]
		elif cmd[0] == "U":
			lines += [(lines[-1][0], lines[-1][1] + int(cmd[1:]))]
		elif cmd[0] == "D":
			lines += [(lines[-1][0], lines[-1][1] - int(cmd[1:]))]
	return lines

def intersect(x1, y1, x2, y2, x3, y3, x4, y4):
	x12 = x1 - x2
	x34 = x3 - x4
	y12 = y1 - y2
	y34 = y3 - y4
	c = x12 * y34 - y12 * x34

	if abs(c) < 1:
		return 9999
	a = x1 * y2 - y1 * x2
	b = x3 * y4 - y3 * x4
	x = (a * x34 - b * x12) / float(c)
	y = (a * y34 - b * y12) / float(c)
	if between(x, x1, x2) and between(x,x3,x4) and between(y,y1,y2) and between(y,y3,y4):
		return abs(x) + abs(y)
	return 9999

def find_intersections(lines_a, lines_b):
	distance = 9999
	for i_a in range(len(lines_a) - 1):
		for i_b in range(len(lines_b) - 1):
			dst = intersect(lines_a[i_a][0], lines_a[i_a][1], lines_a[i_a+1][0], lines_a[i_a+1][1], lines_b[i_b][0], lines_b[i_b][1], lines_b[i_b + 1][0], lines_b[i_b + 1][1])
			if dst > 0:
				distance = distance if distance < dst else dst
	return distance

lines_a = get_lines(_a)
lines_b = get_lines(_b)	

dst = find_intersections(lines_a, lines_b)

print(dst)