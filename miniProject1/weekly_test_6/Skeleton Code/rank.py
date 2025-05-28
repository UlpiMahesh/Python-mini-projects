
# #constants

def readFiles(UniFileName, capitalsFileName):
    countries = []
    allUnivs = {}
    try:
        # read capitalsFileName
        # read UniFileName
    except IOError :
        return False 
    return allUnivs

def findCountryByName(countryName, countries):
    # return country
    # OR
    # return False



def getAllCodes(allUnivs):
    codes =set()
    # your code is here
    return codes


def getDistinctCountries(allUnivs):
    distinctCountries = set()
    # your code is here
    return distinctCountries


def getDistinctContinents(allUnivs):
    distinctContinents = set()
    # your code is here
    return distinctContinents


def getTopIntRank(countryName, allUnivs):
    countryName = countryName.upper()
    # your code is here
    return (intRank, topUni)


def getTopNatRank(countryName, allUnivs):
    countryName = countryName.upper()
    # your code is here
    return (natRank, topUni)


def getAvgScore(countryName, allUnivs):
    countryName = countryName.upper()
    # your code is here
    return round(sum/count,2) 


def getRelativeScoreContinent(countryName, allUnivs):
    countryName = countryName.upper()
    # your code is here
    return round(100*avg/max,2)


def getUnivWithCapital(countryName, allUnivs):
    univsWithCapital=set()
    countryName = countryName.upper()
    # your code is here
    return univsWithCapital


def studyInOnePlace(countryName, degrees, budget,allUnivs):
    countryName = countryName.upper()
    codes=set()
    degrees = set( [d.upper() for d in degrees])
    # your code is here
    return codes


def studyInTwoPlaces(firstCode, firstDegree,secondCode , secondDegree, budget,allUnivs):
    firstDegree = firstDegree.upper()
    secondDegree = secondDegree.upper()
    firstCode = firstCode.upper()
    secondCode = secondCode.upper()
    # your code is here
    
    #     return True
    # or
    #     return False
    # or
    #     raise ValueError("Something went wrong!")