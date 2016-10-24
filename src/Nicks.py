def nickname(n):   # use a nickname function for each name based on gender
	nicks = []
	if n[-2:] == 'hs' or n[-2:] == 'os' or n[-2:] == 'as':
		nicks = male_nicks(n)
	else:
		nicks = fem_nicks(n)
	return nicks

def fem_nicks(s):  # create female nicknames
	nicks = []
	if s[-2:] == 'ia':
		nicks.append(s[:-2]+'oula')
		nicks.append(s[:-2]+'aki')
		nicks.append(s[:-2]+'itsa')
	else:
		nicks.append(s[:-1]+'oula')
		nicks.append(s[:-1]+'aki')
		nicks.append(s[:-1]+'itsa')
	return nicks

def male_nicks(s):  # create male nicknames
	nicks = []
	nicks.append(s[:-2]+'aras')
	nicks.append(s[:-2]+'akhs')
	nicks.append(s[:-2]+'akos')
	return nicks
