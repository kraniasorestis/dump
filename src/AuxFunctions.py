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



# A leet-like couple of functions for greeklish

def replace(lst, s1, s2):
	for i in lst:
		if s1 in i:
			lst.append(i.replace(s1, s2))   # if a string in the list contains 's1', swap it for 's2'

def dic_rep(lst, dic):
	for k in dic:
		replace(lst, str(k), str(dic[k]))
	return lst     # do replacing for every pair in a dictionary
