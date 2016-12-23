#!/bin/python

from src import Nicks, Setup, RestFunctions, AuxFunctions, NumberFunctions
# intro = '''
#
# #############################################################
#
#
#     ########     ####    ####  #####    #####  ########
#     ##########   ####    ####  ######  ######  #########
#     ###   #####  ####    ####  ##############  ###   ###
#     ###    ####  ####    ####  #### #### ####  #########
#     ###    ####  ####    ####  ####  ##  ####  ########
#     ###   #####  #####  ####   ####      ####  ####
#     ##########    #########    ####      ####  ####
#     ########       #######     ####      ####  ####
#
#
# ######## a DUMP of UNBELIEVABLY MEDIOCRE PASSWORDS #########
#
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
#  see <http://www.gnu.org/licenses/>
#
# * Creator: Orestis Kranias
# * kraniasorestis@protonmail.com
# * www.github.com/kraniasorestis
# * Copyright (C) 2016
# * Contributor: Panagiwtis Simakis - https://github.com/sp1thas
#
#
# For the Greek users:
# An thelete na doulepsei swsta to programma na grafete orthografhmena!
# (opws edw). Gia paradeigma ta kuria onomata me hta sto telos.
# LATHOS: Orestis. --> SWSTO: Oresths. To wmega to grafoume me "w",
# tous difthogkous kanonika, dld: mp - oxi b, nt - oxi d, gk - oxi g.
# Ta dipla fwnhenta kanonika. ei, oi, ai, kai oxi 'i' kai 'e'.
# ALLIWS DEN THA VGOYN OLOI OI DYNATOI SYNDYASMOI KWDIKWN!
#
# Ean thelete na rythmisete posous xarakthres 8a exoun oi telikoi kwdikoi,
# aytes oi rythmiseis vriskontai sto /src/Setup.py
# To default einai apo 8 ews 18 (optimized gia wifi attacks).
#
# DISCLAIMER: If you do anything illegal with this program, you could
# end up in JAIL! I have no responsibility over how this will be used!
# It's developed for penetration testers and security researchers!!
# Not for wardriving!!
#
#
# #############################################################
#
#
#     ########     ####    ####  #####    #####  ########
#     ##########   ####    ####  ######  ######  #########
#     ###   #####  ####    ####  ##############  ###   ###
#     ###    ####  ####    ####  #### #### ####  #########
#     ###    ####  ####    ####  ####  ##  ####  ########
#     ###   #####  #####  ####   ####      ####  ####
#     ##########    #########    ####      ####  ####
#     ########       #######     ####      ####  ####
#
#
# ######## a DUMP of UNBELIEVABLY MEDIOCRE PASSWORDS #########
#
#
# '''


######################## GLOBAL CONSTANTS WE'LL NEED ##############################


minchar = Setup.minchar    # min and max password characters - change this as you like
maxchar = Setup.maxchar



# these are lists of years and common sequences used in passwords - they will be used in reverse too
years = Setup.years()
sequences = Setup.sequences()
pop_pswd = Setup.pop_pswd()
common_nums = NumberFunctions.common_nums()

# for the greeklish version of leet mode


leet_dict = Setup.leet_dict()


special_characters = Setup.SpecChars()


olympiakos = Setup.Team('OLY')
panathinaikos = Setup.Team('PAO')
aek = Setup.Team('AEK')
paok = Setup.Team('PAOK')
ael = Setup.Team('AEL')
aris = Setup.Team('ARIS')


########################### THE FUNCTIONS ##############################



def names():        # populates the nameslist
	global surname
	global firstname

	while True:
		x = raw_input("\n[+] owner's surname - press ENTER if you don't know it > ")
		if x == "":
			pass
		else:
			surname = x
			nameslist.append(surname)

		y = raw_input("\n[+] owner's firstname - press ENTER if you don't know it' > ")
		if y == "":
			break
		else:
			firstname = y
			nameslist.append(firstname)
			nameslist.append(surname + firstname)
			if surname + firstname != firstname + surname:
				nameslist.append(firstname + surname)
		break

	print "\n[+] names of partner, child, possible nicknames, relatives, pets or best friends - press ENTER to move on > "
	while True:
		name = raw_input("[+] enter a name (or press ENTER) >  ")
		if name == "":
			break
		else:
			nameslist.append(name)


