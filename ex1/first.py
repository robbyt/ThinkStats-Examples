#!/usr/bin/env python

import survey
import thinkstats

TABLE = survey.Pregnancies()
TABLE.ReadRecords()

def ex1_3_2():
    """Number of live births
    """
    d = {'live':0, 'death':0}

    for r in TABLE.records:
        if r.outcome == 1:
            d['live'] += 1
        elif r.outcome == 2:
            d['death'] += 1
    return d

def ex1_3_3():
    """Number of live, first births vs. non-first
    """
    d = {'first':0, 'other':0}

    for r in TABLE.records:
        if r.outcome == 1:
            if r.birthord == 1:
                d['first'] += 1
            else:
                d['other'] += 1
    return d

def ex1_3_4():
    first_list = []
    other_list = []

    for r in TABLE.records:
        if r.outcome == 1:
            if r.birthord == 1:
                first_list.append(r.prglength)
            else:
                other_list.append(r.prglength)

    return {'avg_first':thinkstats.Mean(first_list), 
            'avg_other':thinkstats.Mean(other_list)}

def main():
    ex2 = ex1_3_2()
    ex3 = ex1_3_3()
    ex4 = ex1_3_4()
    diff = (ex4['avg_first'] - ex4['avg_other']) * 7.0

    print "number of live: %s" % ex2['live']
    print "number of non-live: %s" % ex2['death']
    print "number of live first: %s" % ex3['first']
    print "number of live non-first: %s" % ex3['other']
    print "avg first-timers: %s weeks" % ex4['avg_first']
    print "avg non-first-timers: %s weeks" % ex4['avg_other']
    print "difference, between 1st timers and non 1st pregnancies: %s days" % diff

if __name__ == '__main__':
    main()
