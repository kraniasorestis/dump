#!/bin/python

from src import Questions, Setup, AuxFunctions, AuxFunctions, NumberFunctions

intro = '''

#############################################################


    MMMMMMMM     MMMM    MMMM  MMMMN    NMMMM  MMMMMMMN
    MMMMMMMMMN   MMMM    MMMM  MMMMMM  MMMMMM  MMMMMMMMN
    MMM   NMMMM  MMMM    MMMM  MMMMMMMMMMMMMM  MM(   )MMN
    MMM    MMMM  MMMM    MMMM  MMMM  NN  MMMM  MMMMMMMMM
    MMM   NMMMM  MMMMN  NMMMM  MMMM      MMMM  MMMMMMM
    MMMMMMMMND    MMMMMMMMMM   MMMM      MMMM  MMMM
    MMMMMMMM       MMMMMMMM    MMMM      MMMM  MMMM


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


    MMMMMMMM     MMMM    MMMM  MMMMN    NMMMM  MMMMMMMN
    MMMMMMMMMN   MMMM    MMMM  MMMMMM  MMMMMM  MMMMMMMMN
    MMM   NMMMM  MMMM    MMMM  MMMMMMMMMMMMMM  MM(   )MMN
    MMM    MMMM  MMMM    MMMM  MMMM  NN  MMMM  MMMMMMMMM
    MMM   NMMMM  MMMMN  NMMMM  MMMM      MMMM  MMMMMMM
    MMMMMMMMND    MMMMMMMMMM   MMMM      MMMM  MMMM
    MMMMMMMM       MMMMMMMM    MMMM      MMMM  MMMM


######## a DUMP of UNBELIEVABLY MEDIOCRE PASSWORDS #########


'''''

def soccer_mix(omada):
    list1 = AuxFunctions.combine2(nameslist, omada)
    list2 = AuxFunctions.combine2(list1, omada)
    list3 = AuxFunctions.combine2(list1, Setup.years)
    list4 = AuxFunctions.combine2(list2, Setup.years)
    list5 = AuxFunctions.combine2(omada, Setup.years)
    list6 = AuxFunctions.combine2(omada, birthdates)
    return omada + list1 + list2 + list3 + list4 + list5 + list6

def soccer():
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
        tmp = []
        if x == '':
            break
        elif int(x) >= 1 and int(x) <= 6:
            tmp = soccer_mix(Setup.team_dic[int(x)])
            break
        else:
            print "\nError: That wasn't in the list of options\nType one of the numbers or press ENTER to move on\n"
    return tmp



# first we reverse the years, sequences and popular passwords and reappend them in their lists

AuxFunctions.rev(Setup.years)
AuxFunctions.add_(Setup.years)
AuxFunctions.rev(Setup.sequences)
AuxFunctions.add_(Setup.sequences)
AuxFunctions.rev(Setup.pop_pswd)
AuxFunctions.add_(Setup.pop_pswd)

print intro

final_list = AuxFunctions.load(Setup.sequences)  # append the final list with common passwords, numbers and sequences
final_list += AuxFunctions.load(Setup.pop_pswd)
cmn_pswd = NumberFunctions.common_nums()
final_list += AuxFunctions.load(cmn_pswd)

######################### Asking Personal Info #############################

nameslist = Questions.names()
nameslist += Questions.list_nicks(nameslist)   # let's find some nicknames
AuxFunctions.capitalize(nameslist)
nameslist = AuxFunctions.dic_rep(nameslist, Setup.leet_dict)
AuxFunctions.rev(nameslist)                       # reverse those names
final_list += AuxFunctions.load(nameslist)

birthdates = Questions.births()
AuxFunctions.rev(birthdates)
AuxFunctions.add_(birthdates)
final_list += AuxFunctions.load(birthdates)

telephones = Questions.telephone()
AuxFunctions.rev(telephones)
AuxFunctions.add_(telephones)
final_list += AuxFunctions.load(telephones)

final_list += soccer()                           # bring soccer to the mix

########################## Working with the Info ###############################

namelist = NumberFunctions.add_nums(nameslist)
final_list += nameslist

interestslist = Questions.interests()             # see what other interests we can mix
AuxFunctions.add_(interestslist)
final_list += AuxFunctions.load(interestslist)

final_list += AuxFunctions.combine2(nameslist, birthdates)    # combine as many lists as possible
final_list += AuxFunctions.combine2(nameslist, Setup.years)
final_list += AuxFunctions.combine2(nameslist, Setup.sequences)
final_list += AuxFunctions.combine2(nameslist, telephones)
final_list += AuxFunctions.combine2(nameslist, interestslist)
final_list += AuxFunctions.combine2(interestslist, Setup.years)

final_list += AuxFunctions.spec_chars(nameslist)
final_list += AuxFunctions.bi_spec_chars(nameslist)

paswd_list = "\n".join(final_list)    # Getting the list together
AuxFunctions.write_out(paswd_list, final_list)
