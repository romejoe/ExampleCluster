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
	
	min = None
	for combo in itertools.product(clusterA, clusterB):
		tmp = distance(combo[0], combo[1])
		if min == None:
			min = tmp
		elif tmp < min:
			min = tmp
	return min
	

import sys
from operator import sub
import math

from Cluster import Cluster

class minDistanceCluster(Cluster):
	def _getClusterInfo(cluster):
		pass

	def distance(a,b):
		return math.sqrt(reduce(lambda s, t: s+t, map(lambda x,y: (x-y)**2, a, b)))

	def _getClusterDistance(clusterA, clusterAinfo, clusterB, clusterBinfo):
		min = None
		for combo in itertools.product(clusterA, clusterB):
			tmp = self.distance(combo[0], combo[1])
			if min == None:
				min = tmp
			elif tmp < min:
				min = tmp
		return min
	
if __name__ == "__main__":
	fpath = sys.argv[1]
	clusterer = minDistanceCluster()

	clusterer.ClusterCSVFile(fpath, True)