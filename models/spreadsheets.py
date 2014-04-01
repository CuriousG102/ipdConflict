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
        
        if spreadsheetID in openSheets:
            raise Exception("Spreadsheet is open in another Spreadsheet object")

        self.name = spreadsheetID
        openSheets.append(spreadsheetID)

        with open(self.name, 'r') as f:
            reader = csv.reader(f, dialect = 'excel')
            
            for row in reader:
                self.table.append(row)

    def make(self, spreadsheetID):
        if self.isPresent(spreadsheetID):
            raise Exception("Spreadsheet already exists")

        self.name = spreadsheetID
        openSheets.append(spreadsheetID)
        
        self.table.append(['Resource', 'Mine Type', 'Location Name', \
        'Standard Measure', 'Annual Location Capacity in Standard Measure', 'January PPU', 'Yearly Location Value', 'Capacity of Location in Kilograms', 'Price Per Kilogram', 'Longitude', 'Latitude', 'Precision Code'])
         
