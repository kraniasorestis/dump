#!/bin/python

from src import Questions, Setup, Auxiliary, Numbers

intro = '''

#############################################################


    MMMMMMMM     MMMM    MMMM  MMMMN    NMMMM  MMMMMMMN
    MMMMMMMMMN   MMMM    MMMM  MMMMMM  MMMMMM  MMMMMMMMN
    MMM   NMMMM  MMMM    MMMM  MMMMMMMMMMMMMM  MM(   )MMN
    MMM    MMMM  MMMM    MMMM  MMMM  NN  MMMM  MMMMMMMMM
    MMM   NMMMM  MMMMN  NMMMM  MMMM      MMMM  MMMMMMM
    MMMMMMMMND    MMMMMMMMMM   MMMM      MMMM  MMMM
    MMMMMMMM       NMMMMMMN    MMMM      MMMM  MMMM


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
Parola auta, den peirazei an to prwto gramma einai mikro anti gia kefalaio:
LATHOS: orestis. --> SWSTO: oresths. To wmega to grafoume me "w",
tous difthogkous kanonika, dld: mp - kai oxi b, nt - oxi d, gk - oxi g.
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
    MMMMMMMM       NMMMMMMN    MMMM      MMMM  MMMM


######## a DUMP of UNBELIEVABLY MEDIOCRE PASSWORDS #########


'''''

def soccer_mix(omada):
    list1 = Auxiliary.combine2(nameslist, omada)
    list2 = Auxiliary.combine2(list1, omada)
    list3 = Auxiliary.combine2(list1, Setup.years)
    list4 = Auxiliary.combine2(list2, Setup.years)
    list5 = Auxiliary.combine2(omada, Setup.years)
    list6 = Auxiliary.combine2(omada, birthdates)
    return omada + list1 + list2 + list3 + list4 + list5 + list6

def soccer():
    print '''\n\nwhat's his favourite team?

    [!][!][!][!][!][!][!][!][!][!][!][!][!][!][!][!][!][!][!][!][!][!][!][!][!]
    [!][!][!][!][!][!][!][!]        WARNING      [!][!][!][!][!][!][!][!][!][!]
    [!][!][!][!][!]  This will make your wordlist so huge [!][!][!][!][!][!][!]
    [!][!][!][!][!]       that python may even crash      [!][!][!][!][!][!][!]
    [!][!][!][!]  in case of a crash, retry with fewer names [!][!][!][!][!][!]
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
            print '\n[!] Wait a couple of mins and pray that your RAM can handle this [!]\n'
            tmp = soccer_mix(Setup.team_dic[int(x)])
            break
        else:
            print "\nError: That wasn't in the list of options\nType one of the numbers or press ENTER to move on\n"
    return tmp



# first we reverse the years, sequences and popular passwords and reappend them in their lists

Auxiliary.rev(Setup.years)
Auxiliary.add_(Setup.years)
Auxiliary.rev(Setup.sequences)
Auxiliary.add_(Setup.sequences)
Auxiliary.rev(Setup.pop_pswd)
Auxiliary.add_(Setup.pop_pswd)

print intro

final_list = Auxiliary.chop(Setup.sequences)  # append the final list with common passwords, numbers and sequences
final_list += Auxiliary.chop(Setup.pop_pswd)
cmn_pswd = Auxiliary.one_char_psw()
final_list += Auxiliary.chop(cmn_pswd)

######################### Asking Personal Info #############################

nameslist = Questions.names()
nameslist += Questions.nicknames(nameslist)
Auxiliary.capitalize(nameslist)
nameslist = Auxiliary.leet_rep(nameslist, Setup.leet_dict)
Auxiliary.rev(nameslist)
final_list += Auxiliary.chop(nameslist)

birthdates = Questions.births()
Auxiliary.rev(birthdates)
Auxiliary.add_(birthdates)
final_list += Auxiliary.chop(birthdates)

telephones = Questions.telephone()
Auxiliary.rev(telephones)
Auxiliary.add_(telephones)
final_list += Auxiliary.chop(telephones)

final_list += soccer()

########################## Working with the Info ###############################

namelist = Numbers.add_nums(nameslist)
final_list += nameslist

interestslist = Questions.interests()             # see what other interests we can mix
Auxiliary.add_(interestslist)
final_list += Auxiliary.chop(interestslist)

final_list += Auxiliary.combine2(nameslist, birthdates)    # combine as many lists as possible
final_list += Auxiliary.combine2(nameslist, Setup.years)
final_list += Auxiliary.combine2(nameslist, Setup.sequences)
final_list += Auxiliary.combine2(nameslist, telephones)
final_list += Auxiliary.combine2(nameslist, interestslist)
final_list += Auxiliary.combine2(interestslist, Setup.years)

final_list += Auxiliary.spec_chars(nameslist)
final_list += Auxiliary.bi_spec_chars(nameslist)
final_list = list(set(final_list))

paswd_list = "\n".join(final_list)    # Getting the list together
Auxiliary.write_out(paswd_list, final_list)
