# Entries works as follows: 
# Requests: Client requests an entry based on primary key (corresponds to row). Entries instantiates a Location class from the spreadsheet passed to it using gData representing the request and returns it to the client. Client can do what they wish with this class.

# Writes: Client decides to write a new entry by creating an instance of the Location class. Once they are ready to write it, they pass it to a method of Entrieswhich commits it to the spreadsheet.

# After fiddling and consideration, the decision was made to make a class called Spreadsheet. This class will have all of the methods required to perform the tasks of entries, but will conveniently allow for another layer of abstraction. Spreadsheets might use a CSV as a storage medium, an SQL database, a google doc, or anything else imaginable. The idea is that the storage medium can easily be changed without the need to make extensive modifications to the rest of the program

# pk starts at 2

from spreadsheets import Spreadsheet
from locations import Location

class Entries:
    def __init__(self, country, year): # complete
        spreadsheetID = "ipdConflict" + country + str(year)
        self.table = Spreadsheet()
        if self.table.isPresent(spreadsheetID):
            self.table.open(spreadsheetID)
        else:
            self.table.make(spreadsheetID)

    def getNumEntries(self): # complete
        return self.table.numRows() - 1 # return number of rows - 1 (excluding column labels)

    def getEntry(self, pk): # complete
        if pk > self.table.numRows() or pk < 2: # if the primary key is out of bounds, raise exception
            raise ValueError("pk out of bounds")

        row = self.table.getRow(pk)
        entry = self.__processRow(row)
        return entry
    
    def makeEntry(self, location): # complete
        row = self.__getRow(location)
        self.table.append(row)

    def changeEntry(self, pk, location): # complete
        if self.table.numRows() < pk or pk < 2:
            raise ValueError("pk out of bounds")
        rowNumToChange = pk
        entry = self.__getRow(location)
        self.table.modify(rowNumToChange, entry)

    def __getRow(self, location): # complete
        # make an array of items to insert into row, pass that array to spreadsheet while specifying row 
        # order: resource, minetype, locationname, stdmeasure, annlLocCapacity in stdMeasure
        #        Jan ppu, yrlLocValue, capOfLocInKg, ppKilogram, long, lat, precisCode
        #        arbit field 1, arbit field 2, ...

        row = []

        row.extend([location.getResource(), location.getMineType(), location.getLocationName()])
        row.extend([location.getStdMeasure(), location.getAnnlLocCapacity()])
        row.extend([location.getPpu(), location.getYrlyLocValue()])
        row.extend([location.getKgCapacity(), location.getPpk(), location.getLong()])
        row.extend([location.getLat(), location.getPrecisCode()])
        # must implement arbit fields!!
        arbitFields = location.getArbitFields()

        keys = arbitFields.keys().sort()
        
        for key in keys:
            row.extend(key + '!' +  arbitFields[key])
        
        return row

    def __processRow(self, row): # complete #given row, returns location
        locToReturn = Location()
        l = locToReturn

        functionsToCall = [l.setResource, l.setMineType, l.setLocName, l.setStdMeasure,\
                           l.setAnnlLocCapacity, l.setPpu, l.setLongLat, l.setPrecisCode]
        
        i = 0

        while i <= 5:
            functionsToCall[i](row[i])
            i += 1

        l.setLongLat(row[9], row[10])
        l.setPrecisCode(row[11])

        i = 12

        while i < len(row):
            arbitKeyValue = row[i]
            key, value = arbitKeyValue.partition('!')[0], arbitKeyValue.partition('!')[2]
            l.setArbitField(key, value)
            
        return locToReturn        

    def save(self):
        self.table.save()

	def close(self):
		self.table.close()
