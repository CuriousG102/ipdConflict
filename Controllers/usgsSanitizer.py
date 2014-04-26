import csv

def Sanitizer(inFile, outFile):
    """Sanitizer is a method that serves the purpose of taking raw datasheets
    from USGS and transforming them into csv datasheets of the following
    format:
    __|Commodity|StdMeasure|Location Name|AnnlCapacity|__"""

    reader = csv.reader(inFile, dialect = 'excel')
    inTable = []
    for line in reader:
        inTable.append(line)

    row = 0
    for row in inTable:
        col = 0
        startRow = None
        commodityCol = None

        for cell in row:
            if 'Commodity' in cell:
                commodityCol = col
                startRow = row + 1
            col += 1

        if not startRow is None:
            break

        row += 1
   
    writer = csv.writer(outFile, dialect = 'excel')
    writer.writerow(['Commodity', 'StdMeasure', 'Location Name', 'Annual Capacity'])

    for i in range(startRow, len(inTable)):
        row = inTable[i]
        commodity = row[commodityCol]
        stdMeasureInfo = row[commodityCol + 1]
        locName = row[commodityCol + 5]
        annlCapacityInfo = row[commodityCol + 7]
        stdMeasure = _getStdMeasure(stdMeasureInfo,default = 1000)
        commodity, annlCapacity = _getCapacity(commodity, annlCapacity)
        writer.writerow([commodity, stdMeasure, locName, annlCapacity])

def _getStdMeasure(stdMeasureInfo, default = 1000):
    """takes a string, stdMeasureInfo, and returns a number to convert
       annlCapacity to kg, otherwise returning default if stdMeasureInfo has
       no specified value"""

    if len(stdMeasureInfo) == 0:
        return default
    



