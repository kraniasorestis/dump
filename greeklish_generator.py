#!/bin/python

import time
from src import Nicks
intro = '''

########################   GREEKLISH WORDLIST GENERATOR ############################



This program is free software: you can redistribute it and/or modify
it under the terms of the GNU General Public License as published by
the Free Software Foundation, either version 3 of the License, or
(at your option) any later version.

This program is distributed in the hope that it will be useful,
but WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
GNU General Public License for more details.

 see <http://www.gnu.org/licenses/>

* Creator: Orestis Kranias
* kraniasorestis@protonmail.com
* www.github.com/kraniasorestis
* Copyright (C) 2016


For the Greek users:
An thelete na doulepsei swsta to programma na grafete orthografhmena!
(opws edw). Gia paradeigma ta kuria onomata me hta sto telos.
LATHOS: Orestis. --> SWSTO: Oresths. To wmega to grafoume me "w",
tous difthogkous kanonika, dld: mp - oxi b, nt - oxi d, gk - oxi g.
Ta dipla fwnhenta kanonika. ei, oi, ai, kai oxi 'i' kai 'e'.
ALLIWS DEN THA VGOYN OLOI OI DYNATOI SYNDYASMOI KWDIKWN!


DISCLAIMER: If you do anything illegal with this program, you could
end up in JAIL! I have no responsibility over how this will be used!
It's developed for penetration testers and security researchers!!
Not for wardriving!!


Type help to see more about this project.


'''


info = '''


About this project

This is a personalised greeklish dictionary creator, desingned for penetration
testing within Greece - but it can obviously be altered for use in other languages.
It's being developed to fill a gap in dictionary-attacks in Greece
which fail too often precisely because there is no good greeklish
dictionary similar to rockyou and because tools like cupp do not
help that much when it comes to Greek.

The premise: if you provide this program with info on your target
it will generate a wordlist (implementing a 'cupp-like thinking')
taylored specifically for your target, with greater chances of success
than a usual english dictionary, which is next to useless in Greece.

I didn't have the time to do any type checking to the input you give, so,
if you type words where you should be typing telephone numbers etc,
the crappy passwords that will be generated will be on you!'

Expect passwords in the hundreds of thousands at the very least.

Good luck!

'''


######################## GLOBAL CONSTANTS WE'LL NEED ##############################


minchar = 8    # min and max password characters - change this as you like
maxchar = 18



# these are lists of years and common sequences used in passwords - they will be used in reverse too
years = [1950,1951,1952,1953,1954,1955,1956,1957,1958,1959,1960,1961,1962,1963,1964,1965,1966,1967,1968,1969,1970,1971,1972,1973,1974,1975,1976,1977,1978,1979,1980,1981,1982,1983,1984,1985,1986,1987,1988,1989,1990,1991,1992,1993,1994,1995,1996,1997,1998,1999,2000,2001,2002,2003,2004,2005,2006,2007,2008,2009,2010,2011,2012,2013,2014,2015,2016,2017,2018,2019,2020]
sequences = [123,1234,12345,123456,1234567,12345678,123456789,123456789,135,1357,13579,1357911,135791113,246,2468,246810,24681012,2468101214]


# for the greeklish version of leet mode


leet_dict = {
	'a':'@',
	'w':'o',
	'o':'0',
	'gk':'g',
	'gg':'g',
	'mp':'b',
	'nt':'d',
	'h':'i',
	'y':'i',
	'u':'i',
	'f':'u',
	'v':'u',
	'ay':'ef',
	'ey':'ef',
	'au':'af',
	'eu':'ef',
	'ch':'x'
}


special_characters = ['!', '.', '@', '#', '$', '%']


olympiakos = ['thrillos', 'gayros', 'olympiakos', 'olympiakara', 'thira', 'gate', 'thrilara']
panathinaikos = ['panatha', 'panathinaikos', 'thira', 'gate', 'trifili', 'trifilara', 'vazelos', 'vazelos']
aek = ['original', 'aek', 'original', 'aek', 'aekara', 'thira', 'aekara', 'hanoumi', 'hanoumaki']
paok =['paok', 'toumpa', 'paoki', 'mpaok', 'paokara', 'mpaokara', 'voulgaros', 'salonika', 'thessaloniki', 'gate4', 'thira4']
ael = ['alogaki', 'visini', 'larisa', 'larsa', 'trakter', 'ael', 'aelara']
aris = ['skouliki', 'salonika', 'xarilaou', 'aris', 'arianos' ]


########################### THE FUNCTIONS ##############################



