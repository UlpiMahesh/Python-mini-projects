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
    # # your code is here
    for unis in allUnivs.values():
        codes.add(unis['Code'])
    # # can also return just keys as my keys of allUnivs is also codes
    # # codes=set(allUnivs.keys())
    return codes

def getDistinctCountries(allUnivs):
    distinctCountries = set()
    # your code is here
    for unis in allUnivs.values():
        distinctCountries.add(unis['Country'])
    return distinctCountries


def getDistinctContinents(allUnivs,countries_file='cap.csv'):
    
    continents=set()
    #reading capitals_file to get continents 
    countries={}
    with open(countries_file,'r') as cap_file:
        reader = csv.reader(cap_file)
        for row in reader:
            countries[row[0]]=row[-1]
        
    
    distinctContinents = set()
    # your code is here
    for i in allUnivs.values():
        country = i['Country']
        distinctContinents.add(countries.get(country,'NA'))
    return distinctContinents


def getTopIntRank(countryName, allUnivs):
    countryName = countryName.upper()
    # your code is here
    intRank = 99999
    topUni = ''
    for row in allUnivs.values():
        search = row['Country'].upper()
        if search==countryName and intRank>int(row['World Rank']):
          topUni,intRank=row.get('Institution name'),int(row.get('World Rank'))
    return (intRank, topUni)


def getTopNatRank(countryName, allUnivs):
    countryName = countryName.upper()
    # your code is here
    natRank=1 #assuming that each country has top rank as 1 
    topUni = ''
    for row in allUnivs.values():
        if row['Country'].upper()==countryName and int(row['National Rank'])==natRank:
            topUni = row['Institution name']
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
    return 


    
    

