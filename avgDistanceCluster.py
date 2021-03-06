import sys
from operator import sub
import math

from Cluster import Cluster

class avgDistanceCluster(Cluster):
	def _getClusterInfo(cluster):
		pass

	def distance(a,b):
		return math.sqrt(reduce(lambda s, t: s+t, map(lambda x,y: (x-y)**2, a, b)))

	def _getClusterDistance(clusterA, clusterAinfo, clusterB, clusterBinfo):
		
		average =0.0
		count = 0 
		for combo in itertools.product(clusterA, clusterB):
			tmp = self.distance(combo[0], combo[1])
			average = average + tmp
			count = count + 1
			
		return average / count
	
if __name__ == "__main__":
	fpath = sys.argv[1]
	clusterer = avgDistanceCluster()

	clusterer.ClusterCSVFile(fpath, True)