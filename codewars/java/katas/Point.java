
/**
 * 2 Dimensionaler Punkt im Kartesichen Raum.
 * 
 * @author Sascha Zapf 
 * @version 06.01.2025
 */

public class Point
{
    // Instanzvariablen - ersetzen Sie das folgende Beispiel mit Ihren Variablen
    private int x;
    private int y;

    /**
     * Konstruktor für Objekte der Klasse Point
     */
    public Point(int x_pos, int y_pos)
    {
        // Instanzvariable initialisieren
        x = x_pos;
        y = y_pos;
    }

    /**
     * Move verschiebt den Punkt um die beiden übergebenen Offsets.
     * 
     * @param  x_offs   Offsetwert für die X-Koordinate.
     * @param  y_offs   Offsetwert für die Y-Koordinate.
     */
    public void move(int x_offs, int y_offs)
    {
        x += x_offs;
        y += y_offs;
    }
    
    public String to_String() {
        return String.valueOf(x) + '/' + String.valueOf(y);
    }
}