def names():        # populates the nameslist
	global surname
	global firstname

	while True:
		x = raw_input("\n[+] owner's surname - type 'end' if you don't know it > ")
		if x == "help":
			print info
		elif x == "end":
			pass
		else:
			surname = x
			nameslist.append(surname)

		y = raw_input("\n[+] owner's firstname - type 'end' if you don't know it' > ")
		if y == "help":
			print info
		elif y == "end":
			break
		else:
			firstname = y
			nameslist.append(firstname)
			nameslist.append(surname + firstname)
			if surname + firstname != firstname + surname:
				nameslist.append(firstname + surname)
		break

	print "\n[+] names of partner, child, possible nicknames, relatives, pets or best friends - type 'end' to move on > "
	while True:
		name = raw_input("[+] enter a name (or 'end') >  ")
		if name == "end":
			break
		elif name == "help":
			print info
		else:
			nameslist.append(name)


def list_nicks(l): # returns a list of names appended with nicknames
	nicks = []
	for i in l:
		nicks = nicks + Nicks.nickname(i)
	return nicks







def his_birth():    # create a list with dates of births
	while True:
		global birthdates
		x = raw_input("\n[+] target's birthdate in DDMMYYYY format (or 'end' if you don't know)>  ")
		if x == 'end':
			break
		elif len(x) == 8:
			birthdates += (x, x[2:], x[:4], x[:2]+'_'+x[2:4]+'_'+x[4:], x[:2]+'_'+x[2:4]+'_'+x[6:], x[:4]+x[6:], x[:2]+'_'+x[2:4], x[2:4]+'_'+x[4:], x[2:4]+'_'+x[6:])
			break
		else:
			print "DDMMYYYY requires 8 characters!"

def her_birth():
	while True:
		global birthdates
		x = raw_input("\n[+] partner's birthdate in DDMMYYYY format (or 'end' if you don't know)>  ")
		if x == 'end':
			break
		elif len(x) == 8:
			birthdates += (x, x[2:], x[:4], x[:2]+'_'+x[2:4]+'_'+x[4:], x[:2]+'_'+x[2:4]+'_'+x[6:], x[:4]+x[6:], x[:2]+'_'+x[2:4], x[2:4]+'_'+x[4:], x[2:4]+'_'+x[6:])
			break
		else:
			print "DDMMYYYY requires 8 characters!"

def kid_birth():
	while True:
		global birthdates
		x = raw_input("\n[+] child's birthdate in DDMMYYYY format (or 'end' if you don't know)>  ")
		if x == 'end':
			break
		elif len(x) == 8:
			birthdates += (x, x[2:], x[:4], x[:2]+'_'+x[2:4]+'_'+x[4:], x[:2]+'_'+x[2:4]+'_'+x[6:], x[:4]+x[6:], x[:2]+'_'+x[2:4], x[2:4]+'_'+x[4:], x[2:4]+'_'+x[6:])
			break
		else:
			print "DDMMYYYY requires 8 characters!"

def births():
	his_birth()
	her_birth()
	kid_birth()          # makes a list of variations of everyones birth dates


def telephone():
	print "\n[+] type his telephone numbers if you know them"
	while True:
		tel = raw_input("[+] telephone or 'end' to move on-->  ")
		if tel == "end":
			break
		elif tel == 'help':
			print info
		else:
			telephones.append(tel)


def interests():
	print "\n[+] additional keywords - (place of birth, favorite band or director any keyword you think useful)"
	while True:
		interest = raw_input("[+] enter an interest (or 'end') >  ")
		if interest == "end":
			break
		elif interest == "help":
			print info
		else:
			interestslist.append(interest)


def combine2 (a, b, new_l):    # Combine the string items of two lists to a new list & the final list
	global min_char
	global max_char
	n = 0
	while n < len(a):
		for i in b:
			if minchar <= len(str(a[n])+str(i)) and maxchar >= len(str(a[n])+str(i)):
				new_l.append(str(a[n]) + str(i))
				final_list.append(str(a[n]) + str(i))
		n += 1


def team_combine():
	print '''\n\nwhat's his favourite team?\n
	1) olympiakos
	2) panathinaikos
	3) AEK
	4) PAOK
	5) AEL
	6) Aris
	[+] type 'end' if you don't know or if you don't want to use this
	'''

	while True:
		x = raw_input("[+] pick the corresponding number (or 'end') >  ")
		if x == '1':
			loadf(olympiakos)
			combine2(nameslist, olympiakos, namesteams)
			combine2(namesteams, ['thira7', 'gate7', '7', 'oeo', 'ole'], namesteams_final)
			combine2(namesteams_final, years, namesteams_dates)
			break
		elif x == '2':
			loadf(panathinaikos)
			combine2(nameslist, panathinaikos, namesteams)
			combine2(namesteams, ['thira13', 'gate13', '13', 'oeo', 'ole'], namesteams_final)
			combine2(namesteams_final, years, namesteams_dates)
			break
		elif x == '3':
			loadf(aek)
			combine2(nameslist, aek, namesteams)
			combine2(namesteams, ['thira21', 'gate21', '21', 'oeo', 'ole'], namesteams_final)
			combine2(namesteams_final, years, namesteams_dates)
			break
		elif x == '4':
			loadf(paok)
			combine2(nameslist, paok, namesteams)
			combine2(namesteams, ['thira4', 'gate4', '4', 'oeo', 'ole'], namesteams_final)
			combine2(namesteams_final, years, namesteams_dates)
			break
		elif x == '5':
			loadf(ael)
			combine2(nameslist, ael, namesteams)
			combine2(namesteams, ['alogaki', 'oeo', 'ole'], namesteams_final)
			combine2(namesteams_final, years, namesteams_dates)
			break
		elif x == '6':
			loadf(aris)
			combine2(nameslist, aris, namesteams)
			combine2(namesteams, years, namesteams_dates)
			break
		elif x == 'end':
			break
		elif x == 'help':
			print info
		else:
			print "\nError: That wasn't in the list of options\nPlease type one of the numbers or 'end' to move on\n"


