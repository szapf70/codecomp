public class Starter
{
    public static void main() {
        
        Tier[] tiere = new Tier[] {new Tier(), new Hund(), new Katze()};
        
        for (Tier act : tiere) {
            act.eat();
        }
    }
}
