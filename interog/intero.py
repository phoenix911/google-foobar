from operator import itemgetter

def answer(minions):
	ratio_list = [(0.0 + minion[0])/((0.0 + minion[1])/minion[2])  for minion in minions]
	return [minion[0] for minion in sorted(list(enumerate(ratio_list)), key=itemgetter(1))]