def loadf(x):      # append a list's items to the final list
	global min_char
	global max_char
	for i in x:
		if minchar <= len(str(i)) and maxchar >= len(str(i)):
			final_list.append(i)



def write_out(x):     # final function - creating the file with the wordlist
	mylist = file('wordlist_%s.txt' % time.strftime('%d-%m-%Y_%H:%M'), 'w')
	mylist.write(x)
	mylist.close
	print "[+] created a wordlist with %d passwords" % len(final_list)
	raw_input("\n\npress enter to exit")
	exit()



# Auxiliary functions   - functions to add some spice

def rev(l): # append a list with the reversed versions of its strings
	tmp = []
	for i in l:
		tmp.append(str(i)[::-1])
	for i in tmp:
		l.append(i)

def add_(l):   # add the '_' and '-' characters before the list's strings and reappend them to the list (to be used with years and sequences)
	tmp = []
	for i in l:
		tmp.append('_'+str(i))
		tmp.append('-'+str(i))
	for i in tmp:
		l.append(i)

def add_nums(l):   # add some numbers to a list's elements
	tmp = []
	new_l = []
	for i in range(0, 100):
		tmp.append(str(i))
		tmp.append('_'+str(i))
	for i in range(0, 10):
		tmp.append('0'+str(i))
	combine2(l, tmp, new_l)
	l = new_l

def capitalize(l):    # append the capitalized elements of a list to itself
	tmp = []
	for i in l:
		tmp.append(i.capitalize())
	for i in tmp:
		l.append(i)

def spec_chars():     # append a couple of special characters at the end of the passwords
	names_spec_chars = []
	double_spec_chars = []
	names_spec_chars_final = []
	combine2(nameslist, special_characters, names_spec_chars)
	combine2(special_characters, special_characters, double_spec_chars)
	combine2(nameslist, double_spec_chars, names_spec_chars_final)




# finally the greeklish version of the leet mode:


def replace(lst, s1, s2):
	for i in lst:
		if s1 in i:
			lst.append(i.replace(s1, s2))   # if a string in the list contains 's1', swap it for 's2'


def dic_rep(lst, dic):
	for k in dic:
		replace(lst, str(k), str(dic[k]))
	return lst     # do replacing for every pair in a dictionary


########################### MAIN PROGRAM ###############################



# first we add the reverse versions of the years and sequences in their lists

rev(years)
add_(years)
rev(sequences)
add_(sequences)

print intro

surname = 'x'   # surname's gonna be important - gotta have a placeholder for that
firstname = 'x' # same here and bellow

# Predefining some lists to be populated later

nameslist = []
teamslist = []
birthdates = []
telephones =[]
interestslist = []


# predefined combined lists (including reveresed versions of the ingredient lists)

namesbirthdates = []
namestelephones = []
namesyears = []
namessequences = []
namesteams = []
namesteams_final = []
namesteams_dates = []
namesinterests = []
interestsyears = []



final_list=[]   # defining the list and min and max characters of its contents

# Start the action

names()                 # start asking info
nameslist = nameslist + list_nicks(nameslist) # let's find some nicknames
capitalize(nameslist)
nameslist = dic_rep(nameslist, leet_dict)
rev(nameslist)          # reverse those names
loadf(nameslist)        # add them to the final list

births()                # ask for some more info
rev(birthdates)
add_(birthdates)
loadf(birthdates)

telephone()
rev(telephones)
add_(telephones)
loadf(telephones)

team_combine()      # bring football to the mix

add_nums(nameslist)

interests()             # what other interests we can mix
add_(interestslist)
loadf(interestslist)

combine2(nameslist, birthdates, namesbirthdates)    # combine the s**t out of them
combine2(nameslist, years, namesyears)
combine2(nameslist, sequences, namessequences)
combine2(nameslist, telephones, namestelephones)
combine2(nameslist, interestslist, namesinterests)
combine2(interestslist, years, interestsyears)

spec_chars()

paswd_list = "\n".join(final_list)	# Getting the list together
write_out(paswd_list)
