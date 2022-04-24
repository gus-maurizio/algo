#!/usr/bin/env python3
import itertools
import numpy as np
import matplotlib.pyplot as plt
import math

plt.figure(figsize=(24.0, 16.0))
plt.title('Find (near) Equilateral Triangles')

# points = set([(1,1),(2,1),(3,1), (1,0), (2,0), (3,0)])
# points = set([(2,4),(4,2),(5,7),(7,5)]) # this is a rectangle not parallel to axis
# points = set([(1,1),(2,1),(3,1), (1,0), (2,0), (3,0),(2,4),(4,2),(5,7),(7,5)])
# points = set([(2,4),(4,2),(5,7),(7,5)])

POINTS=130
FACTOR=1.005
MAXDIMENSION = 50
coordinates = np.random.randint(MAXDIMENSION, size=(2,POINTS))
points = set([ (coordinates[0][x],coordinates[1][x]) for x in range(len(coordinates[0]))])

print(points)
triangles = set()

x = [x[0] for x in points]
y = [x[1] for x in points]

plt.scatter(x, y, color='green')

def isEquilateralTriangle(a,b,c):
	# get coordinates of each point a, b, c
	xa, ya = a
	xb, yb = b
	xc, yc = c
	# for this to be an equilateral triangle the distances (squared)
	# must be all equal ab = ac = bc
	ab = (xb - xa) ** 2 + (yb - ya) ** 2
	ac = (xc - xa) ** 2 + (yc - ya) ** 2
	bc = (xc - xb) ** 2 + (yc - yb) ** 2
	distances = [ab, ac, bc]
	# for equilateral
	# result = all(element == distances[0] for element in distances)
	# return result

	# almost equilateral!
	largest 	= max(distances)
	smallest 	= min(distances)
	if largest < smallest * FACTOR:
		# heron formula for area
		a 	 	= math.sqrt(ab)
		b		= math.sqrt(ac)
		c		= math.sqrt(bc)
		s		= (a + b + c) / 2
		area    = math.sqrt(s * (s - b) * (s - a) * (s - c))
		return True, largest/smallest, area, 2 * s
	else:
		return False, 0, 0, 0



nonEqui = 0
yesEqui = 0
for a,b,c in itertools.combinations(points,3):
			isEquilateral, factor, area, perimeter = isEquilateralTriangle(a,b,c)
			if not isEquilateral:
				nonEqui += 1
				continue
			yesEqui += 1
			triangles.add(frozenset([a,b,c]))
			_rect = plt.Polygon([a,b,c], fill=True, edgecolor='red', alpha=0.2)
			plt.gca().add_patch(_rect)
			print(f'{(a,b,c)} {factor:.5f} area {area:.2f} perimeter {perimeter:.2f}')

plt.axis('equal')
plt.grid(axis='both', which='both')
plt.show()

print(triangles)
print('number of triangles is {}'.format(len(triangles)))
print('number of triangles is {} Total points {} non {} yes {}'.format(len(triangles),len(points),nonEqui,yesEqui))
		
