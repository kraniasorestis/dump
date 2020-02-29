#!/bin/python

from src import Questions, Setup, Auxiliary, Numbers
import os

intro = '''
  ----------------------          LICENSE         ------------------------
 |                                                                        |
 |  This program is free software: you can redistribute it and/or modify  |
 |  it under the terms of the GNU General Public License as published by  |
 |  the Free Software Foundation, either version 3 of the License, or     |
 |  (at your option) any later version.                                   |
 |                                                                        |
 |  This program is distributed in the hope that it will be useful,       |
 |  but WITHOUT ANY WARRANTY; without even the implied warranty of        |
 |  MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the         |
 |  GNU General Public License for more details.                          |
 |                                                                        |
 |  see <http://www.gnu.org/licenses/>                                    |
 |                                                                        |
 |  * Author: Orestis Kranias                                             |
 |  * kraniasorestis@protonmail.com                                       |
 |  * www.github.com/kraniasorestis                                       |
 |  * Copyright (C) 2016                                                  |
 |  * Contributor: Panagiwtis Simakis - https://github.com/sp1thas        |
 |                                                                        |
  -----------------------------------------------------------------------


   -------------------           DISCLAIMER            ------------------
  |                                                                      | 
  |  Ayto to programma exei graftei gia pen-testing. An xrhsimopoihthei  |
  |  gia paranomes epitheseis thn eythynh thn ferei o xrhsths.           |
  |                                                                      |
   ----------------------------------------------------------------------                   


  -----------------            ODHGIES XRHSHS              ----------------
 |                                                                         |
 | Gia na doulepsei kala, xrhsimopoihste thn orthografia twn greeklish.    |
 |                                                                         |
 | gia paradeigma -> to hta me 'h' (anti gia 'i'), to wmega to grafoume    |
 | me 'w' anti gia 'o', tous difthogkous toys grafoume kanonika, dld: mp   |
 | (oxi "b"), nt (oxi "d") ktl                                             |
 |                                                                         |
 | To prwto gramma twn onomatwn prepei na einai mikro anti gia kefalaio:   |
 |                                                                         |
 | Me liga logia -> oresths (to swsto), anti gia Orestis (to lathos)       |
 |                                                                         |
 | Ta onomata poy exoyn "epishmh" ekdoxh na ta grafete me thn kathhmerinh  |
 | ekdoxh. (px Dhmhtrhs anti gia Dhmhtrios). To DUMP tha symplhrwsei thn   |
 | epishmh ekdoxh apo mono toy. (Rikste mia matia sto /src/Setup.py gia    |
 | perissotera. Mporeite epishs na symplhrwsete onomata poy leipoyn,       |
 | nicknames ktl)                                                          |
 |                                                                         |
 | An thelete na rythmisete posous xarakthres 8a exoun oi telikoi kwdikoi, |
 | To default einai apo 6 ews 16.                                          |
  -------------------------------------------------------------------------


       #############################################################


            MMMMMMMM     MMMM    MMMM  MMMMN    NMMMM  MMMMMMMN
            MMMMMMMMMN   MMMM    MMMM  MMMMMM  MMMMMM  MMMMMMMMN
            MMM   NMMMM  MMMM    MMMM  MMMMMMMMMMMMMM  MM(   )MMN
            MMM    MMMM  MMMM    MMMM  MMMM  NN  MMMM  MMMMMMMMM
            MMM   NMMMM  MMMMN  NMMMM  MMMM      MMMM  MMMMMMM
            MMMMMMMMND    MMMMMMMMMM   MMMM      MMMM  MMMM
            MMMMMMMM       NMMMMMMN    MMMM      MMMM  MMMM

                                  -  2.0  -
        ######## a DUMP of UNREASONABLY MEDIOCRE PASSWORDS #########


      [!]  Don't forget to check the Setup.py file to configure   [!]
      [!]       Dump's parameter's to your specific needs         [!]

'''''



print intro

# firstly, we put some dates/years (both normal form and reversed), usual sequences, common passwords etc in our list

final_list = Auxiliary.chop(Setup.years)                      
rev_years = Auxiliary.rev(Setup.years)                        
final_list += Auxiliary.chop(rev_years)                       
sp_char_years = Auxiliary.add_(Setup.years)                   


########################## Collecting Personal Info #############################

final_list += Questions.pop_pass() 

nameslist = Auxiliary.chop(Questions.names())                  
birthdates = Questions.births()                                
telephones = Questions.telephone()                             

final_list += Auxiliary.soccer(nameslist, birthdates)          
interests = Questions.interests()
vulgar = Questions.vulgar()


########################### Working with the Info ###############################

rev_names = Auxiliary.rev(nameslist)
nameslist += Auxiliary.chop(Auxiliary.check_nicks(nameslist))
nameslist += rev_names                                         
nameslist += Auxiliary.capitalize(nameslist)                   
rev_dates = Auxiliary.rev(birthdates)                          
rev_tel = Auxiliary.rev(telephones)                            
final_list += Auxiliary.chop(telephones)                       
final_list += Auxiliary.chop(rev_tel)                          
final_list += Auxiliary.chop(Auxiliary.spec_chars(telephones)) 
final_list += Auxiliary.chop(interests)

final_list += Auxiliary.chop(nameslist)                        
final_list += Auxiliary.chop(birthdates)                       
final_list += Auxiliary.chop(rev_dates)
final_list += vulgar                                  # ask for vulgar passwords                     

final_list += Auxiliary.chop(Questions.nums(nameslist))        

final_list += Auxiliary.combine2way(nameslist, birthdates)
final_list += Auxiliary.combine2way(nameslist, rev_dates)
final_list += Auxiliary.combine2way(nameslist, Setup.years)    
final_list += Auxiliary.combine(nameslist, sp_char_years)      
final_list += Auxiliary.combine2way(nameslist, telephones)     
final_list += Auxiliary.combine(nameslist, interests)
final_list += Auxiliary.combine(interests, Setup.years)
final_list += Auxiliary.combine(interests, rev_years)
final_list += Auxiliary.combine(interests, sp_char_years)

##################### dealing with additional wordlists #########################

def additional_wordlists():
    tmp = []
    print "\n[+] Do you want to use additional wordlists? (y/n)> "
    while True:
        reply = raw_input("\n(y/n) > ")
        if reply == 'y':
            tmp += load_words()
            break
        elif reply == 'n':
            break
        else:
            print "\n[!] please type y/n or press ENTER"
    return tmp

def load_words():
    os.system('cd additional_wordlists && cat * > additional_dictionary.txt')
        
    script_dir = os.path.dirname(os.path.abspath(__file__))   # <- absolute directory the script is in
    rel_path = "additional_wordlists/additional_dictionary.txt"
    abs_file_path = script_dir + '/' + rel_path

    f = open(abs_file_path, 'r')
    additional = f.read().splitlines()
    additional = Auxiliary.wikipedia_unlink(additional)
    additional = [i.lower() for i in additional]
    additional += Auxiliary.capitalize(additional)
    tmp = []
    tmp += Auxiliary.combine(additional, Setup.years)
    tmp += Auxiliary.combine(additional, sp_char_years)
    tmp += Auxiliary.combine(additional, birthdates)
    tmp += Auxiliary.combine(additional, rev_dates)
    os.system('rm additional_wordlists/additional_dictionary.txt')
    return additional + tmp

final_list += Auxiliary.chop(additional_wordlists())

############################### Closing up ######################################

final_list += Questions.leet(final_list)
final_list = list(set(final_list))
#print final_list
paswd_list = "\n".join(final_list)
Auxiliary.write_out(paswd_list, final_list)


