import java.util.ArrayList;

/**
 * Beschreiben Sie hier die Klasse protest.
 * 
 * @author (Ihr Name) 
 * @version (eine Versionsnummer oder ein Datum)
 */
public class protest
{
    public static void main(String[] args) {
        System.out.println("Test");
        
        ArrayList<String> texts = new ArrayList<>();
        
        for(int i = 0; i < 100_000; i++) {
            texts.add(Integer.toString(i));
        }
    
        System.out.println("Test - fertig");
        
    
    }
}
