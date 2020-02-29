# This file contains some lists etc that will be used as constants by Dump.
# You can easily change them to fit your specific needs.


# minimum and maximum number of characters the final passwords may have
minchar = 6
maxchar = 16

# This range of years will be combined with names etc in the passwords
years = list(range(1980, 2021))

# Same goes for those number sequences and other numbers
sequences = [
                0,00,000,0000,00000,000000,0000000,00000000,000000000,
                123,1234,12345,123456,123123,1234567, 12345678,123456789,
                135,1357,13579,1357911,135791113, # Odd numbers
                246,2468,246810,24681012,2468101214, # Even numbers
                235,2357,235711,23571113,2357111317, # Prime numbers
                112,1123,11235,112358,11235813,1123581321, # Fibonachi sequence
				131313,123123,121212,6969,696969,112233,233444,2334445555, # Other usual numbers in passwords 
                233444555566666,232323 # Other usual numbers in passwords
            ]

# This dictionary will replace the vowels and diphthongs on the left with the ones on the right
leet_dict = {
            	'a':'@',
                'w':'o',
                'o':'0',
                'e':'3',
                'gk':'g',
                'gg':'g',
                'mp':'b',
                'nt':'d',
                'h':'i',
                'y':'i',
                'u':'i',
                'v':'7',
                'ei':'i',
                'ay':'af',
                'ey':'ef',
                'au':'af',
                'eu':'ef',
                'ou':'oy',
                'ks':'x',
                'th':'8',
                'x':'ch',
                'nn':'n',
                'll':'l',
                'pp':'p',
                'mm':'m',
                'rr':'r',
                'tt':'t'
            }

leet_dict_2 = {
            	'a':'4',
                'w':'0',
                'gk':'gg',
                'gg':'gk',
                'oy':'ou',
                'ay':'av',
                'ey':'ev',
                'au':'av',
                'eu':'ev',
                't':'7',
                'x':'ks',
                'ch':'x'
                 }


# Special characters to be added in the passwords
SpecChars = ['!', '!!', '!!!', '.', '..', '...', '@', '#', '$', '%', '*']


# Specific keywords to be used with the favourite-team option
team_dic = {
        1: ['thrillos', 'gayros', 'olympiakos', 'olympiakara', 'thira', 'gate', 'thira7', 'gate7', '7', 'oeo', 'ole'],
        2: ['panatha', 'panathinaikos', 'thira', 'gate', 'trifili', 'trifilara', 'vazelos', 'vazela', 'thira13', 'gate13', '13', 'oeo', 'ole'],
        3: ['original', 'aek', 'original', 'aekara', 'thira', 'aekara', 'hanoumi', 'hanoumaki', 'thira21', 'gate21', '21', 'oeo', 'ole'],
        4: ['paok', 'toumpa', 'paoki', 'mpaok', 'paokara', 'mpaokara', 'voulgaroi', 'salonika', 'thessaloniki', 'gate', 'thira', 'thira4', 'gate4', '4', 'oeo', 'ole'],
        5: ['alogaki', 'visini', 'larisa', 'larsa', 'trakter', 'ael', 'aelara', 'alogaki', 'oeo', 'ole'],
        6: ['skouliki', 'salonika', 'xarilaou', 'aris', 'arianos', 'oeo', 'ole']
    }

# Common passwords derived from the "worst 500 passwords" wordlist hosted in SkullSecurity.
# I deleted a lot that were just English-only names.

