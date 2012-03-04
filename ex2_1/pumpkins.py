#!/usr/bin/env python

from numpy import array

PUMPKINS = [1,1,1,3,3,591]
N = array((PUMPKINS))

def main():
    print "Mean: %s" % N.mean()
    print "Variance: %s" % N.var()
    print "Standard Deviation: %s" % N.std()

if __name__ == '__main__':
    main()
