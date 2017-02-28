from Auxiliary import combine2

def add_nums(l):   # add some numbers to the back a list's elements
    tmp = []
    for i in range(0, 10):
        tmp.append('0'+str(i))
        tmp.append('_'+'0'+str(i))
        tmp.append('-'+'0'+str(i))
    for i in range(0, 100):
        tmp.append(str(i))
        tmp.append('_'+str(i))
        tmp.append('-'+str(i))
    return combine2(l, tmp)