def births():    # create a list with variations on dates of birth
	print "\n[+] If you know any birthdates (target's, his/her partner's or kid's) enter them bellow:"
	while True:
		global birthdates
		x = raw_input("[+] enter a relevant birthdate in DDMMYYYY format (or press ENTER to move on)>  ")
		if x == '':
			break
		elif len(x) == 8:
			birthdates += (x, x[2:], x[:4], x[:2]+'_'+x[2:4]+'_'+x[4:], x[:2]+'_'+x[2:4]+'_'+x[6:], x[:4]+x[6:], x[:2]+'_'+x[2:4], x[2:4]+'_'+x[4:], x[2:4]+'_'+x[6:])
		else:
			print "DDMMYYYY requires 8 characters!"


def telephone():
	print "\n[+] type his telephone numbers if you know them"
	while True:
		tel = raw_input("[+] telephone (or press ENTER to move on) >  ")
		if tel == "":
			break
		else:
			telephones.append(tel)


def interests():
	print "\n[+] additional keywords - (place of birth, favorite band, director or any other keyword you think might be useful)"
	while True:
		interest = raw_input("[+] enter an interest (or ENTER) >  ")
		if interest == "":
			break
		else:
			interestslist.append(interest)


def combine2 (a, b, new_l):    # Combine the string items of two lists to a new list & add it to the final list
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
	[+] press ENTER if you don't know or if you don't want to use this
	'''

	while True:
		x = raw_input("[+] pick the corresponding number (or ENTER) >  ")
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
		elif x == '':
			break
		elif x == 'help':
			print info
		else:
			print "\nError: That wasn't in the list of options\nType one of the numbers or press ENTER to move on\n"


def loadf(lst):      # append a list's items to the final list
	for i in lst:
		if minchar <= len(str(i)) and maxchar >= len(str(i)):
			final_list.append(str(i))



def add_nums(l):   # add some numbers to the back a list's elements
	tmp = []
	new_l = []
	for i in range(0, 100):
		tmp.append(str(i))
		tmp.append('_'+str(i))
	for i in range(0, 10):
		tmp.append('0'+str(i))
	combine2(l, tmp, new_l)
	l = new_l


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

# The Preparation:

# first we add the reverse versions of the years, sequences and popular passwords in their lists

RestFunctions.rev(years)
AuxFunctions.add_(years)
RestFunctions.rev(sequences)
AuxFunctions.add_(sequences)
RestFunctions.rev(pop_pswd)
AuxFunctions.add_(pop_pswd)

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



final_list=[]


# The actual main program

# print intro

loadf(sequences)  # append the final list with common passwords, numbers and sequences
loadf(pop_pswd)
loadf(common_nums)

names()                 # start asking info
nameslist = nameslist + Nicks.list_nicks(nameslist) # let's find some nicknames
AuxFunctions.capitalize(nameslist)
nameslist = dic_rep(nameslist, leet_dict)
RestFunctions.rev(nameslist)          # reverse those names
loadf(nameslist)        # add them to the final list

births()                # ask for some more info
RestFunctions.rev(birthdates)
AuxFunctions.add_(birthdates)
loadf(birthdates)

telephone()
RestFunctions.rev(telephones)
AuxFunctions.add_(telephones)
loadf(telephones)

team_combine()      # bring football to the mix

add_nums(nameslist)

interests()             # what other interests we can mix
AuxFunctions.add_(interestslist)
loadf(interestslist)

combine2(nameslist, birthdates, namesbirthdates)    # combine as many lists as possible
combine2(nameslist, years, namesyears)
combine2(nameslist, sequences, namessequences)
combine2(nameslist, telephones, namestelephones)
combine2(nameslist, interestslist, namesinterests)
combine2(interestslist, years, interestsyears)

spec_chars()

paswd_list = "\n".join(final_list)	# Getting the list together
RestFunctions.write_out(paswd_list, final_list)
