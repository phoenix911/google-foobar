from operator import itemgetter

def answer(meetings):
    a = sorted(meetings)
    solutions = [[a[0]]]
    maxm = 1
    for i in xrange(1, len(a)):
    	for solution in solutions:
    		if a[i][0] >= solution[-1][1]:
    			solution.append(a[i])
    			if len(solution) > maxm:
    				maxm = len(solution)
    	solutions.append([a[i]])
    return maxm

a = [[0, 1],[4, 5] ,[1, 2], [2, 3], [3, 5]]
#a = [[0, 1000000], [42, 43], [0, 1000000], [42, 43]]

print answer(a)
