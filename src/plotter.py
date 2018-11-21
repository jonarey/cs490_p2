
import sys
import matplotlib.pyplot as plt
from pylab import *
from matplotlib.collections import LineCollection
from matplotlib.collections import CircleCollection
from matplotlib.colors import colorConverter

if len( sys.argv ) >= 2:
	fileName = sys.argv[1]
else:
	print 'Enter a filename'
	exit()
ax = axes()
file = open(fileName, 'r' )


segs = []
minx = 0
maxx = 0
miny = 0
maxy = 0
count = 0
for line in file:
	numbers = line.split()
	if len( numbers ) < 4:
		continue
	elif len( numbers ) == 4:
		try:
			x1 = float( numbers[0]  )
			y1 = float( numbers[1] )
			x2 = float( numbers[2] )
			y2 = float( numbers[3] )
		except ValueError:
			continue
	elif len( numbers ) == 6:
		try:
			x1 = float( numbers[0]  )
			y1 = float( numbers[1] )
			x2 = float( numbers[2] )
			y2 = float( numbers[3] )
		except ValueError:
			continue
	else:
		continue
	segs.append( [ [ x1,  y1 ], [x2 ,  y2 ] ]  )
	if count == 0:
		minx = x1
		maxx =x2
		miny =  y1
		maxy =  y2
	
	if x1 < minx:
		minx = x1
	if x2 < minx:
		minx = x2
	if x1 > maxx:
		maxx = x1
	if x2 > maxx:
		maxx = x2
	if y1 < miny:
		miny = y1
	if y2 < miny:
		miny = y2
	if y1 > maxy:
		maxy = y1
	if y2 > maxy:
		maxy = y2
	
	
	count = count+1
	#x1.append( float( numbers[0] ) )
	#y1.append(  float( numbers[1] ) )
	#x2.append(  float( numbers[2] ) )
	#y2.append(  float( numbers[3] ) )

ax.set_xlim((minx,maxx))
ax.set_ylim((miny,maxy))

colors = [colorConverter.to_rgba(c) for c in ('r','g','b','c','y','m','k')]
print 'make a collection'
line_segments = LineCollection( segs, # Make a sequence of x,y pairs
                                linewidths    = (1),
                                linestyles = 'solid',
				colors = colors)
print 'formatting input'

offs = []
for s in segs:
	offs.append( (s[0][0], s[0][1]) )
#print offs
#circles = CircleCollection(sizes=(50,), offsets = offs ) 
print 'adding to collection'
ax.add_collection(line_segments)
#ax.add_collection(circles)

print 'plot it'
#plt.plot([x for (x,y) in offs], [y for (x,y) in offs], 'bo' )
#sci(line_segments) 
show()
