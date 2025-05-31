import csv
import numpy as np
# #constants

def readFiles(UniFileName, capitalsFileName,capitals=False,universities=False):

    countries = []
    allUnivs = {}
    uni=[]
    try:
        # read capitalsFileName
        with open(capitalsFileName,'r') as capitals_file:
            reader = csv.reader(capitals_file)
            countries_header = next(reader)
            for row in reader:
                countries.append(row)
                
        # read UniFileName
        with open(UniFileName,'r') as uni_file:
            reader = csv.DictReader(uni_file)
            
            for row in reader:
                key = row['Code']
                allUnivs[key]={k:v for k,v in row.items()}
            uni_file.seek(0)
            nreader = csv.reader(uni_file)
            next(nreader)
            for row in nreader:
                uni.append(row)
            
                
        
        
        if capitals:
            return countries
        if universities:
            return uni
                
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


def getDistinctContinents(allUnivs,countries_file='capitals.csv'):
    continents=set()
    #reading capitals_file to get continents 
    countries={}
    with open(countries_file,'r') as cap_file:
        reader = csv.reader(cap_file)
        for row in reader:
            countries[row[0]]=row[-1]

        
    temp_dict={}
    distinctContinents = set()
    # your code is here
    for i in allUnivs.values():
        country = i['Country']
        distinctContinents.add(countries.get(country,'NA'))
        temp_dict[country.upper()]=countries.get(country,'NA')
    # with open('universities.csv','w',newline='') as uniFile:
    #     writer = csv.DictWriter(uniFile,fieldnames='Continent')
    #     writer.writeheader()
    #     for row in allUnivs.values()
    #     writer.writerows(temp_dict)
    return distinctContinents,temp_dict


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
    sum=0
    count=0
    for row in allUnivs.values():
        if row.get('Country').upper()==countryName:
            sum+=float(row.get('Score'))
            count+=1
    return round(sum/count,2) 

import numpy as np
def getRelativeScoreContinent(countryName, allUnivs):
    countryName = countryName.upper()
    # your code is here
    countries=[]
    continents = getDistinctContinents(allUnivs)[1]
    continent = continents[countryName]
    for k,v in continents.items():
        if v==continent:
            countries.append(k)

    avg=getAvgScore(countryName,allUnivs)
    maxx=0
    for row in allUnivs.values():
        if row['Country'].upper() in countries:
            maxx = max(maxx,float(row['Score']))
            
    return round(100*avg/maxx,2)

import numpy as np
def getUnivWithCapital(countryName, allUnivs):
    univsWithCapital=set()
    countryName = countryName.upper()
    # your code is here
    capitals = {}
    capital=''
    
    #geting countries for capitals
    countries=readFiles('universities.csv','capitals.csv',True)
    
    #using numpy array for faster fetching and comparing
    countries = np.char.upper(np.array(countries))
    arr = countries[:,0]==countryName
    countries = countries[arr]
    capital = countries[0,1]
    
    for row in allUnivs.values():
        if row['Country'].upper()==countryName and capital.upper() in row['Institution name'].upper():
            univsWithCapital.add(row['Code'])

    return univsWithCapital


def studyInOnePlace(countryName, degrees, budget,allUnivs):
    countryName = countryName.upper()
    codes=set()
    degrees = set( [d.upper() for d in degrees])
    Degrees = np.array(degrees)
    # your code is here
    universities = readFiles('universities.csv','capitals.csv',False,True)
    universities = np.char.upper(np.array(universities))
    #boolean indexing if using & () mandatory and check dtypes...
    country = universities[(countryName==universities[:,3]) & (budget>=universities[:,-2].astype(int))]
    
    print(country)
    
    
    
    
    return codes

# ['Code' 'World Rank' 'Institution name' 'Country' 'National Rank' 'Degrees Offered' 'Average Cost' 'Score']

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


    
    
