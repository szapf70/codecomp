import java.lang.Math;

public class Misc
{
    public static void main(String[] args) {
        System.out.println("Hello World!");
  
        double a = 30; 
  
        System.out.println(Math.sqrt(a)); 
        int[][] feld = new int[][] {{1,2,3},{1,2,3}};
        System.out.println(s2d(feld));
    
    }
    
    public static void testFibo() {

        
        
    }

    public static int s2d(int[][] arr) {
        int res = 0;
        for (int i = 0; i < arr.length; i++) {
            for (int j = 0; j < arr[0].length; j++) {
                res += arr[i][j];
            }
        }
        return res;
    }
}

