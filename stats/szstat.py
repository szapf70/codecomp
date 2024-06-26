import sys
import basestat


class SZStat(basestat.BaseStat):
    """
    Methoden
    
    getMin()
        Berechnet das Minimum und gibt es zurück.
        
    getMax()
        Berechnet das Maximun und gibt es zurück.
        
    getRange()
        Berechnet die Spannweite und gibt sie zurück.        
    
    getMean()
        Berechne den Mittelwert und gibt ihn zurück.
        
    getMedian()
        Berechnet den Median und gibt ihn zurück.    
    
    getVariance()
        Berechnet die Varianz und gibt sie zurück.
        
    getStdDev()
        Berechnet die Standardabweichung und gibt sie zurück.
        
    """

    def getMin(self):
        """
        Berechnet das Minimum der Datenliste
        
        Rückgabewert
        
        int 
            Kleinster Wert in der Datenliste
        
        """
        lmin = sys.maxsize 
        lData = []
        
        if not self.window or len(self.data) < self.window:
            lData = self.data
        else:
            lData = self.data[-self.window:]
        
        for v in lData:        
            if v < lmin:
                lmin = v
                        
        return lmin        
        
    def getMax(self):
        """
        Berechnet das Maximum der Datenliste
        
        Rückgabewert
        
        int 
            Größter Wert in der Datenliste
        
        """

        lmax = 0 
        lData = []
        
        if not self.window or len(self.data) < self.window:
            lData = self.data
        else:
            lData = self.data[-self.window:]
        
        for v in lData:        
            if v > lmax:
                lmax = v
                      
        return lmax   
        
    def getRange(self):
        """
        Berechnet die Spannweite in der Datenliste
        
        Rückgabewert
        
        int
            Differenz des größten zum kleinsten Wert in der Datenliste.
            
        """
        return self.getMax() - self.getMin()
    
    def getMean(self):
        """
        Berechnet den Mittelwert der Datenliste.
        
        Rückgabewert
        
        float
            Mittelwert der Datenliste.
        
        """
    
        lsum = 0 
        lData = 0        

        if not self.window or len(self.data) < self.window:
            lData = self.data
        else:
            lData = self.data[-self.window]

        for v in lData:        
            lsum += v
        return lsum / len(lData)            

    def getMedian(self):
        """
        Berechnet den Median der Datenliste.
        
        Rückgabewert
        
        float
            Median der Datendatenliste.
        
        """

        lData = []
        
        if not self.window or len(self.data) < self.window:        
            lData = sorted(self.data)
        else:
            lData = sorted(self.data[-self.window:])

        if len(lData)%2:
            return lData[len(lData)//2]
        else:
            return (lData[(len(lData)//2)-1] + lData[len(lData)//2])/2
            
    def getVariance(self):
        """
        Berechnet die Varianz der Datenliste.
        
        Rückgabewert
        
        float
            Varianz der Datenliste.
        
        """    
        
        lMean = self.getMean()
        lVariance = 0
        lData = []
        
        if not self.window or len(self.data) < self.window:        
            lData = self.data
        else:
            lData = self.data[-self.window:]
        
        for v in lData:
            lVariance += (v - lMean)**2
        lVariance /= len(lData)
        
        return lVariance    
        
    def getStdDev(self):
        """
        Berechnet die Standardabweichung.
        
        Rückgabewert
        
        float
            Standardabweichung der Datenliste
            
        """    
        
        return self.getVariance() ** 0.5
    
    