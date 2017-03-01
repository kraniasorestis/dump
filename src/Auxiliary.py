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
    for n in range(len(a)):
        for i in b:
            if Setup.minchar <= len(str(a[n])+str(i)) and Setup.maxchar >= len(str(a[n])+str(i)):
                tmp.append(str(a[n]) + str(i))
    for n in range(len(b)):
        for i in a:
            if Setup.minchar <= len(str(b[n])+str(i)) and Setup.maxchar >= len(str(b[n])+str(i)):
                tmp.append(str(b[n]) + str(i))
    return tmp



def soccer_mix(omada, names, dates):
    list1 = combine2(names, omada)
    list2 = combine2(list1, omada)
    list3 = combine2(list1, Setup.years)
    list4 = combine2(list2, Setup.years)
    list5 = combine2(omada, Setup.years)
    list6 = combine2(omada, dates)
    return omada + list1 + list2 + list3 + list4 + list5 + list6

def soccer(names, dates):
    print '''\n\nwhat's his favourite team?

                                       __
                                      /88&
                                     /8^^8&
                                    /88  88&
                                   /88    88&
                                  /88      88&
                                 /88   ##   88&
                                /88    ##    88&
                               /88     ##     88&
                              /88      ##      88&
                             /88       ##       88&
                            /88                  88&
                           /88         ##         88&
                          /88          ##          88&
                          YY\ ____________________ /YY
                           \&&&&&&&&&&&&&&&&&&&&&&&&/
                                    
    [!][!][!][!][!][!][!][!][!][!][!][!][!][!][!][!][!][!][!][!][!][!][!][!][!]
    [!]  Depending on your Setup.py configuration & the input you've given, [!]
    [!]          this option may make your wordlist so huge                 [!]
    [!]                   that python may even crash.                       [!]
    [!]      In case of a memory error, retry with fewer names              [!] 
    [!]                or cut back on your settings' scope                  [!]
    [!][!][!][!][!][!][!][!][!][!][!][!][!][!][!][!][!][!][!][!][!][!][!][!][!]

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
            print '\n[!] Wait a couple of mins for this to finish... [!]\n'
            tmp = soccer_mix(Setup.team_dic[int(x)], names, dates)
            break
        else:
            print "\nError: That wasn't in the list of options\nType one of the numbers or press ENTER to move on\n"
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
    return tmp


############## A leet-like couple of functions for greeklish #########################

def replace(lst, s1, s2):
    for i in lst:
        if s1 in i:
            lst.append(i.replace(s1, s2))   # if a string in the list contains 's1', swap it for 's2'

def leet_rep(lst, dic):
    for k in dic:
        replace(lst, str(k), str(dic[k]))
    return lst     # do replacing for every pair in a dictionary


######################################################################################


def write_out(x, final_list):     # final function - creating the file with the wordlist
    mylist = file('wordlist_%s.txt' % time.strftime('%d-%m-%Y_%H:%M'), 'w')
    mylist.write(x)
    mylist.close
    print "\n[+] created a wordlist with %d passwords" % len(final_list)
    raw_input("\n\npress enter to exit")
    exit()
