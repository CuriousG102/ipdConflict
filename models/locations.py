class Location():
    def __init__(self):
        self.resource = None
        self.mineType = None
        self.locationName = None
        self.stdMeasure = None # stdMeasure is defined such that annualLocationCapacity * stdMeasure = kgLocationCapacity

        self.annualLocationCapacity = None #in std measure
        self.ppu = None #price per unit(of stdMeasure) in nominal dollars
        self.geoLong = None
        self.geoLat = None
        self.precisionCode = None
        self.arbitraryFields = {}
    
    def getResource():
        return self.resource

    def getMineType():
        return self.mineType

    def getLocationName():
        return self.locationName

    def getStdMeasure():
        return self.stdMeasure

    def getAnnlLocCapacity():
        return self.annualLocationCapacity

    def getPpu():
        return self.ppu

    def getYrlyLocValue():
        return self.getPpu() * self.getAnnlLocCapacity()

    def getKgCapacity():
        return self.getAnnlLocCapacity() * self.getStdMeasure()

    def getPpk():
        return self.getYrlyLocValue()/self.getKgCapacity()

    def getLong():
        return self.geoLong
    
    def getLat():
        return self.geoLat
    
    def getPrecisCode():
        return self.precisionCode
    
    def getArbitFields():
        return self.arbitraryFields.copy()
        
    def setResource(resource):
        self.resource = resource
    
    def setMineType(mineType):
        self.mineType = mineType
        
    def setLocName(locName):
        self.locationName = locName
        
    def setStdMeasure(stdMeasure):
        self.stdMeasure = stdMeasure
    
    def setAnnlLocCapacity(annlCapacity):
        self.annualLocationCapacity = annlCapacity
        
    def setPpu(ppu):
        self.ppu = ppu
    
    def setLongLat(geoLong, geoLat):
        self.geoLong = geoLong
        self.geoLat = geoLat
        
    def setPrecisCode(code):
        self.precisionCode = code
     
    def setArbitField(key, value):
        self.arbitraryFields[key] = value
  
