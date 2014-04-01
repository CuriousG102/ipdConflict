# Entries works as follows: 
# Requests: Client requests an entry based on primary key (corresponds to row). Entries instantiates a Location class from the spreadsheet passed to it using gData representing the request and returns it to the client. Client can do what they wish with this class.

# Writes: Client decides to write a new entry by creating an instance of the Location class. Once they are ready to write it, they pass it to a method of Entrieswhich commits it to the spreadsheet.

# After fiddling and consideration, the decision was made to make a class called Spreadsheet. This class will have all of the methods required to perform the tasks of entries, but will conveniently allow for another layer of abstraction. Spreadsheets might use a CSV as a storage medium, an SQL database, a google doc, or anything else imaginable. The idea is that the storage medium can easily be changed without the need to make extensive modifications to the rest of the program

import Spreadsheet

class Entries:
    def __init__(self, country, year):
        spreadsheetID = "ipdConflict" + country + str(year)
        self.table = Spreadsheet()
        if self.table.isPresent(spreadsheetID):
            self.table.open(spreadsheetID)
        else:
            self.table.make(spreadsheetID)

    def getNumEntries():
        return self.table.numRows() - 1 # return number of rows - 1 (excluding column labels)

    def getEntry(pk):
        if pk > getNumEntries + 1 or pk < 2: # if the primary key is out of bounds, raise exception
            raise ValueError("pk out of bounds")

        row = self.table.getRow(pk)
        entry = self.__processRow(row)
        return entry
    
    def makeEntry(location):
        pk = self.getNumEntries() + 2
        self.changeEntry(pk, location)    

    def changeEntry(pk, location):
        rowToInsert = pk
        # make an array of items to insert into row, pass that array to spreadsheet while specifying row 
