class Location():
    def __init__():
        resource = ""
        mineType = ""
        locationName = ""
        stdMeasure = None # stdMeasure is defined such that annualLocationCapacity * stdMeasure = kgLocationCapacity

        annualLocationCapacity = None #in std measure
        ppu = None #price per unit(of stdMeasure) in nominal dollars
        geoLong = None
        geoLat = None
        precisionCode = None
        arbitraryFields = []
    
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

    
