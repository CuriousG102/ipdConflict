import csv

def Sanitizer(inFile, outFile):
    """Sanitizer is a method that serves the purpose of taking raw datasheets
    from USGS and transforming them into csv datasheets of the following
    format:
    __|Commodity|StdMeasure|Location Name|AnnlCapacity|__"""

    reader = csv.reader(inFile, dialect = 'excel')
    inTable = [] # get a reader for an input csv table and set up an array inTable to receive what is read
    for line in reader: # read the csv table into inTable
        inTable.append(line)

    row = 0
	commodityCol = None
	startRow = None
	
    for row in inTable:
        col = 0

        for cell in row:
            if 'Commodity' in cell:
                commodityCol = col
                startRow = row + 1
				break
            col += 1

        row += 1
   
    # get the column # commodityCol that commodities are stored in
    # get the row on which we should start reading from the table, startRow
	
	stripRowsWithoutCommodity(inTable, commodityCol, startRow)
	# take out rows without commodity info in them, moving the contents of their cells to the cells immediately above them by appending. Strip useless stuff above data.
	
    writer = csv.writer(outFile, dialect = 'excel')
    writer.writerow(['Commodity', 'StdMeasure', 'Location Name', 'Annual Capacity'])

    for i in range(startRow, len(inTable)):
        row = inTable[i]
        commodity = row[commodityCol]
		
		if commodity.lower().strip() == "do.":
			commodity = lastCommodity
		else:
			lastCommodity = commodity
		
        stdMeasureInfo = row[commodityCol + 1]

        locName = row[commodityCol + 5]
        annlCapacityInfo = row[commodityCol + 7]
        stdMeasure = _getStdMeasure(stdMeasureInfo,default = 1000)
        commodity, annlCapacity = _getCapacity(commodity, annlCapacity)
        writer.writerow([commodity, stdMeasure, locName, annlCapacity])

#def _getStdMeasure(stdMeasureInfo, default = 1000):
#    """takes a string, stdMeasureInfo, and returns a number to convert
#       annlCapacity to kg, otherwise returning default if stdMeasureInfo has
#       no specified value"""

#    if len(stdMeasureInfo) == 0:
#        return default



#def _getCapacity(commodity, annlCapacity)

def stripRowsWithoutCommodity(inTable, commodityCol, startRow):

	i = startRow

	while(i < len(inTable)):
		row = inTable











