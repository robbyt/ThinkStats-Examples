import Pmf

L = [1,2,2,3,5]
HIST = Pmf.MakeHistFromList(L)

def mode():
    mode = {}
    for val, freq in HIST.Items():
        if freq > mode.get('freq'):
            mode = {'val':val, 'freq':freq}
    return mode

def all_modes(reverse=True):
    l = []
    for key, value in sorted(HIST.GetDict().iteritems(), key=lambda (k,v): (v,k)):
        l.append((key, value))

    if reverse:
        l.reverse()

    return l
    

def main():
    m = mode()
    print "The mode of the set is %s at a frequency of %s" % (m['val'], m['freq'])

    a = all_modes()
    print "List of modes, sorted from most frequent to least:"
    print a

if __name__ == '__main__':
    main()

