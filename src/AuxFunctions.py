# Auxiliary functions   - functions to add some spice



def add_(l):   # add the '_' and '-' characters before the list's strings and reappend them to the list (to be used with years and sequences)
	tmp = []
	for i in l:
		tmp.append('_'+str(i))
		tmp.append('-'+str(i))
	for i in tmp:
		l.append(i)


def capitalize(l):    # append the capitalized elements of a list to itself
	tmp = []
	for i in l:
		tmp.append(i.capitalize())
	for i in tmp:
		l.append(i)
