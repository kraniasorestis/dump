minchar = 8     # minimum and maximum number of characters the final passwords may have - change this however you like
maxchar = 18

years = [
                1950,1951,1952,1953,1954,1955,1956,1957,1958,1959,1960,1961,
                1962,1963,1964,1965,1966,1967,1968,1969,1970,1971,1972,1973,
                1974,1975,1976,1977,1978,1979,1980,1981,1982,1983,1984,1985,
                1986,1987,1988,1989,1990,1991,1992,1993,1994,1995,1996,1997,
                1998,1999,2000,2001,2002,2003,2004,2005,2006,2007,2008,2009,
                2010,2011,2012,2013,2014,2015,2016,2017,2018,2019,2020
            ]

def sequences():
    return  [
                0,00,000,0000,00000,000000,0000000,00000000,000000000,123,1234,12345,123456,123123,1234567,
                12345678,123456789,123456789,135,1357,13579,1357911,135791113,246,2468,246810,24681012,2468101214,
                235,2357,235711,23571113,2357111317,112,1123,11235,112358,11235813,1123581321
            ]

def leet_dict():
    return {
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

def SpecChars():
    return ['!', '.', '@', '#', '$', '%', '*']

def Team(TeamLabel):
    TeamDict = {
        'OLY': ['thrillos', 'gayros', 'olympiakos', 'olympiakara', 'thira', 'gate', 'thrilara'],
        'PAO': ['panatha', 'panathinaikos', 'thira', 'gate', 'trifili', 'trifilara', 'vazelos', 'vazelos'],
        'AEK': ['original', 'aek', 'original', 'aek', 'aekara', 'thira', 'aekara', 'hanoumi', 'hanoumaki'],
        'PAOK': ['paok', 'toumpa', 'paoki', 'mpaok', 'paokara', 'mpaokara', 'voulgaros', 'salonika', 'thessaloniki', 'gate', 'thira'],
        'AEL': ['alogaki', 'visini', 'larisa', 'larsa', 'trakter', 'ael', 'aelara'],
        'ARIS': ['skouliki', 'salonika', 'xarilaou', 'aris', 'arianos' ]
    }
    return TeamDict[TeamLabel]


def pop_pswd():  # either very common passwords or password elements
    return  [
                'dragon','iloveyou','love','princess','master','monkey',
                'qwerty','abcdef','asdf','qazwsx','1qaz2wsx','abc123'
                'password','login','admin'
            ]

######## PLACEHOLDERS for upcomming features ########


# def swearing():
#     lista vrisiwn

# def komma():
#     analogo me thn omada

# def fav_chars
#     lista agaphmenwn xarakthrwn analoga me tainies/seires pou vlepei
