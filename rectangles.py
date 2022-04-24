#!/usr/bin/env python3
import itertools
import numpy as np
import matplotlib.pyplot as plt

plt.figure(figsize=(24.0, 16.0))
plt.title('Find Rectangles')

# points = set([(1,1),(2,1),(3,1), (1,0), (2,0), (3,0)])
# points = set([(2,4),(4,2),(5,7),(7,5)]) # this is a rectangle not parallel to axis
# points = set([(1,1),(2,1),(3,1), (1,0), (2,0), (3,0),(2,4),(4,2),(5,7),(7,5)])
# points = set([(2,4),(4,2),(5,7),(7,5)])


coordinates = np.random.randint(30, size=(2,50))
points = set([ (coordinates[0][x],coordinates[1][x]) for x in range(len(coordinates[0]))])



print(points)
rectangles = set()

x = [x[0] for x in points]
y = [x[1] for x in points]

plt.scatter(x, y, color='green')


def isSquareTriangle(a,b,c):
	# get coordinates of each point a, b, c
	xa, ya = a
	xb, yb = b
	xc, yc = c
	# for this to be a possible rectangle the distances (squared)
	# must be in pythagoras relationship
	ab = (xb - xa) ** 2 + (yb - ya) ** 2
	ac = (xc - xa) ** 2 + (yc - ya) ** 2
	bc = (xc - xb) ** 2 + (yc - yb) ** 2
	# find the largest distance
	distances = [ab, ac, bc]
	distances.sort(reverse=True, key=int)
	diagonal, sides = distances[0], distances[1:]
	if diagonal != sum(sides):
		return False, [a,b,c]
	# now compute the position of the point that will close the square
	# find which points are the diagonal and return them in order 
	if ab == diagonal:
		return True, [a,c,b]
	elif ac == diagonal:
		return True, [a,b,c]
	else:
		return True, [b,a,c]


def computePoint(triangle):
	"""
	Computes the last point D in an ABC square triangle 
	where a and c are the diagonal - triangle = [a,b,c]
	            D--- C
	            |  / |
	            | /  |
	            |/   |
	            A----B
	"""
	# get coordinates of each point a, b, c
	a, b, c = triangle
	xa, ya = a
	xb, yb = b
	xc, yc = c
	# due to subtriangle congruence
	xd = xc - (xb - xa)
	yd = (ya -yb) + yc
	d = (xd, yd)
	return d

nonRect = 0
yesRect = 0
for a,b,c in itertools.combinations(points,3):
			isSquare, triangle = isSquareTriangle(a,b,c)
			if not isSquare:
				nonRect += 1
				continue
			# candidate, the points define a right angle, but can we close it with a rectangle?
			yesRect += 1
			d = computePoint(triangle)
			if d in points:
				rectangles.add(frozenset([a,b,c,d]))
				_rect = plt.Polygon([list(triangle[0]), list(triangle[1]), list(triangle[2]), list(d)], fill=True, edgecolor='r', alpha=0.2)
				plt.gca().add_patch(_rect)
			else:
				pass

plt.axis('equal')
plt.grid(axis='both', which='both')
plt.show()

print(rectangles)
print('number of rectangles is {}'.format(len(rectangles)))
print('number of rectangles is {} Total points {} non-Rect {} rect {}'.format(len(rectangles),len(points),nonRect,yesRect))
		
