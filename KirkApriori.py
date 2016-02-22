from itertools import combinations


def readFile( filename ):
    
    results = []
    fData = open( filename, 'r' )
    for line in fData :
        results.append( line[:-1] )
    return results

def singleCandidates( dataset ):
    results = []
    for transaction in dataset:
        items = transaction.split(',')
        for item in items:
            if not str([item])[2:-2] in results:
                results.append(str([item])[2:-2])
    return results

def countCandidates( dataset, singles ):
    candidateCount = {}
 
    for transaction in dataset:
        items = transaction.split(',')
        for item in items: 
            for candidate in singles:
                #print("comparing " + str(candidate)[2:-2] + " and " + str(item) )
                if candidate == item:
                    candidateCount.setdefault(candidate, 0)
                    candidateCount[candidate] += 1
    return candidateCount

def convertDicToArr( dictionary ):
    result = []
    for key in dictionary:
        result.append([key])
    return result

def totalItems( dataset ):
    total = 0
    for transaction in dataset:
        items = transaction.split(',')
        for item in items:
            total = total + 1
    return total

def supportCheck( itemCount, candidateCount, support ):
    supportNumbers = {}
    for candidate in candidateCount:
        if candidateCount[candidate] / itemCount >= support:
            supportNumbers[candidate] = ( candidateCount[candidate] / itemCount )
    return supportNumbers

def supportCheckCount( itemCount, candidateCount, support ):
    result = []
    for candidate in candidateCount:
        if candidateCount[candidate] / itemCount >= support:
            result.append( candidate)
    return result


def frequentPairs( frequentItems, dataset, itemCount, support):
    results = {}
    for transaction in dataset:
        for item in combinations( transaction, 2 ):
            results.setdefault(item, 0)
            results[item] += 1

    markForDeletion = []
    for key in results:
        if results[key]  / total < support:
            results[key] = ( results[key]  / total )
            markForDeletion.append(key)
        else:
            results[key] = ( results[key]  / total )

    for key in markForDeletion:
        results.pop( key, None )

    
    return results

    
                   

                



dataFile = 'mushroom.data'
support = .03



data = readFile( dataFile )

candidates1 = singleCandidates( data )
print( candidates1 )

counts = countCandidates( data, candidates1 )
print( counts )

total = totalItems( data )

frequentCandidates = supportCheck( total, counts, support )
print( frequentCandidates )

supportCounts = supportCheckCount( total, counts, support)
print( supportCounts )
print( data[0] )

pairs = frequentPairs( supportCounts, data, total, support )
for pair in pairs:
    print( str(pair) + str(pairs[pair]) )






