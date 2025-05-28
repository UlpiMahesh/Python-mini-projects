import csv
# #constants

def readFiles(UniFileName, capitalsFileName):
    countries = []
    allUnivs = {}
    try:
        # read capitalsFileName
        with open(capitalsFileName,'r') as capitals_file:
            reader = csv.reader(capitals_file)
            countries_header = next(reader)
            for row in reader:
                countries.append(reader)
                
        # read UniFileName
        with open(UniFileName,'r') as uni_file:
            reader = csv.DictReader(uni_file)
            for row in reader:
                key = row['Code']
                allUnivs[key]={k:v for k,v in row.items()}

    # {'Code': 'TDEG', 'World Rank': '1', 'Institution name': 'Harvard University', 'Country': 'USA', 'National Rank': '1', 'Degrees Offered': 'BSc-MSc-MEng-Diploma-MPhil-PhD', 'Average Cost': '14000', 'Score': '100'}
                
    except IOError :
        return False 
    return allUnivs




def findCountryByName(countryName, countries):
    try:
        country=False
        for row in countries:
            #modify country according to requirement
            if countryName in row:
                country=row
    except Exception as e:
        print(e.args)
    finally:
        return country



def getAllCodes(allUnivs):
    codes = set()
    # your code is here
    for unis in allUnivs.values():
        codes.add(unis['Code'])
    # can also return just keys as my keys of allUnivs is also codes
    # codes=set(allUnivs.keys())
    return codes

def getDistinctCountries(allUnivs):
    distinctCountries = set()
    # your code is here
    for unis in allUnivs.values():
        distinctCountries.add(unis['Country'])
    return distinctCountries


def getDistinctContinents(allUnivs):
    distinctContinents = set()
    # your code is here
    for unis in allUnivs:
        distinctContinents.add(unis['Conti'])
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