from rank import *
def toUpper(value):
    if isinstance(value,str):
        return value.upper()
    elif isinstance(value,list):
        return [item.upper() for item in value]
    elif isinstance(value,set):
        lst = [item.upper() for item in value]
        return set(lst)

# keep whatever above this line uncommented


#You can use the tests individually or all together


###########################################################################################

allUnivs = readFiles("universities.csv", "capitals.csv")
t1 = len(allUnivs)==100
if t1: print("Test01- PASSED... readFiles()")
else : print("Test01- FAILED... readFiles()")


###########################################################################################
allUnivs = readFiles("wrongFileNAme.xzy", "capitalasdfas asfda sdfa sfasdfs.csv")
t1 = allUnivs==False
if t1: print("Test02- PASSED... readFiles()")
else : print("Test02- FAILED... readFiles()")


###########################################################################################

allUnivs = readFiles("universities.csv", "capitals.csv")
codes = getAllCodes(allUnivs)

t1 = isinstance(codes,set)
t2 = codes == {'ZZUH', 'SBCU', 'PBST', 'CTVT', 'RZOU', 'BRGQ', 'TYSY', 'KEEF', 'HAYS', 'XJMX', 'YADT', 'DWYC', 'IEOJ', 'NDAN', 'JDBS', 'IJVJ', 'YKYZ', 'JRFB', 'GRGT', 'LYZP', 'CBPR', 'MVPR', 'UHOI', 'KJVT', 'ISTQ', 'XSWD', 'SLWT', 'RLIS', 'NJDZ', 'KYAQ', 'JEBR', 'PWZD', 'SOTY', 'UULK', 'AZLR', 'ACYE', 'WUJO', 'PPIS', 'GPKM', 'VPNN', 'ISRL', 'FXGR', 'QQRH', 'VCNF', 'DIBN', 'FOSJ', 'TMQF', 'GRXQ', 'HQLO', 'IUAA', 'QRPK', 'XYFL', 'ZTND', 'RRWA', 'BXVP', 'ECTX', 'SBXL', 'YOUD', 'BQMQ', 'HGLJ', 'EQNG', 'AGON', 'GFBA', 'YRRV', 'LAGA', 'JXVG', 'JTEZ', 'YJBC', 'UEQW', 'YJBX', 'YGZH', 'XVMI', 'VISE', 'UPIB', 'OIOY', 'CZEG', 'CLMB', 'XDXZ', 'XDCQ', 'FKCK', 'YEJI', 'ZFUO', 'POLK', 'FXML', 'IKAQ', 'VPPB', 'ARSX', 'MZDG', 'TDEG', 'OTTE', 'OSVY', 'OPDS', 'GSHV', 'KNYG', 'ZUIF', 'GNTP', 'MJQW', 'LYTB', 'SHZX', 'SMJK'}
if t1 and t2: print("Test03- PASSED... getAllCodes()")
else : print("Test03- FAILED... getAllCodes()")


###########################################################################################
allUnivs = readFiles("universities.csv", "capitals.csv")
countries=getDistinctCountries(allUnivs)
t1 = isinstance(countries,set)
t2 = toUpper(countries) == {'UNITED KINGDOM', 'CANADA', 'DENMARK', 'SWEDEN', 'AUSTRALIA', 'FRANCE', 'ISRAEL', 'GERMANY', 'USA', 'SWITZERLAND', 'SINGAPORE', 'CHINA', 'TAIWAN', 'NORWAY', 'JAPAN', 'NETHERLANDS', 'SOUTH KOREA'}
if t1 and t2: print("Test04- PASSED... getDistinctCountries()")
else : print("Test04- FAILED... getDistinctCountries()")


###########################################################################################
allUnivs = readFiles("universities.csv", "capitals.csv")
continents=getDistinctContinents(allUnivs)
t1 = isinstance(continents,set)
t2 = toUpper(continents) =={'ASIA', 'AUSTRALIA', 'EUROPE', 'NORTH AMERICA'}
if t1 and t2: print("Test05- PASSED... getDistinctContinents()")
else : print("Test05- FAILED... getDistinctContinents()")


