# This file contains some lists etc that will be used as constants by Dump.
# You can easily change them to fit your specific needs.


# minimum and maximum number of characters the final passwords may have
minchar = 6
maxchar = 16

# This range of years will be combined with names etc in the passwords
years = list(range(1980, 2021))

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

# Common passwords derived from the "worst 500 passwords" wordlist hosted in SkullSecurity. I deleted a lot that were just English-only names
# and I tried to produce the greek counterparts of a lot that could be being used in Greece
pop_pswd = [
            'dragon','iloveyou','love','princess','master','monkey', '121212','podosfairo','abgrtyu','dreams',
            'qwerty','abcdef','asdf','qazwsx','1qaz2wsx','abc123','qwer','zxcasd','asdzxc','qweasdzxc','password',
            'login','admin','root','paremoumiapipa','arxidi','arxidia','malakas','mpastardos','kargiolhs','kargiolis',
            'pussy','dragon','696969','mustang','kwdikos','kodikos','letmein','baseball',
            'master','football','shadow','monkey','abc123','pass','fuckme','6969','jordan','harley','mousikh','tester',
            'ranger','iwantu','fuck','test','batman','tigger','access','love','buster','olympiakos',
            'olimpiakos','gayros','panathinaikos','aek','ael','aris','paok','mpasket','basket','hockey','killer','george',
            'sexy','superman','spiderman','wolverine','cyclops','asshole','fuckyou','summer','hammer','enter','nicole',
            'cowboy','fucker','corvette','freedom','blowjob','yellow','kitrino','camaro','secret','dick','poutsos','poutsa',
            '131313','123123','bitch','hello','please','porsche','guitar','chelsea','black','diamond','nascar',
            'computer','wizard','magos','money','lefta','fragka','iceman','tigers','purple','andrea','horny',
            'dakota','player','paixths','paixtaras','paixtoura','starwars','boomer','cowboys','charles','girls','gkomenakia','gkomenes',
            'coffee','kafes','bulldog','john','mpyra','johnny','johnaras','gandalf','winter','brandy','tennis','mike','pipa',
            'pipes','ferrari','ferari','maverick','diablo','sexsex','hardcore','counterstrike','counter','chris','yamaha','driver',
            'angels','maddog','butthead','fucking','captain','bigdick','xavier','viking','snoopy','blue','mple','eagles',
            'winner','house','flower','united','zxcvbn','golf','bond007','tiger','doctor','angel','junior','porno','athens',
            'thessalonikh','thessaloniki','salonica','patra','larisa','larissa','trikala','karditsa','volos',
            'hrakleio','xania','krhth','rethymno','thiva','lamia','leivadia','livadia','kozani','kozanh','grevena','ptolemaida','drama','serres',
            'seres','kavala','alexandroupolh','rodos','xalkida','evoia','katerinh','katerini','sparth','tripolh','badboy','gamwthnpanagia',
            'spider','1212','porn','matrix','teens','scooby','jason','cumshot','lover','princess','mercedes','doggie','zzzzzz',
            'horney','2112','fred','xxxxx','tits','member','boobs','bigdaddy','penis','voyager','white','topgun','bigtits','bitches','green','prasino',
            'portokali','mwv','mob','super','qazwsx','magic','slayer','asdf','video','kwlos','kwlarakia','kwlaraki','skata','marlboro',
            'internet','action','monster','jeremy','bill','crystal','peter','pussies','cock','beer','rocket','prince','beach','amateur',
            'star','testing','murphy','mother','forever','angela','viper','lovers','suckit','gregory','nikolas','nikos','paylos',
            'kwstas','giwrgos','apostolis','giannhs','grhgorhs','grigoris','dhmhtrhs','dimitris','mhtros','mitsos','buddy','filos','kollhtos',
            'kolitos','kolhth','kolith','whatever','young','nicholas','lucky','helpme','midnight','baby','cunt','startrek','232323','bigcock',
            'happy','sophie','ladies','naughty','giants','booty','blonde','fucked','golden','fire','sagapw','sagapo','agaph',
            'fwtia','einstein','warrior','mouni','kayli','kayla','xynw','xysia','xysi','slut','xanthia','xan8ia','nipples','power','victoria','roges',
            'roga','vizia','vyzia','vizi','vyzi','vagina','toyota','hotdog','gamhsi','gamhsou','gamiese','gamiesai','gamias',
            'gamaw','segamaw','gamhseme','gamame','rock','extreme','erotic','erwtas','dirty','ford','arsenal','wolf','nipple','alex',
            'dota','legend','movie','success','jaguar','great','cool','japan','naked','squirt','thalassa','apple','alexis','swimming',
            'dolphin','kolypmi','casper','stupid','shit','saturn','gemini','apples','august','cumming','kitty','rainbow','112233','cream','shaved',
            'mine','delfini','king','racing','aetos','eagle','hentai','little','kokkino','cocacola','animal','private','blondes','melaxrines',
            'enjoy','girl','apollo','qwert','time','metal','women','gynaikes','voodoo','magnum','juice','oneira','music','mistress','phantom',
            ]

######## PLACEHOLDERS for upcomming features ########


# def swearing():
#     lista vrisiwn

# def komma():
#     analogo me thn omada

# def fav_chars
#     lista agaphmenwn xarakthrwn analoga me tainies/seires pou vlepei
