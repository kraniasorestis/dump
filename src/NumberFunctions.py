import Setup
from AuxFunctions import combine2

minchar = Setup.minchar
maxchar = Setup.maxchar

def common_nums():    # provide a list with common pswrds like 00000000
	tmp = []
	for i in range (minchar, maxchar+1):
		tmp.append('1'*i)
		tmp.append('0'*i)
		tmp.append(' '*i)
		tmp.append('x'*i)
		tmp.append('X'*i)
	return tmp


def add_nums(l):   # add some numbers to the back a list's elements
    tmp = []
    for i in range(0, 100):
        tmp.append(str(i))
        tmp.append('_'+str(i))
    for i in range(0, 10):
        tmp.append('0'+str(i))
    return combine2(l, tmp)
