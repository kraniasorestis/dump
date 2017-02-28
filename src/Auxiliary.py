import time, Setup


def chop(l):      # returns a list's items that they are within a length range
    tmp = []
    for i in l:
        if Setup.minchar <= len(str(i)) and Setup.maxchar >= len(str(i)):
            tmp.append(str(i))
    return tmp

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

def rev(l): # append a list with the reversed versions of its strings
    tmp = []
    for i in l:
        tmp.append(str(i)[::-1])
    for i in tmp:
        l.append(i)

def spec_chars(l):     # append a couple of special characters at the end of the passwords
    return combine2(l, Setup.SpecChars)

def bi_spec_chars(l):
    double_spec_chars = combine2(Setup.SpecChars, Setup.SpecChars)
    return combine2(l, double_spec_chars)

def combine2 (a, b):    # return the combinations of 2 lists' items
    tmp = []
    n = 0
    while n < len(a):
        for i in b:
            if Setup.minchar <= len(str(a[n])+str(i)) and Setup.maxchar >= len(str(a[n])+str(i)):
                tmp.append(str(a[n]) + str(i))
        n += 1
    return tmp

def one_char_psw():    # provide a list with common pswrds like 00000000
	tmp = []
	for i in range (Setup.minchar, Setup.maxchar+1):
		tmp.append('1'*i)
		tmp.append('0'*i)
		tmp.append(' '*i)
		tmp.append('x'*i)
		tmp.append('X'*i)
        tmp.append('a'*i)
	return tmp

############## A leet-like couple of functions for greeklish #########################

def replace(lst, s1, s2):
    for i in lst:
        if s1 in i:
            lst.append(i.replace(s1, s2))   # if a string in the list contains 's1', swap it for 's2'

def dic_rep(lst, dic):
    for k in dic:
        replace(lst, str(k), str(dic[k]))
    return lst     # do replacing for every pair in a dictionary

######################################################################################


def write_out(x, final_list):     # final function - creating the file with the wordlist
    mylist = file('wordlist_%s.txt' % time.strftime('%d-%m-%Y_%H:%M'), 'w')
    mylist.write(x)
    mylist.close
    print "[+] created a wordlist with %d passwords" % len(final_list)
    raw_input("\n\npress enter to exit")
    exit()
