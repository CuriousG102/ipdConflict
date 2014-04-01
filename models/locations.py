class Location:
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
    
    def getResource(self):
        return self.resource

    def getMineType(self):
        return self.mineType

    def getLocationName(self):
        return self.locationName

    def getStdMeasure(self):
        return self.stdMeasure

    def getAnnlLocCapacity(self):
        return self.annualLocationCapacity

    def getPpu(self):
        return self.ppu

    def getYrlyLocValue(self):
        return self.getPpu() * self.getAnnlLocCapacity()

    def getKgCapacity(self):
        return self.getAnnlLocCapacity() * self.getStdMeasure()

    def getPpk(self):
        return self.getYrlyLocValue()/self.getKgCapacity()

    def getLong(self):
        return self.geoLong
    
    def getLat(self):
        return self.geoLat
    
    def getPrecisCode(self):
        return self.precisionCode
    
    def getArbitFields(self):
        return self.arbitraryFields.copy()
        
    def setResource(self, resource):
        self.resource = resource
    
    def setMineType(self, mineType):
        self.mineType = mineType
        
    def setLocName(self, locName):
        self.locationName = locName
        
    def setStdMeasure(self, stdMeasure):
        self.stdMeasure = stdMeasure
    
    def setAnnlLocCapacity(self, annlCapacity):
        self.annualLocationCapacity = annlCapacity
        
    def setPpu(self, ppu):
        self.ppu = ppu
    
    def setLongLat(self, geoLong, geoLat):
        self.geoLong = geoLong
        self.geoLat = geoLat
        
    def setPrecisCode(self, code):
        self.precisionCode = code
     
    def setArbitField(self, key, value):
        self.arbitraryFields[key] = value
  
