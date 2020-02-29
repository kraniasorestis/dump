import Setup
import Auxiliary
import Numbers

def names():        # populates the nameslist
    tmp=[]
    while True:
        surname = raw_input("\n[+] target's surname - press ENTER if you don't know it > ")
        if surname == "":
            pass
        else:
            tmp.append(surname)

        firstname = raw_input("\n[+] target's firstname - press ENTER if you don't know it' > ")
        if firstname == "":
            break
        else:
            tmp.append(firstname)
            tmp.append(surname)
            tmp.append(surname + firstname)
            tmp.append(firstname + surname)
            break

    print "\n[+] any other relevant names/surnames (eg partner, child, pets or best friends) or press ENTER to move on > "
    while True:
        name = raw_input("[+] enter a name (or press ENTER) >  ")
        if name == "":
            break
        else:
            tmp.append(name)
    return  tmp


def pop_pass():
    tmp = []
    print "\n\n[+] Do you want to include some popular passwords?"
    while True:
        q = raw_input("\n[+] y/n. > ")
        if q == 'n':
            break
        elif q == 'y':
            tmp += Auxiliary.chop(Setup.pop_pswd)
            tmp += Auxiliary.chop(Setup.sequences)
            tmp += Auxiliary.chop(Auxiliary.rev(Setup.sequences))
            tmp += Auxiliary.chop(Auxiliary.one_char_psw())
            break  
        else:
            print "\n[!] please type y/n or press ENTER"
    return tmp


def births():    # create a list with variations on dates of birth
    tmp=[]
    print "\n[+] If you know any birthdates (target's, his/her partner's, kid's etc):"
    while True:
        x = raw_input("[+] Enter in DDMMYYYY format (or press ENTER to move on)>  ")
        if x == '':
            break
        elif len(x) == 8:
            tmp += (x, x[2:], x[:4], x[:2]+'_'+x[2:4]+'_'+x[4:], x[:2]+'_'+x[2:4]+'_'+x[6:], x[:4]+x[6:], x[:2]+'_'+x[2:4], x[2:4]+'_'+x[4:], x[2:4]+'_'+x[6:], x[:2]+'.'+x[2:4]+'.'+x[4:], x[:2]+'-'+x[2:4]+'-'+x[4:], x[:2]+'-'+x[2:4]+'-'+x[6:], x[:2]+'.'+x[2:4]+'.'+x[6:], x[:2]+'.'+x[2:4], x[:2]+'-'+x[2:4], x[2:4]+'.'+x[4:], x[2:4]+'-'+x[4:], x[2:4]+'.'+x[6:], x[2:4]+'-'+x[6:])
        else:
            print "DDMMYYYY requires 8 characters!"
    return tmp


def telephone():
    tmp = []
    print "\n[+] Type his telephone numbers if you know them"
    while True:
        tel = raw_input("[+] Telephone (or press ENTER to move on) >  ")
        if tel == "":
            break
        else:
            tmp.append(tel)
    return tmp


def interests():
    tmp = []
    print "\n[+] Additional keywords - (place of birth, maybe a favorite artist/director/game? etc)"
    while True:
        interest = raw_input("[+] enter an interest (or press ENTER to move on) >  ")
        if interest == "":
            break
        else:
            tmp.append(interest)
    return tmp

def nums(l):
    tmp = []
    print "\n[+] Do you want to append numbers (01-100) to each password?\n[!] This will increase the wordlist size many times over. [!]"
    while True:
        ans = raw_input("\n[+] y/n > ")
        if ans == 'n':
            break
        elif ans == 'y':
            tmp += Numbers.add_nums(l)
            tmp += Numbers.add_nums2(l)
            break  
        else:
            print "\n[!] please type y/n or press ENTER [!]"
    return tmp

def leet(l):
    while True:
        leet = raw_input("\n[+] Do you want to use leet mode?\n[!] This will increase the wordlist size manyfold. [!]\n[+] y/n > ")
        if leet == 'n':
            break
        elif leet == 'y':
            Auxiliary.leet(l)
            break  
        else:
            print "\n[!] please type y/n or press ENTER"
    return l

def vulgar():
    tmp = []
    print "\n[+] Could he be using a vulgar password? (y/n)> "
    while True:
        vulgar = raw_input("\n[+] y/n > ")
        if vulgar == 'y':
            tmp += Setup.vulgar
            break
        elif vulgar == 'n':
            break
        else:
            print "\n[!] please type y/n or press ENTER"
    return tmp






