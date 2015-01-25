import csv
import sys
import itertools

def getClusterInfo(cluster):
	pass

def getClusterDistance(clusterA, clusterAinfo, clusterB, clusterBinfo):
	pass

points = []

with open(sys.argv[1], 'r') as csvfile:
	pointReader = csv.reader(csvfile)
	for row in pointReader:
		points.append(list(row[i] for i in range(0, len(row))))

print points

clusters = [ list(point) for point in points]
print clusters
while len(clusters) > 1:
	rangeInfo = range(0, len(clusters))
	clusterInfo = []
	for cluster in clusters:
		clusterInfo.append(getClusterInfo(cluster))
	distances = []
	for combo in itertools.combinations(rangeInfo, rangeInfo):
		a = combo[0]
		b = combo[1]
		if a == b:
			continue
		distances.append((getClusterDistance(clusters[a], clusterInfo[a], clusters[b], clusterInfo[b]), a, b))
	print distances
	distances = sorted(distances, key=lambda x:x[0])
	merge = distances[0]
	a = distances[1]
	b = distances[2]
	if a > b:
		tmp = a
		a = b
		b = tmp
	clusters[a] = clusters[a] + clusters[b]
	del clusters[b]
	print clusters




