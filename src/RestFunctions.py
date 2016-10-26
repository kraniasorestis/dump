import time
def rev(l): # append a list with the reversed versions of its strings
	tmp = []
	for i in l:
		tmp.append(str(i)[::-1])
	for i in tmp:
		l.append(i)


def write_out(x):     # final function - creating the file with the wordlist
	mylist = file('wordlist_%s.txt' % time.strftime('%d-%m-%Y_%H:%M'), 'w')
	mylist.write(x)
	mylist.close
	print "[+] created a wordlist with %d passwords" % len(final_list)
	raw_input("\n\npress enter to exit")
	exit()
