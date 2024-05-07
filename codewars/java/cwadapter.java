import java.util.*;
import java.util.stream.IntStream;

public class cwadapter {
    public static void main(String[] args) {
        System.out.println("CW Adapter");

    }

    // https://www.codewars.com/kata/55695bc4f75bbaea5100016b/train/java
    // Fibonacci Streaming

    public static IntStream generateFibonacciSequence() {
        // To be implemented: Proper implementation.
        IntStream fib = IntStream.iterate(new int[] {0,1}, pair -> new int[] {pair[1], pair[0] + pair[1]}).mapToInt(pair -> pair[0]);
    
    
        return IntStream.of(1, 1, 2, 3, 5, 8, 13);
    
    
    }




    // The observed PIN
    // https://www.codewars.com/kata/5263c6999e0f40dee200059d/train/java

    public static List<String> expand(List<String> list, Character next) {
        HashMap<Character,Character[]> ladj = new HashMap<>();
        ladj.put('0', new Character[] {'0','8'});
        ladj.put('1', new Character[] {'1','2','4'});
        ladj.put('2', new Character[] {'2','1','3','5'});
        ladj.put('3', new Character[] {'3','2','6'});
        ladj.put('4', new Character[] {'4','1','5','7'});
        ladj.put('5', new Character[] {'2','4','5', '6','8'});
        ladj.put('6', new Character[] {'3','5','6','9'});
        ladj.put('7', new Character[] {'4','7','8'});
        ladj.put('8', new Character[] {'5','7','8','9','0'});
        ladj.put('9', new Character[] {'6','8','9'});
        List<String> expanded = new ArrayList<String>();
        if ( list.isEmpty() ) {
            for (Character c : ladj.get(next)) {
                expanded.add(""+c);
            }
        } else {   
            for (String sofar: list) {
                for (Character c: ladj.get(next)) {
                    expanded.add(sofar+c);
                }
            }        
        }
        return expanded;
    }
    public static List<String> getPINs(String observed) {
        List<String> allpos = new ArrayList<>();
        for (Character ch: observed.toCharArray()) {
            allpos = expand(allpos, ch);
        }
        Collections.sort(allpos);
        return allpos;
    }    


    public static String formatDuration(int seconds) {
        if (seconds == 0) {
            return "now";
        }
        String[] names = new String[] {"year", "day", "hour", "minute", "second"};
        Integer[] stable = new Integer[] {31_536_000,86_400,3_600,60,1};
        Integer[] ctable = new Integer[] {0,0,0,0,0};
        String[] filler =  new String[] {"s", ", ", " and "};
        Integer pc = 0;

        for (int cidx = 0; cidx <= 4; cidx++) {
            while (seconds >= stable[cidx]) {
                seconds -= stable[cidx];
                ctable[cidx]++;
            }
            if (ctable[cidx] > 0) {
                pc++;
                if (ctable[cidx] > 1) {
                    names[cidx] = names[cidx]+filler[0];
                }
            }
        }

        ArrayList<String> preres = new ArrayList<String>();

        for (int i = 0; i <=4; i++) {
            if (ctable[i] > 0) {
                preres.add(ctable[i].toString() + " " + names[i]);
                pc--;
                if (pc == 1) {
                    preres.add(filler[2]);
                }
                if (pc > 1) {
                    preres.add(filler[1]);
                }
            }
        }

        String res = "";
        for (String p: preres) {
            res += p;
        }
        return res;
    }

    
    

    public static boolean isPrime(int num) {
        if (num <= 1) {return false;}
        if (num == 2) {return true;}
        int m = (int) Math.sqrt((double)num);
        int i = 2;
        while (i <= m) {
            if (num / (double) i == (int) num / i) {
                return false;
            }
            i++;
        }
        return true;
    }

    public static boolean comp(int[] a, int[] b) {
        Arrays.sort(a);
        Arrays.sort(b);    
        for (int i = 0; i < a.length; i++) {
            a[i] *= a[i];
        }
        return Arrays.equals(a,b);
    }

    // https://www.codewars.com/kata/576757b1df89ecf5bd00073b/train/java
    // Build Tower


    public static String[] towerBuilder(int nFloors) {
        String[] floors = new String[nFloors];
        int w = 1 + 2*(nFloors-1);
        for (int i = 0, j = 1; i < nFloors; i++, j+=2) {
            StringBuilder sides = new StringBuilder();
            StringBuilder stars = new StringBuilder();
            for ( int s = 0; s <= (w-j)/2;s++) { sides.append(" ");}
            for ( int s = 0; s < j;s++) { stars.append("*");}
            stars.append(sides);
            sides.append(stars);
            floors[i] = sides.toString();
        }
        return floors;
    }



 }