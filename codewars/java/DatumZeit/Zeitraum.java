import java.util.StringTokenizer;
/**
 * Klasse Zeitraum. Verwaltet einen Zeitraum in Sekunden (24.800 Tage oder 67 Jahre)
 * 
 * @author (Sascha Zapf) 
 * @version (1.0)
 */
public class Zeitraum implements Comparable<Zeitraum>
{
    // Einheit - ganze Sekunden.
    private int secs;

    /**
     * Standardkonstruktor, initialsierung mit 0
     */
    public Zeitraum()
    {
        this.secs = 0;
    }

    /**
     * Konstruktor mit Sekunden.
     * 
     * @param  secs   sekunden als init
     */
    public Zeitraum(int secs)
    {
        this.secs = secs;
    }

    /**
     * Konstruktor mit Zeitraum-String in der Form "[tage] [stunden]:[minuten]:[sekunden]".
     * 
     * @param   zrString    Zeichenkette mit speziellem Format
     */
    
    public Zeitraum(String zrString) {
        this.secs = decodezrString(zrString); 
    }
    
    public static int decodezrString(String zrString) {
        int retval = 0;
        StringTokenizer st = new StringTokenizer(zrString,":");
        retval += 86400 * Integer.valueOf(st.nextToken());
        retval += 3600 * Integer.valueOf(st.nextToken());
        retval += 60 * Integer.valueOf(st.nextToken());
        retval += Integer.valueOf(st.nextToken());
        return retval;    
    }
    
    public static String encodesrString(int secs) {
        return "0:00:00:00";
    }
    
    public void add(int secs) {
        this.secs += secs;
    }
    
    public void add(String zrString) {
        this.secs += decodezrString(zrString);
    }
        
    public Zeitraum clone() {
        return new Zeitraum(this.secs); 
    }

    public int compareTo(Zeitraum other) {
        return Integer.compare(this.secs, other.secs);
    }


}
