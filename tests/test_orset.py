__author__ = 'Salessawi Ferede Yitbarek'

from crdt.sets import ORSet

#TODO: write proper unit tests

#NOTE that the random IDs used to track keys
#are not asserted since they are uniquely generated
#for each operation


def printORSet(s):
    print s.value
    print "E:" + str(s.E)
    print "T:" + str(s.T)

    print "************************"



def orset():

    a = ORSet()
    b = ORSet()
    c = ORSet()


    print( "a:1")
    a.add(1)
    assert  a.value == {1}
    assert  set(a.T) == set()
    printORSet(a)


    print("merge: b <- a")
    b = ORSet.merge(a,b)
    assert b.value == {1}
    assert set(b.T) == set()
    printORSet(b)

    print ("remove 1 from b")
    b.discard(1)
    assert b.value == set()
    assert set(b.T) == {1}
    printORSet (b)

    print ("add 2 to b")
    b.add(2)
    assert b.value == {2}
    assert set(b.T) == {1}
    printORSet(b)

    print("Merge: a <- b")
    a = ORSet.merge(a,b)
    assert a.value == {2}
    assert  set(a.T) == {1}
    printORSet(a)


    print( "Merge: c <- b")
    c = ORSet.merge(b,c)
    assert c.value == {2}
    assert set(c.T) == {1}
    printORSet(c)

    print("Merge: c <- a")
    c = ORSet.merge(a,c)
    assert c.value == {2}
    assert set(c.T) == {1}
    printORSet(c)

    print ("Add 1 back to c")
    c.add(1)
    assert c.value == {1,2}
    assert set(c.T) == {1} #we still have observed removes
    printORSet(c)

    print ("Remove 2 from c")
    c.discard(2)
    assert c.value == {1}
    assert set(c.T) == {1,2}
    printORSet(c)


orset()
