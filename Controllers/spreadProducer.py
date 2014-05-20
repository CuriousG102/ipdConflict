import csv
from models.countryYear import Entries
from models.locations import Location

class Producer:

    def __init__(self, usgsSourceName, entryPath, stdValuesDict = {'mt':1000, 'kg':1, 'troy oz':0.0311034768, 'dmtu fe':1000}):

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
            if newLoc.stdMeasure == "":
                newLoc.stdMeasure = None

            newLoc.locName = line[2]
            newLoc.annualLocationCapacity = line[3]
            if newLoc.annualLocationCapacity == "":
                newLoc.annualLocationCapacity = None

            self.findValues(newLoc, year)
            entries.makeEntry(newLoc)

        entries.save()
        entries.close()

    def findValues(self, newLoc, year):
        NEEDS_COMMOD = -1
       
        commodIndex = self.usgsTable[4]
        commodToFind = newLoc.resource
       
        for i in range(1, len(commodIndex)):
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
                try:
                    if units[1].lower() in self.stdValues.keys():
                        usgsStdValue = self.stdValues[units[1].lower()]
                except:
                    pass

                if usgsStdValue != None and newLoc.stdMeasure != None\
                    and newLoc.annualLocationCapacity != None:

                    usgsMultiplier = float(newLoc.stdMeasure)/usgsStdValue
                    newLoc.ppu = self.getPpu(usgsMultiplier, year, isCents, i)
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
            if self.__is_number(dollarString):
                dollarNum = float(dollarString)
                if isCents:
                    dollarNum = dollarNum/100
                return dollarNum*usgsMultiplier

            else:
                return None

    def __is_number(self, s):
        try:
            float(s)
            return True
        except ValueError:
            return False

