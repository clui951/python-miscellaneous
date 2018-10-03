from collections import defaultdict

def maxPoints(points):
	if len(points) <= 2:
		return len(points)

	maxPoints = 0
	for i in range(len(points)):
		slopeDict = defaultdict(int)
		ptA = points[i]
		for j in range(i, len(points)):
			ptB = points[j]
			slopeX = ptB[0] - ptA[0]
			slopeY = ptB[1] - ptA[1]
			if slopeX == 0:
				slopeDict['inf'] += 1
			elif slopeX == 0 and slopeY == 0:
				slopeDict['same'] += 1
			else:
				slope = slopeY / slopeX
				slopeDict[slope] += 1
		iterMax = max(slopeDict.values())
		if iterMax > maxPoints:
			maxPoints = iterMax

	return maxPoints

if __name__ == "__main__":
	print("=== maxPoints ===")
	points = [[1,1],[3,2],[5,3],[4,1],[2,3],[1,4]]
	assert maxPoints(points) == 3
	print("=== done! ===")
