import csv
from models.countryYear import Entries
from models.locations import Location

class Producer:

    def __init__(self, usgsSourceName,\
    stdValuesDict = {'mt':1000, 'kg':1, 'troy oz':0.0311034768\
                     'dmtu fe':1000}, entryPath):

        self.entryPath = entryPath
        self.usgsSourceName = usgsSourceName
        f = open(self.usgsSourceName, 'rU')
        usgsReader = csv.reader(f)
        self.usgsTable = []
        for line in usgsReader:
            self.usgsTable.append(line)
        f.close()
        self.stdValues = stdValuesDict
    
    def produce(self, inFileName, country, year):
        entries = Entries(country, year, self.entryPath)
        inFile = open(inFileName, 'rU')
        usgsReader = csv.reader(inFile)
        usgsReader.next() # dispose of header row

        for line in usgsReader:
            newLoc = Location()
            newLoc.resource = line[0]
            newLoc.stdMeasure = line[1]
            newLoc.locName = line[2]
            newLoc.annualLocationCapacity = line[3]

            findValues(newLoc, year)
            entries.makeEntry(newLoc)

        entries.save()
        entries.close()

    def findValues(self, newLoc, year):
        NEEDS_COMMOD = -1
       
        commodIndex = self.usgsTable[4]
        commodToFind = newLoc.resource
       
        for i in range(0, len(commodIndex)):
            commod = commodIndex[i]
            if commod.lower() in commodToFind.lower():
                units = self.usgsTable[5][i]
                units = units.strip('()')
                units = units.split('/')
                isCents = None
               
                if units[0] == '$':
                    isCents = False
                else:
                    isCents = True
                
                usgsStdValue = None

                if units[1].lower() in self.stdValues.keys():
                    usgsStdValue = self.stdValues[units[1].lower()]
                
                if usgsStdValue != None and newLoc.stdMeasure != None
                    and newLoc.annualLocationCapacity != None:

                    usgsMultiplier = newLoc.stdMeasure/usgsStdValue
                    newLoc.ppu = getPpu(usgsMultiplier, year, isCents, i)
                break

    def getPpu(self, usgsMultiplier, year, isCents, index):
        yearKey = str(year) + "M01"
        row = None
        for i in range(0, len(self.usgsTable)):
            if self.usgsTable[i][0] == yearKey:
                row = i
                break

        if row != None:
            dollarString = self.usgsTable[row][index]
            if __is_number(dollarString):
                dollarNum = float(dollarString)
                if isCents:
                    dollarNum = dollarNum/100
                return dollarNum*usgsMultiplier

            else:
                return None

    def __is_number(s):
        try:
            float(s)
            return True
        except ValueError:
            return False