pop_pswd = [
            'dragon','iloveyou','love','princess','master','monkey','podosfairo','abgrtyu','dreams','extreme',
            'qwerty','abcdef','asdf','qazwsx','1qaz2wsx','abc123','qwer','zxcasd','asdzxc','qweasdzxc','password',
            'login','admin','root','mustang','kwdikos','kodikos','letmein','baseball','hockey','dirty','ford',
            'master','football','shadow','monkey','abc123','pass','fuckme','jordan','harley','mousikh','tester',
			'ranger','iwantu','test','batman','tigger','access','love','buster','mpala','mpasket','basket','killer',
            'sexy','superman','spiderman','wolverine','cyclops','summer','hammer','enter','women','voodoo','magnum',
            'cowboy','corvette','freedom','blowjob','yellow','camaro','secret','gamatos','legend','movie','rock',
            'hello','please','porsche','guitar','chelsea','black','diamond','success','jaguar','great','cool','hotdog',
            'computer','wizard','magos','money','lefta','fragka','iceman','tigers','purple','arsenal','wolf',
			'dakota','player','paixths','paixtaras','paixtoura','starwars','boomer','cowboys','charles','girls','coffee',
            'bulldog','john','mpyra','johnny','johnaras','casper','stupid','saturn','juice','oneira','music','phantom',
			'gandalf','winter','brandy','tennis','mike','ferrari','ferari','maverick','sexsex','butterfly','btrfly',
			'hardcore','counterstrike','counter','yamaha','driver','angels','maddog','captain','erotic','erwtas',
			'xavier','viking','snoopy','blue','eagles','winner','house','flower','united','zxcvbn','golf','toyota',
			'bond007','tiger','doctor','angel','junior','athens','thessalonikh','thessaloniki','salonica','patra',
			'larisa','larissa','trikala','karditsa','volos','hrakleio','xania','krhth','rethymno','thiva','lamia','leivadia',
			'livadia','kozani','kozanh','grevena','ptolemaida','drama','serres','seres','kavala','alexandroupolh','rodos',
			'xalkida','evoia','katerinh','katerini','sparth','tripolh','badboy','spider','1212','rainbow','kitty',
			'matrix','teens','scooby','scooobydoo','lover','princess','mercedes','zzzzzz','2112','gemini','apples','august',
			'member','bigdaddy','voyager','white','topgun','enjoy','girl','apollo','blondes','cocacola','animal','private',
			'green','super','qazwsx','magic','slayer','asdf','video','eagle','little','mine','king','racing','naked',
			'marlboro','internet','action','monster','crystal','qwert','time','metal','cream','shaved','thalassa',
			'beer','rocket','prince','beach','amateur','star','testing','murphy','mother','forever','angela','viper',
			'lovers','buddy','kollhtos','kolitos','kolhth','kolith','whatever','young','lucky','helpme','japan',
			'midnight','baby','startrek','happy','sophie','ladies','naughty','giants','booty','apple','swimming','dolphin',
			'blonde','golden','fire','sagapw','sagapo','agaph','einstein','warrior','power','victoria',
			'12three','12tria','123four','123tessera','123tesera','1234five','1234pente','12345six','12345eksi','1233456seven',
            '123456epta','1234567eight','1234567oktw',
            ]

gaming = [
			'playstation','psx','nintendo','nes','snes','gameboy','gameboycolor','sega','segasaturn','saturn','megadrive',
            'mastersystem',
            
            'minecraft','hearthstone','csgo','fortnite','lol','leagueoflegends','wow','warcraft','overwatch','mario','dota2',
			'dota','starcraft','diablo','pokemon','pubg',
   
            'zelda','crashbandicoot','crash','coco','cocobandicoot',

]

vulgar = ['paremoumiapipa','arxidi','arxidia','malakas','mpastardos','kargiolhs','kargiolis','pussy','mounopano',
          'fuck','asshole','fuckyou','fucker','dick','poutsos','poutsa','bitch','kaula','gkaula','gkavla','eatadick',
          'horny','kavla','gkomenakia','gkomenakia','mounia','moynia','moynara','mounara','pipa','pipes','butthead',
          'fucking','porn','brazzers','youporn','pornhub','bdsm','bondage','gamwthnpanagia','horney','cumshot','doggie',
          'bigtits','bitches','kwlaraki','kwlos','kwlarakia','nipple','tits','vyzia','bigcock','suckit','boobs','cunt',
          'mouni','kayli','cumming','gamhsi','gamhsou','gamiese','gamiesai','gamias','gamaw','segamaw','gamhseme',
          'hentai','gamame','xynw','xysia','xysi','slut','squirt','nipples','pussies','cock','penis','skata','fucked',
          'mistress','shit','vizia','vyzia','vizi','vyzi','vagina'

]


