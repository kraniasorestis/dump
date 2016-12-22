from src import Setup

minchar = Setup.minchar
maxchar = Setup.maxchar


def common_nums():    # populate the final list with common pswrds like 000000000000
	tmp = []
	for i in range (minchar, maxchar+1):
		tmp.append('0'*i)
		tmp.append('1'*i)
		tmp.append(' '*i)
		tmp.append('x'*i)
		tmp.append('X'*i)
	return tmp

