import csv
import sys
import itertools
from operator import sub
import math
def getClusterInfo(cluster):
	pass
def getCentroid(cluster):
	sums = [0.0] * len(cluster[0])
	

	for i in range(0, len(cluster)):
		for j in range(0,len(sums)):
			sums[j] = sums[j] + cluster[i][j]
#	print sums
	sums = map(lambda x: x/len(cluster), sums)
	#for i in range(0, len(sums)):
		#sums[i] = sums[i] / len(clusters)
	#print "centroid,", sums
	return sums


def getClusterDistance(clusterA, clusterAinfo, clusterB, clusterBinfo):
	tmp = clusterA + clusterB
	centroid = getCentroid(tmp)
	
	return max(map(lambda t: math.sqrt(reduce(lambda s, t: s+t, map(lambda x,y: (x-y)**2, t, centroid))),tmp))
	#return abs(clusterAinfo - clusterBinfo)
	

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
	print "Distances:"
	for dist in distances:
		print dist[0], "\t", clusters[dist[1]], "\t", clusters[dist[2]]

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




