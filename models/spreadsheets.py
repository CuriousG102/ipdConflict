import csv
import os.path

class Spreadsheet:

    openSheets = []

    def __init__(self):
        self.name = None
        self.table = []

    def isPresent(self, spreadsheetID):
        if self.name == None:
            return os.path.isfile(spreadsheetID)
        else:
            raise Exception("This Spreadsheet object already has a table")

    def open(self, spreadsheetID):
        # assert spreadsheet is correctly formatted
        
        if not self.isPresent(spreadsheetID):
            raise Exception("Spreadsheet does not exist")
        
        if spreadsheetID in Spreadsheet.openSheets:
            raise Exception("Spreadsheet is open in another Spreadsheet object")

        self.name = spreadsheetID
        Spreadsheet.openSheets.append(spreadsheetID)

        with open(self.name, 'rU') as f:
            reader = csv.reader(f)
            
            for row in reader:
                self.table.append(row)

    def make(self, spreadsheetID):
        if self.isPresent(spreadsheetID):
            raise Exception("Spreadsheet already exists")

        self.name = spreadsheetID
        Spreadsheet.openSheets.append(spreadsheetID)
        
        self.table.append(['Resource', 'Mine Type', 'Location Name', \
        'Standard Measure', 'Annual Location Capacity in Standard Measure', 'January PPU', 'Yearly Location Value', 'Capacity of Location in Kilograms', 'Price Per Kilogram', 'Longitude', 'Latitude', 'Precision Code'])

    def numRows(self):
        return len(self.table)

    def getRow(self, pk):
        tableRow = pk - 1 # Changing between index systems(rows start at 1, self.table starts at 0

        return self.table[tableRow].copy()

    def append(self, row):
        self.table.append(row)

    def modify(self, rowNumToChange, row):
        self.table[rowNumToChange - 1] = row

    def save(self):
        with open(self.name, 'w') as f:
            writer = csv.writer(f, dialect = 'excel')
            writer.writerows(self.table)

    def close(self):
        self.save()
        Spreadsheet.openSheets.remove(self.name)
        self.table = []

