import csv
import sys
import itertools
from operator import sub
import math
def getClusterInfo(cluster):
	pass

def distance(a,b):
	return math.sqrt(reduce(lambda s, t: s+t, map(lambda x,y: (x-y)**2, a, b)))

def getClusterDistance(clusterA, clusterAinfo, clusterB, clusterBinfo):
	
	average =0.0
	count = 0 
	for combo in itertools.product(clusterA, clusterB):
		tmp = distance(combo[0], combo[1])
		average = average + tmp
		count = count + 1
		
	return average / count
	

points = []

with open(sys.argv[1], 'r') as csvfile:
	pointReader = csv.reader(csvfile)
	for row in pointReader:
		points.append([list(int(row[i]) for i in range(0, len(row)))])

print points

clusters = [ list(point) for point in points]
print clusters
iterCount = 0
while len(clusters) > 1:
	print "===Iter Start==="
	print "Iter:", iterCount
	rangeInfo = range(0, len(clusters))
	clusterInfo = []
	for cluster in clusters:
		clusterInfo.append(getClusterInfo(cluster))
	distances = []
	for combo in itertools.combinations(rangeInfo, 2):
		a = combo[0]
		b = combo[1]
		if a == b:
			continue
		distances.append((getClusterDistance(clusters[a], clusterInfo[a], clusters[b], clusterInfo[b]), a, b))
	#print distances
	distances = sorted(distances, key=lambda x:x[0])
	#print "Distances:"
	#for dist in distances:
	#	print dist[0], "\t", clusters[dist[1]], "\t", clusters[dist[2]]

	merge = distances[0]
	a = merge[1]
	b = merge[2]
	if a > b:
		tmp = a
		a = b
		b = tmp
		
	clusters[a] = clusters[a] + clusters[b]
	del clusters[b]
	print "clusters:"
	for x in clusters:
		print x 
	iterCount = iterCount +  1
	print "===Iter Done==="




