# This file contains some lists etc that will be used as constants by Dump.
# You can easily change them to fit your specific needs.


# minimum and maximum number of characters the final passwords may have
minchar = 8
maxchar = 18

# This range of years will be combined with names etc in the passwords
years = list(range(1950, 2021))

# Same goes for those number sequences
sequences = [
                0,00,000,0000,00000,000000,0000000,00000000,000000000,
                123,1234,12345,123456,123123,1234567, 12345678,123456789,123456789,
                135,1357,13579,1357911,135791113, # Odd numbers
                246,2468,246810,24681012,2468101214, # Even numbers
                235,2357,235711,23571113,2357111317, # Prime numbers
                112,1123,11235,112358,11235813,1123581321 # Fibonachi sequence
            ]

# This dictionary will replace the vowels and diphthongs on the left with the ones on the right
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
# Special characters to be added in the passwords
SpecChars = ['!', '.', '@', '#', '$', '%', '*']

# Specific keywords to be used with the favourite-team option
team_dic = {
        1: ['thrillos', 'gayros', 'olympiakos', 'olympiakara', 'thira', 'gate', 'thrilara', 'thira7', 'gate7', '7', 'oeo', 'ole'],
        2: ['panatha', 'panathinaikos', 'thira', 'gate', 'trifili', 'trifilara', 'vazelos', 'vazela', 'thira13', 'gate13', '13', 'oeo', 'ole'],
        3: ['original', 'aek', 'original', 'aek', 'aekara', 'thira', 'aekara', 'hanoumi', 'hanoumaki', 'thira21', 'gate21', '21', 'oeo', 'ole'],
        4: ['paok', 'toumpa', 'paoki', 'mpaok', 'paokara', 'mpaokara', 'voulgaros', 'salonika', 'thessaloniki', 'gate', 'thira', 'thira4', 'gate4', '4', 'oeo', 'ole'],
        5: ['alogaki', 'visini', 'larisa', 'larsa', 'trakter', 'ael', 'aelara', 'alogaki', 'oeo', 'ole'],
        6: ['skouliki', 'salonika', 'xarilaou', 'aris', 'arianos', 'oeo', 'ole' ]
    }

# Very common passwords & password elements
pop_pswd = [
                'dragon','iloveyou','love','princess','master','monkey',
                'qwerty','abcdef','asdf','qazwsx','1qaz2wsx','abc123','qwer',
                'zxcasd','asdzxc','qweasdzxc','password','login','admin','root'
            ]

######## PLACEHOLDERS for upcomming features ########


# def swearing():
#     lista vrisiwn

# def komma():
#     analogo me thn omada

# def fav_chars
#     lista agaphmenwn xarakthrwn analoga me tainies/seires pou vlepei
