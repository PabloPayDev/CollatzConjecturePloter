def nextTermCollatzConjecture(lastTerm):
    rem = lastTerm%2
    return int(lastTerm/2) if rem==0 else ((lastTerm*3)+1)

def collatzSequence(firstTerm,nTerms):
    seq = list()
    i = 1
    seq.append(firstTerm)
    while((not (seq[-1] == 1))and(i<=nTerms)):
        i += 1
        seq.append(nextTermCollatzConjecture(seq[-1]))
    return seq