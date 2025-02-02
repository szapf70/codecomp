public class arrtest
{
    public static void printArray(int[] arr) {
        for(int act : arr) {
            System.out.println(act);
        }
    }
    
    public static void main() {
        int[] feld = new int[] {1,3,5,7};
        System.out.println(feld);
        //printArray(feld);
        
        int[] feld2 = feld;
        //printArray(feld2);
        System.out.println(feld2);
        
        feld = new int[] {2,4,6,8,10};
        //printArray(feld);
        //printArray(feld2);
        System.out.println(feld);
        System.out.println(feld2);
        
        
        
    }
}
