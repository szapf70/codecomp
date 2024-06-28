import sys

import basestat


class SZStatPro(basestat.BaseStat):
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
   
    def __init__(self, data, window=0):
        self._window = window
        self._max = 0
        self._min = sys.maxsize 
        self._sum = 0
        
        if not self._window or len(data) < self._window:        
            self._data = data.copy()
        else:
            self._data = data.copy()[-self._window:]
            
        self._len = len(self._data)
            
        for v in self._data:
            self._sum += v     
            if v > self._max:
                self._max = v
            if v < self._min:
                self._min = v

        self._mean = self._sum / self._len                
                
    
    def addValue(self,value):
        if not self._window or len(self._data) < self._window:        
            self._data.append(value)
            if value < self._min:
                self._min = value
            if value > self._max:
                self._max = value
            self._sum += value
            self._len += 1
            self._mean = self._sum / self._len
            
        else:
            if value < self._min:
                self._min = value
            if value > self._max:
                self._max = value
            
            r = self._data.pop(0)
            self._data.append(value)
            if r == self._min or r == self._max:
                self._min = sys.maxsize
                self._max = 0            
                for v in self._data:
                    if v > self._max:
                        self._max = v
                    if v < self._min:
                        self._min = v    

            self._sum -= r
            self._sum += value
            self._mean = self._sum / self._len

    def getMin(self):
        """
        Berechnet das Minimum der Datenliste
        
        Rückgabewert
        
        int 
            Kleinster Wert in der Datenliste
        
        """
        return self._min        
        
    def getMax(self):
        """
        Berechnet das Maximum der Datenliste
        
        Rückgabewert
        
        int 
            Größter Wert in der Datenliste
        
        """
        return self._min   
        
    def getRange(self):
        """
        Berechnet die Spannweite in der Datenliste
        
        Rückgabewert
        
        int
            Differenz des größten zum kleinsten Wert in der Datenliste.
            
        """

        return self._max - self._min
    
    def getMean(self):
        """
        Berechnet den Mittelwert der Datenliste.
        
        Rückgabewert
        
        float
            Mittelwert der Datenliste.
        
        """
        return self._mean            

    def getMedian(self):
        """
        Berechnet den Median der Datenliste.
        
        Rückgabewert
        
        float
            Median der Datendatenliste.
        
        """

        lData = []
        
        if not self._window or len(self._data) < self._window:        
            lData = sorted(self._data)
        else:
            lData = sorted(self._data[-self._window:])

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
        
        lVariance = 0
        lData = []
        
        if not self._window or len(self._data) < self._window:        
            lData = self._data
        else:
            lData = self._data[-self._window:]
        
        for v in lData:
            lVariance += (v - self._mean)**2
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
    
    def Desc(self):
        """
        Ruft alle statistischen Methioden der Klasse auf.
        
        Rückgabewert
            Dictionary mit den statistischen Kennzahlen
        
        
        """
        return {"min" : self._min,
                "max" : self._max,
                "range" : self._max - self._min,
                "median" : self.getMedian(),
                "mean" : self._mean,
                "variance" : self.getVariance(),
                "stddev" : self.getStdDev()}
    
    def Report(self):
        """
        Erstellt einen formatierten Bericht über die statistischen Kennzahlen
        
        Rückgabewert
            Mehrzeiliger String
                
        """
        
        rep = f"Report for {super().__str__()}\n"
        d = self.Desc()
        rep += f"Data count: {len(self._data)}\n"
        rep += f"Minvalue:   {d['min']:>10}\n"
        rep += f"Maxvalue:   {d['max']:>10}\n"
        rep += f"Range:      {d['range']:>10}\n"
        rep += f"Median:     {d['median']:>10}\n"
        rep += f"Mean:       {d['mean']:>10.2f}\n"
        rep += f"Variance:   {round(d['variance'],2):>10.2f}\n"
        rep += f"StdDev:     {round(d['stddev'],2):>10.2f}\n"
        return rep
    