nic_dic = {
        'giwrgos':['giwrgaras','giwrgakhs','giwrgaros','tzwrhs','tzwrtzhs','giwrgakos','gewrgios','george'],
        'giannhs':['giannakos','tzonnhs','johnny','john','tzwnaras','iwannhs'],
        'kwstas':['kwnstantinos','kwtsos','kwstaras','gus','kwstakhs','kwstakos','ntinos'],
        'manwlhs':['manwlakhs','manwlakos','manwlios','emmanouhl','manwlos','manwlaras'],
        'vaggelhs':['vaggelakos','vaggelaras','vaggelakhs','evanggelos','vaggos'],
        'dhmhtrhs':['takhs','jimhs','tzimhs','tzimakos','tzimaras','dhmhtrakos','dhmhtrakhs','mhtsos','mhtsaras','mhtsaki','jimmy','jim','jimmhs','dhmhtrios'],
        'nikos':['nikolas','nick','nikolos','nikolakhs','nikolaos'],
        'panagiwths':['panos','panoulhs'],
        'vasilhs':['vasilakhs','vasilaras','vasilakos','bill','billy','mpillhs','vasileios'],
        'xrhstos':['xrhstaras','xrhstakhs','xrhstakos','kitsos','chris'],
        'thanashs':['nasos','sakhs','thanasaras','thanasakos','thanasakhs','athanasios'],
        'mixalhs':['mixalakhs','mixalakos','mixalaras','mixahl'],
        'alexandros':['alexandrakos','alexandroylhs','alekos','aleka','alex'],
        'spyros':['spyro','spyridwn','pipphs','spyrakos','spyrothedragon'],
        'antwnhs':['antwnakhs','antwnaras','antony','antwnios','antwnaros','tony'],
        'leyterhs':['eleytherios','terry','leyterakos','lefterakhs'],
        'stefanos':['stefos','stefanakos','stefanaras','stephan'],
        'anastashs':['anastasios','tasos','tasoulhs','soulhs'],
        'thodwrhs':['theodwros','dwrhs','dwros','thodwros','thodwras','thodwrakos','theodore'],
        'hlias':['liakos','lias'],
        'antreas':['andrew','antrakos','antrikos','adnreas','andrakos','andrikos'],
        'apostolhs':['apostolakos','apostolakhs','apostolaras','apostolaros','tolhs','tolakos','tolaras','apostolos'],
        'xaralampos':['mpamphs','mpampinos','xampos','xaralampakos','xaralamphs','xaralampara','xaralampoylhs'],
        'stayros':['stayrakas'],
        'petros':['petrakos','petroulhs','petrakhs','petraras','petran','peter'],
        'stelios':['stelaras','stelakos','stylianos'],
        'swthrhs':['swthrakhs','swthraras','swthrakos','swtos'],
        'thwmas':['thwmakos','thwmaras','tom','tommy'],
        'fwths':['fwtaras','fwtakhs','fwtoulhs','fwtios'],
        'grhgorhs':['grhgorios','gregory','greg'],
        'maria':['maraki','maroula','mary','mairh'],
        'elenh':['elenaki','lena','elenara','elenitsa','leniw','lenaki'],
        'katerina':['katernaki','katerinoula','katerinara','kateriniw','rina','rinaki','riniw','rinoula','aikaterinh'],
        'vasilikh':['vasw','vasilikoyla','vasoula'],
        'sofia':['sofoula','sofaki','sofy','sophy'],
        'anastasia':['anastasaki','anastasoyla','tasoyla','soula'],
        'evaggelia':['evanggelia','litsa','litsaki','litsara','vaggeliw','vaggelitsa','vanggeliw','vangellitsa'],
        'iwanna':['gianna','joanna','josh','giannoyla'],
        'eirhnh':['eirhnaki','eirhnoula','eirhnara','rhniw','rhna','peace','rhnaki','rhnoula'],
        'panagiwta':['giwta','giwtaki','giwtoula','giwtara','panagiwtaki','panagiwtara','panagiwtoula'],
        'xristina':['xristinaki','xristinara','xristinel','xristinoyla','christy'],
        'anna':['annoula','annaki','ann','anny'],
        'despoina':['despoinaki','despoinoyla'],
        'fwteinh':['fanh','fwteinaki','fwteinoula','fanitsa'],
        'alexandra':['aleka','alex','alexandroula','alexandraki'],
        'athhna':['athnoula','athhnaki','athens'],
        'nikoletta':['nicole','nikole','nikol','nikolettitsa','nikolettoula'],
        'aggelikh':['aggelikoula','aggela'],
        'gewrgia':['gwgw','gwgaki','gewrgitsa','gewrgoyla'],
        'dhmhtra':['jimhs','tzimhs','tzimakos','tzimaras','dhmhtrakos','dhmhtrakhs','mhtsos','mhtsaras','mhtsaki','jimmy','jim','jimmhs','dhmhtrios','dhmhtroula','dhmhtraki','mhtsaina'],
        'kwnstantina':['kwnstantinaki','kwnstantinoula','konstance','constance','konstanta','ntina','ntinaki','kwnstantinos','kwtsos','kwstaras','gus','kwstakhs'],
        'paraskeyh':['paraskeyoyla','voula','evh','evita','paraskeyaki']
}





