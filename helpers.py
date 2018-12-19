from nltk.tokenize import sent_tokenize




def lines(a, b):
    """Return lines in both a and b"""
    #create a set for files one and two, split by the (\n)
    setA = set(a.split('\n'))
    setB = set(b.split('\n'))

    #return a set with the itersection of 1 and 2
    setFound = setA.intersection(setB)
    return list(setFound)


def sentences(a, b):
    """Return sentences in both a and b"""
    #create a set for files one and two, split by the sentence
    setA = set(sent_tokenize(a))
    setB = set(sent_tokenize(b))

    #return a set with the itersection of 1 and 2
    setFound = setA.intersection(setB)
    return list(setFound)


def substrings(a, b, n):
    """Return substrings of length n in both a and b"""
    def helper(string, n, permset):
        i = 0
        sl = len(string)
        for i in range(sl):
            while sl >= n:
                permset.add(string[i:n])
                i += 1
                n += 1
    fLo = a.split()
    fLt = b.split()
    i = 0
    nfLo = set()
    nfLt = set()
    for i in range(len(fLo)):
        helper(fLo[i], n, nfLo)
    for i in range(len(fLt)):
        helper(fLt[i], n, nfLt)
    copies = nfLt.intersection(nfLo)
    return list(copies)
