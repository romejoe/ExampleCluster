import sys
from operator import sub
import math

from Cluster import Cluster

class centroidCluster(Cluster):
	def _getClusterInfo(cluster):
		sums = [0.0] * len(cluster[0])
		
		for i in range(0, len(cluster)):
			for j in range(0,len(sums)):
				sums[j] = sums[j] + cluster[i][j]
	#	print sums
		sums = map(lambda x: x/len(cluster), sums)
		print "centroid,", sums
		return sums

	def _getClusterDistance(clusterA, clusterAinfo, clusterB, clusterBinfo):
		return math.sqrt(reduce(lambda x,y: x+y, map(lambda x,y: (x-y)**2, clusterAinfo, clusterBinfo)))
	
if __name__ == "__main__":
	fpath = sys.argv[1]
	clusterer = centroidCluster()

	clusterer.ClusterCSVFile(fpath, True)