from abc import ABC, abstractmethod

class BaseStat(ABC):
    """
    Interface für Klassen zur Berechnung grundlegender statistischer Kennzahlen.
    Bis auf den Konstruktor und die Reportfunktion nur abstrakte Methoden
    Bei der Instanzierung wird festgelegt ob die Kennzahlen immer für die gesamten Daten
    oder nur für die letzten n Daten berechnet werden soll. Diese Eigenschaft kann zur Lebensdauer des
    Objekts nicht mehr geändert werden.
    
    Methoden
    
    addValue(value)
        Fügt den übergebenen Wert der Datenliste des Objekts hinzu.
    
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
        
    getReport()
        Erstellt einen Bericht und gibt ihn als mehrzeiligen String zurück.
    
    """
    
    def __init__(self, data, window = 0):
        """
        Konstruktor von BaseStat
        
        Parameter
        
        data : list
            Liste von Daten die schon zu Beginn zur Verfügung stehen sollen.
            
        window : int
            Größe des Fensters für die Berechnung. Das Fenster befindet sich am Ende der Datenliste.
            Bei Fenstergröße 0 werden die Berechnungen immer auf dem Kompletten Datensatz ausgeführt.        
        
        """    
        
        if not window or len(data) < window:
            self.data = data
        else:
            self.data = data[-window:] 
            
        self.window = window
    
    @abstractmethod
    def addValue(self, value):
        """
        Fügt den übergebenen Wert der Datenliste hinzu.
        
        Parameter
            Wert
        
        """    


    @abstractmethod
    def getMin(self):
        """
        Berechnet das Minimum der Datenliste
        
        Rückgabewert
        
        int 
            Kleinster Wert in der Datenliste
        
        """
        pass        

    @abstractmethod
    def getMax(self):
        """
        Berechnet das Maximum der Datenliste
        
        Rückgabewert
        
        int 
            Größter Wert in der Datenliste
        
        """
        pass
        
    @abstractmethod
    def getRange(self):
        """
        Berechnet die Spannweite in der Datenliste
        
        Rückgabewert
        
        int
            Differenz des größten zum kleinsten Wert in der Datenliste.
            
        """
        pass
    
    @abstractmethod
    def getMean(self):
        """
        Berechnet den Mittelwert der Datenliste.
        
        Rückgabewert
        
        float
            Mittelwert der Datenliste.
        
        """
        pass    
    
    @abstractmethod    
    def getMedian(self):
        """
        Berechnet den Median der Datenliste.
        
        Rückgabewert
        
        float
            Median der Datendatenliste.
        
        """
        pass
    
    @abstractmethod        
    def getVariance(self):
        """
        Berechnet die Varianz der Datenliste.
        
        Rückgabewert
        
        float
            Varianz der Datenliste.
        
        """    
        pass
  
    @abstractmethod    
    def getStdDev(self):
        """
        Berechnet die Standardabweichung.
        
        Rückgabewert
        
        float
            Standardabweichung der Datenliste
            
        """    
        pass
    
    
    def Desc(self):
        """
        Ruft alle statistischen Methioden der Klasse auf.
        
        Rückgabewert
            Dictionary mit den statistischen Kennzahlen
        
        
        """
        return {"min" : self.getMin(),
                "max" : self.getMax(),
                "range" : self.getRange(),
                "median" : self.getMedian(),
                "mean" : self.getMean(),
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
        rep += f"Data count: {len(self.data)}\n"
        rep += f"Minvalue:   {d['min']:>10}\n"
        rep += f"Maxvalue:   {d['max']:>10}\n"
        rep += f"Range:      {d['range']:>10}\n"
        rep += f"Median:     {d['median']:>10}\n"
        rep += f"Mean:       {d['mean']:>10.2f}\n"
        rep += f"Variance:   {round(d['variance'],2):>10.2f}\n"
        rep += f"StdDev:     {round(d['stddev'],2):>10.2f}\n"
        return rep
    