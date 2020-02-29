import Auxiliary

def add_nums(l):   # adds some numbers to the back a list's elements
    tmp = []
    for i in range(0, 10):
        tmp.append('_'+'0'+str(i))
        tmp.append('-'+'0'+str(i))
        tmp.append('.'+'0'+str(i))
    for i in range(0, 100):
        tmp.append(str(i))
        tmp.append('_'+str(i))
        tmp.append('-'+str(i))
        tmp.append('.'+str(i))
    return Auxiliary.combine(l, tmp)

def add_nums2(l):       # adds some numbers both in the front and back of the list's items
     tmp = []
     for i in range(0, 10):
        tmp.append('0'+str(i))
     for i in range(0, 100):
        tmp.append(str(i))
     return Auxiliary.combine2way(l, tmp)
