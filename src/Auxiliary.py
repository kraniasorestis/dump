import time, Setup
import random

def choose_word (wordlist):
       return random.choice (wordlist)

def chop(l):      # returns a list's items that are within a certain length range
    tmp = []
    for i in l:
        if Setup.minchar <= len(str(i)) and Setup.maxchar >= len(str(i)):
            tmp.append(str(i))
    return tmp

def add_(l):   # add the '_', '-' and '.' characters before the list's strings
    tmp = []
    for i in l:
        tmp.append('_'+str(i))
        tmp.append('-'+str(i))
        tmp.append('.'+str(i))
    return tmp

def capitalize(l):    # capitalizes the first letter of every element of a list and reappends them to the list 
    tmp = []
    for i in l:
        tmp.append(i.capitalize())
    return tmp

def rev(l): # append a list with the reversed versions of its strings
    tmp = []
    for i in l:
        tmp.append(str(i)[::-1])
    return tmp


def combine2way (a, b):    # appends list b to a from both front and back
    tmp = []
    for n in range(len(a)):
        for i in b:
            if Setup.minchar <= len(str(a[n])+str(i)) and Setup.maxchar >= len(str(a[n])+str(i)):
                tmp.append(str(a[n]) + str(i))
    for n in range(len(b)):
        for i in a:
            if Setup.minchar <= len(str(b[n])+str(i)) and Setup.maxchar >= len(str(b[n])+str(i)):
                tmp.append(str(b[n]) + str(i))
    return tmp

def combine (a, b):    # appends list b to to the back of list's a elements, chopped to a character length range
    tmp = []
    for n in range(len(a)):
        for i in b:
            if Setup.minchar <= len(str(a[n])+str(i)) and Setup.maxchar >= len(str(a[n])+str(i)):
                tmp.append(str(a[n]) + str(i))
    return tmp

def combine_front (a, b):    # appends list b to to the back of list's a elements, chopped to a character length range
    tmp = []
    for n in range(len(a)):
        for i in b:
            if Setup.minchar <= len(str(a[n])+str(i)) and Setup.maxchar >= len(str(a[n])+str(i)):
                tmp.append(str(i) + str(a[n]))
    return tmp


def spec_chars(l):     # append special characters at the end of list l's items
    return combine(l, Setup.SpecChars)


def soccer_mix(omada, names, dates):
    list1 = combine(names, omada)
    list2 = combine(list1, omada)
    list3 = combine(list1, Setup.years)
    list4 = combine(list2, Setup.years)
    list5 = combine(omada, Setup.years)
    list6 = combine(omada, dates)
    return omada + list1 + list2 + list3 + list4 + list5 + list6

def soccer(names, dates):
    print '''\n\nwhat's his favourite team?

       1) Olympiakos
       2) Panathinaikos
       3) AEK
       4) PAOK
       5) AEL
       6) Aris

    [+] press ENTER if you don't know or if you don't want to use this
    '''

    while True:
        x = raw_input("[+] pick the corresponding number (or ENTER to move on) >  ")
        tmp = []
        if x == '':
            break
        elif int(x) >= 1 and int(x) <= 6:
            tmp = soccer_mix(Setup.team_dic[int(x)], names, dates)
            break
        else:
            print "\nError: That wasn't in the list of options\nType one of the numbers or press ENTER to move on\n"
    return tmp

def wikipedia_unlink(l):
    tmp = []
    for i in l:
        if i[-3:] == 'rft':
            tmp.append(i[:-3])
        else:
            tmp.append(i)
    set(tmp)
    return tmp

def nickname(n):   # create nicknames for each name based on gender
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
    nicks.append(s[:-2]+'oulhs')
    return nicks


def nicknames(l): # returns a list of names appended with nicknames
	nicks = []
	for i in l:
		nicks = nicks + nickname(i)
	return nicks

def check_nicks(l):
    tmp = []
    for i in l:
        if i in Setup.nic_dic:
            tmp += Setup.nic_dic.get(i)
        else:
            tmp += nickname(i) 
    return tmp

def one_char_psw():    # provide a list with common pswrds like 00000000
    tmp = []
    for i in range (Setup.minchar, Setup.maxchar+1):
        tmp.append('0'*i)
        tmp.append('1'*i)
        tmp.append('6'*i)
        tmp.append(' '*i)
        tmp.append('x'*i)
        tmp.append('X'*i)
        tmp.append('a'*i)
        tmp.append('z'*i)
    return tmp


############## A leet-like couple of functions for greeklish #########################

def replace(l, s1, s2):        # if a string in the list contains 's1', swap it for 's2'
    for i in l:
        if s1 in i:
            l.append(i.replace(s1, s2))   

def leet_rep(l, dic):       # do replacing for every pair in a dictionary
    for k in dic:
        replace(l, str(k), str(dic[k]))
    return l     

def leet(l):
    tmp = []
    tmp += leet_rep(l, Setup.leet_dict)
    tmp += leet_rep(l, Setup.leet_dict_2)
    return tmp

######################################################################################


def write_out(x, final_list):     # final function - creating the file with the wordlist
    mylist = file('wordlist_%s.txt' % time.strftime('%d-%m-%Y_%H:%M'), 'w')
    mylist.write(x)
    mylist.close
    print "\n[+] created a wordlist with %d passwords" % len(final_list)
    raw_input("\n\npress enter to exit")
    exit()



