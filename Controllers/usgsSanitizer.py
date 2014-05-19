import csv

def Sanitizer(inFile, outFile, stdMeasures = {'carat':0.0002, 'kilogram':1}):
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
	
    writer = csv.writer(outFile, dialect = 'excel')
    writer.writerow(['Commodity', 'StdMeasure', 'Location Name', 'Annual Capacity'])

    lastCommodity = None
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
        stdMeasure = _getStdMeasure(stdMeasureInfo, default = 1000, stdMeasures)
        commodity, annlCapacity = _getCapacity(commodity, annlCapacity)
        writer.writerow([commodity, stdMeasure, locName, annlCapacity])

def _getStdMeasure(stdMeasureInfo, default = 1000):
     """takes a string, stdMeasureInfo, and returns a number to convert
        annlCapacity to kg, otherwise returning default if stdMeasureInfo has
        no specified value"""

    if len(stdMeasureInfo) == 0:
        return default
    
     # edit here to add more stdMeasures: format is a keyword to look for and then how much the measure associated with that keyword weighs in kilograms

    keywords = stdMeasures.keys()

    for keyword in keywords:
        if keyword in stdMeasureInfo:
            return stdMeasures[keyword]

    return None # there is a specified value, but it does not match with any of the keywords

def _getCapacity(commodity, annlCapacity):
    commodToReturn = commodity
    annlCapacityToReturn = ""

    doneTakingDigits = False
    for character in annlCapacity:
        if character.isdigit() and not doneTakingDigits:
            annlCapacityToReturn += character
        else if character == ',' and not doneTakingDigits:
            pass
        else if character == '.' and not doneTakingDigits:
            annlCapacityToReturn += character
        else:
            doneTakingDigits = True
            if character.isalpha():
                commodToReturn += character
    
    annlCapacityToReturn = float(annlCapacityToReturn)

    return commodToReturn, annlCapacityToReturn

def stripRowsWithoutCommodity(inTable, commodityCol, startRow):

	i = startRow

	while(i < len(inTable)):
		row = inTable[i]
        if not row[commodityCol]: # commodityCol is empty
            rowUp = inTable[i-1]
            for j in range(0, len(row)):
                rowUp[j] += row[j]
            inTable.pop(i)
        else:
            i += 1










