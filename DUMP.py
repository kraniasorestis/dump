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


######## a DUMP of UNREASONABLY MEDIOCRE PASSWORDS #########


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



[!]  Don't forget to check the Setup.py file to configure   [!]
[!]      Dump's parameter's to your specific needs          [!]


'''''



# first we reverse the years & sequences and reappend them in their lists

Auxiliary.rev(Setup.years)
Auxiliary.add_(Setup.years)
Auxiliary.rev(Setup.sequences)
Auxiliary.add_(Setup.sequences)

print intro

final_list = Auxiliary.chop(Setup.sequences)  # append the final list with common passwords, numbers and sequences
final_list += Auxiliary.chop(Setup.pop_pswd)
cmn_pswd = Auxiliary.one_char_psw()
final_list += Auxiliary.chop(cmn_pswd)

######################### Collecting Personal Info #############################

nameslist = Questions.names()
nameslist += Questions.nicknames(nameslist)
Auxiliary.capitalize(nameslist)
nameslist = Auxiliary.leet_rep(nameslist, Setup.leet_dict)
Auxiliary.rev(nameslist)
final_list += Auxiliary.chop(nameslist)

birthdates = Questions.births()
Auxiliary.rev(birthdates)
final_list += Auxiliary.chop(birthdates)
Auxiliary.add_(birthdates)

telephones = Questions.telephone()
Auxiliary.rev(telephones)
final_list += Auxiliary.chop(telephones)
Auxiliary.add_(telephones)

final_list += Auxiliary.soccer(nameslist, birthdates)

########################## Working with the Info ###############################

namelist = Numbers.add_nums(nameslist)
final_list += nameslist

interestslist = Questions.interests()
Auxiliary.add_(interestslist)
final_list += Auxiliary.chop(interestslist)

final_list += Auxiliary.combine2(nameslist, birthdates)
final_list += Auxiliary.combine2(nameslist, Setup.years)
final_list += Auxiliary.combine2(nameslist, Setup.sequences)
final_list += Auxiliary.combine2(nameslist, telephones)
final_list += Auxiliary.combine2(nameslist, interestslist)
final_list += Auxiliary.combine2(interestslist, Setup.years)

final_list += Auxiliary.spec_chars(nameslist)
final_list += Auxiliary.bi_spec_chars(nameslist)
final_list = list(set(final_list))

paswd_list = "\n".join(final_list)
Auxiliary.write_out(paswd_list, final_list)
