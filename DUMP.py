#!/bin/python

from src import AskFunctions, Setup, AuxFunctions, AuxFunctions, NumberFunctions

intro = '''

#############################################################


    ########     ####    ####  #####    #####  ########
    ##########   ####    ####  ######  ######  #########
    ###   #####  ####    ####  ##############  ###   ###
    ###    ####  ####    ####  #### #### ####  #########
    ###    ####  ####    ####  ####  ##  ####  ########
    ###   #####  #####  ####   ####      ####  ####
    ##########    #########    ####      ####  ####
    ########       #######     ####      ####  ####


######## a DUMP of UNBELIEVABLY MEDIOCRE PASSWORDS #########


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
* Contributor: Panagiwtis Simakis - https://github.com/sp1thas


For the Greek users:
An thelete na doulepsei swsta to programma na grafete orthografhmena!
(opws edw). Gia paradeigma ta kuria onomata me hta sto telos.
LATHOS: Orestis. --> SWSTO: Oresths. To wmega to grafoume me "w",
tous difthogkous kanonika, dld: mp - oxi b, nt - oxi d, gk - oxi g.
Ta dipla fwnhenta kanonika. ei, oi, ai, kai oxi 'i' kai 'e'.
ALLIWS DEN THA VGOYN OLOI OI DYNATOI SYNDYASMOI KWDIKWN!

Ean thelete na rythmisete posous xarakthres 8a exoun oi telikoi kwdikoi,
aytes oi rythmiseis vriskontai sto /src/Setup.py
To default einai apo 8 ews 18 (optimized gia wifi attacks).

DISCLAIMER: If you do anything illegal with this program, you could
end up in JAIL! I have no responsibility over how this will be used!
It's developed for penetration testers and security researchers!!
Not for wardriving!!


#############################################################


    ########     ####    ####  #####    #####  ########
    ##########   ####    ####  ######  ######  #########
    ###   #####  ####    ####  ##############  ###   ###
    ###    ####  ####    ####  #### #### ####  #########
    ###    ####  ####    ####  ####  ##  ####  ########
    ###   #####  #####  ####   ####      ####  ####
    ##########    #########    ####      ####  ####
    ########       #######     ####      ####  ####


######## a DUMP of UNBELIEVABLY MEDIOCRE PASSWORDS #########


'''''


######################## GLOBAL CONSTANTS WE'LL NEED ##############################


# these are lists of years and common sequences used in passwords - they will be used in reverse too
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


def combine2 (a, b, new_l):    # Combine the string items of two lists to a new list & add it to the final list
    n = 0
    while n < len(a):
        for i in b:
            if Setup.minchar <= len(str(a[n])+str(i)) and Setup.maxchar >= len(str(a[n])+str(i)):
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
			combine2(namesteams_final, Setup.years, namesteams_dates)
			break
		elif x == '2':
			loadf(panathinaikos)
			combine2(nameslist, panathinaikos, namesteams)
			combine2(namesteams, ['thira13', 'gate13', '13', 'oeo', 'ole'], namesteams_final)
			combine2(namesteams_final, Setup.years, namesteams_dates)
			break
		elif x == '3':
			loadf(aek)
			combine2(nameslist, aek, namesteams)
			combine2(namesteams, ['thira21', 'gate21', '21', 'oeo', 'ole'], namesteams_final)
			combine2(namesteams_final, Setup.years, namesteams_dates)
			break
		elif x == '4':
			loadf(paok)
			combine2(nameslist, paok, namesteams)
			combine2(namesteams, ['thira4', 'gate4', '4', 'oeo', 'ole'], namesteams_final)
			combine2(namesteams_final, Setup.years, namesteams_dates)
			break
		elif x == '5':
			loadf(ael)
			combine2(nameslist, ael, namesteams)
			combine2(namesteams, ['alogaki', 'oeo', 'ole'], namesteams_final)
			combine2(namesteams_final, Setup.years, namesteams_dates)
			break
		elif x == '6':
			loadf(aris)
			combine2(nameslist, aris, namesteams)
			combine2(namesteams, Setup.years, namesteams_dates)
			break
		elif x == '':
			break
		else:
			print "\nError: That wasn't in the list of options\nType one of the numbers or press ENTER to move on\n"


def loadf(lst):      # append a list's items to the final list
	for i in lst:
		if Setup.minchar <= len(str(i)) and Setup.maxchar >= len(str(i)):
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



########################### MAIN PROGRAM ###############################

# The Preparation:

# first we reverse the years, sequences and popular passwords and reappend them in their lists

AuxFunctions.rev(Setup.years)
AuxFunctions.add_(Setup.years)
AuxFunctions.rev(sequences)
AuxFunctions.add_(sequences)
AuxFunctions.rev(pop_pswd)
AuxFunctions.add_(pop_pswd)

# Predefining some lists to be populated later

teamslist = []

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

print intro

loadf(sequences)  # append the final list with common passwords, numbers and sequences
loadf(pop_pswd)
loadf(common_nums)

nameslist = AskFunctions.names()                 # start asking info
nameslist += AskFunctions.list_nicks(nameslist) # let's find some nicknames
AuxFunctions.capitalize(nameslist)
nameslist = AuxFunctions.dic_rep(nameslist, leet_dict)
AuxFunctions.rev(nameslist)          # reverse those names
loadf(nameslist)        # add them to the final list

birthdates = AskFunctions.births()                # ask for some more info
AuxFunctions.rev(birthdates)
AuxFunctions.add_(birthdates)
loadf(birthdates)

telephones = AskFunctions.telephone()
AuxFunctions.rev(telephones)
AuxFunctions.add_(telephones)
loadf(telephones)

team_combine()      # bring football to the mix

add_nums(nameslist)

interestslist = AskFunctions.interests()             # what other interests we can mix
AuxFunctions.add_(interestslist)
loadf(interestslist)

combine2(nameslist, birthdates, namesbirthdates)    # combine as many lists as possible
combine2(nameslist, Setup.years, namesyears)
combine2(nameslist, sequences, namessequences)
combine2(nameslist, telephones, namestelephones)
combine2(nameslist, interestslist, namesinterests)
combine2(interestslist, Setup.years, interestsyears)

spec_chars()

paswd_list = "\n".join(final_list)	# Getting the list together
AuxFunctions.write_out(paswd_list, final_list)
