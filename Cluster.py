from abc import ABCMeta, abstractmethod

class Cluster:
	__metaclass__ = ABCMeta

	@abstractmethod
	def _getClusterInfo(cluster):
		pass

	def _getClusterDistance(clusterA, clusterAInfo, clusterB, clusterBInfo):
		pass

	def Cluster(clusters, verbose=False):
		iterCount = 0
		
		while( len(clusters) > 1):
			if verbose:
				print "===Iter Start==="
				print "Iter:", iterCount
			rangeInfo = range(0, len(clusters))
			clusterInfo = []
			for cluster in clusters:
				clusterInfo.append(self._getClusterInfo(cluster))
			
			MergeCandidate = None
			
			for combo in itertools.combinations(rangeInfo, rangeInfo):
				a = combo[0]
				b = combo[1]
				if a == b:
					continue
				tmp = (self._getClusterDistance(clusters[a], clusterInfo[a], clusters[b], clusterInfo[b]), a, b)
				if MergeCandidate == None or MergeCandidate[0] > tmp[0]:
					MergeCandidate = tmp

			if verbose:
				print MergeCandidate
			
			a = MergeCandidate[1]
			b = MergeCandidate[2]
			if a > b:
				tmp = a
				a = b
				b = tmp
			clusters[a] = clusters[a] + clusters[b]
			del clusters[b]
			if verbose:
				print "clusters:"
				for x in clusters:
					print x 
			iterCount = iterCount +  1
			if verbose:
				print "===Iter Done==="
		return clusters



	def ClusterCSVFile(filepath, verbose=False):
		points = []
		with open(filepath, 'r') as csvfile:
			pointReader = csv.reader(csvfile)
			for row in pointReader:
				points.append([list(float(row[i]) for i in range(0, len(row)))])
		clusters = [ list(point) for point in points]
		return self.Cluster(clusters, verbose)
