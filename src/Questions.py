from Auxiliary import combine2
import Setup

def names():        # populates the nameslist
    tmp=[]
    while True:
        surname = raw_input("\n[+] target's surname - press ENTER if you don't know it > ")
        if surname == "":
            pass
        else:
            tmp.append(surname)

        firstname = raw_input("\n[+] target's firstname - press ENTER if you don't know it' > ")
        if firstname == "":
            break
        else:
            tmp.append(firstname)
            tmp.append(surname + firstname)
            tmp.append(firstname + surname)
            break

    print "\n[+] names of partner, child, possible nicknames, relatives, pets or best friends - press ENTER to move on > "
    while True:
        name = raw_input("[+] enter a name (or press ENTER) >  ")
        if name == "":
            break
        else:
            tmp.append(name)
    return  tmp


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

def nicknames(l): # returns a list of names appended with nicknames
	nicks = []
	for i in l:
		nicks = nicks + nickname(i)
	return nicks


def births():    # create a list with variations on dates of birth
    tmp=[]
    print "\n[+] If you know any birthdates (target's, his/her partner's or kid's) enter them here:"
    while True:
        x = raw_input("[+] Relevant birthdate in DDMMYYYY format (or press ENTER to move on)>  ")
        if x == '':
            break
        elif len(x) == 8:
            tmp += (x, x[2:], x[:4], x[:2]+'_'+x[2:4]+'_'+x[4:], x[:2]+'_'+x[2:4]+'_'+x[6:], x[:4]+x[6:], x[:2]+'_'+x[2:4], x[2:4]+'_'+x[4:], x[2:4]+'_'+x[6:])
        else:
            print "DDMMYYYY requires 8 characters!"
    return tmp


def telephone():
    tmp = []
    print "\n[+] Type his telephone numbers if you know them"
    while True:
        tel = raw_input("[+] Telephone (or press ENTER to move on) >  ")
        if tel == "":
            break
        else:
            tmp.append(tel)
    return tmp


def interests():
    tmp = []
    print "\n[+] Additional keywords - (place of birth, favorite band/director/game or any keyword you think might be useful)"
    while True:
        interest = raw_input("[+] enter an interest (or ENTER) >  ")
        if interest == "":
            break
        else:
            tmp.append(interest)
    return tmp