############################################################################################
allUnivs = readFiles("universities.csv", "capitals.csv")
result=getTopIntRank("United Kingdom", allUnivs)
t1 = isinstance(result,tuple)
t2 = result[0] == 4
t3= toUpper(result[1])==toUpper("UNIVERSITY OF CAMBRIDGE")
if t1 and t2 and t3: print("Test06- PASSED... getTopIntRank()")
else : print("Test06- FAILED... getTopIntRank()")


############################################################################################
allUnivs = readFiles("universities.csv", "capitals.csv")
result=getTopNatRank("jaPAN", allUnivs)
t1 = isinstance(result,tuple)
t2 = result[0] == 1
t3= toUpper(result[1])==toUpper("UNIVERSITY OF TOKYO")
if t1 and t2 and t3: print("Test07- PASSED... getTopNatRank()")
else : print("Test07- FAILED... getTopNatRank()")


############################################################################################
allUnivs = readFiles("universities.csv", "capitals.csv")
score=getAvgScore("usa", allUnivs)
t1 = score==86.59
score=getAvgScore("france", allUnivs)
t2 = score==86.2
if t1 and t2: print("Test08- PASSED... getAvgScore()")
else : print("Test08- FAILED... getAvgScore()")


############################################################################################
# allUnivs = readFiles("universities.csv", "capitals.csv")
# avg=getRelativeScoreContinent("Netherlands", allUnivs)
# t1 = avg==87.64
# avg=getRelativeScoreContinent("germany", allUnivs)
# t2 = avg==88.79
# if t1 and t2: print("Test09- PASSED... getRelativeScoreContinent()")
# else : print("Test09- FAILED... getRelativeScoreContinent()")


############################################################################################
allUnivs = readFiles("universities.csv", "capitals.csv")
names=getUnivWithCapital('usa', allUnivs)
t1 = isinstance(names,set)
t2 = toUpper(names)=={'FKCK', 'PPIS'}
names=getUnivWithCapital('united kingdom', allUnivs)
t3 = isinstance(names,set)
t4 = toUpper(names)=={'HQLO', 'QQRH', 'YKYZ'}
if t1 and t2 and t3 and t4: print("Test10- PASSED... getUnivWithCapital()")
else : print("Test10- FAILED... getUnivWithCapital()")


############################################################################################
# allUnivs = readFiles("universities.csv", "capitals.csv")
# codes=studyInOnePlace('Switzerland', ['MSc','PhD'], 7000,allUnivs)
# t1 = isinstance(codes,set)
# t2 = len(codes)==0
# codes=studyInOnePlace('Switzerland', ['MSc','PhD'], 45000,allUnivs)
# t3 = isinstance(codes,set)
# t4 = toUpper(codes) =={'DIBN', 'HGLJ', 'ACYE', 'TYSY'}
# codes=studyInOnePlace('usa', ['MSc','PhD'], 15000,allUnivs)
# t5 = isinstance(codes,set)
# t6 = toUpper(codes) =={'YJBX', 'FOSJ', 'YRRV'}
# if t1 and t2 and t3 and t4 and t5 and t6: print("Test11- PASSED... studyInOnePlace()")
# else : print("Test11- FAILED... studyInOnePlace()")



############################################################################################
# allUnivs = readFiles("universities.csv", "capitals.csv")
# tf=studyInTwoPlaces('TDEG','Bsc','GRXQ',"MEng",290000,allUnivs)
# t1= tf==True
# try:
#     tf=studyInTwoPlaces('GRXQ',"MEng",'TDEG','Bsc',20000,allUnivs)
# except ValueError as ve:
#     t2 = True
# tf=studyInTwoPlaces('TDEG','Bsc','GRXQ',"MEng",1000,allUnivs)
# t3 = tf==False
# if t1 and t2 and t3: print("Test12- PASSED... studyInTwoPlaces()")
# else : print("Test12- FAILED... studyInTwoPlaces()")