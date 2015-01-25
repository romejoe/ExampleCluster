import sys
from operator import sub
import math

from Cluster import Cluster

class SmallRadiusCluster(Cluster):
	def getClusterInfo(cluster):
		pass
	def getCentroid(cluster):
		sums = [0.0] * len(cluster[0])

		for i in range(0, len(cluster)):
			for j in range(0,len(sums)):
				sums[j] = sums[j] + cluster[i][j]
		sums = map(lambda x: x/len(cluster), sums)
		return sums


	def getClusterDistance(clusterA, clusterAinfo, clusterB, clusterBinfo):
		tmp = clusterA + clusterB
		centroid = self.getCentroid(tmp)
		
		return max(map(lambda t: math.sqrt(reduce(lambda s, t: s+t, map(lambda x,y: (x-y)**2, t, centroid))),tmp))
	
if __name__ == "__main__":
	fpath = sys.argv[1]
	clusterer = SmallRadiusCluster()

	clusterer.ClusterCSVFile(fpath, True)