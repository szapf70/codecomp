from abc import ABC, abstractmethod

class BaseStat(ABC):
    """
    Interface für Klassen zur Berechnung grundlegender statitischer Kennzahlen.
    Bei der Instanzierung wird festgelegt ob die Kennzahlen immer für die gesamten Daten
    oder nur für die letzten n Daten berechnet werden soll. Diese Eigenschaft kann zur Lebensdauer des
    Objekts nicht mehr geändert werden.
    
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
    
    def getReport(self):
        rep = f"Report for {super().__str__()}\n"
        rep += f"Minvalue: {self.getMin():>10}\n"
        rep += f"Maxvalue: {self.getMax():>10}\n"
        rep += f"Range:    {self.getRange():>10}\n"

        rep += f"Median:   {self.getMedian():>10}\n"
        rep += f"Mean:     {self.getMean():>10}\n"
        rep += f"Variance: {round(self.getVariance(),3):>10}\n"
        rep += f"StdDev:   {round(self.getStdDev(),3):>10}\n"

        return rep
    