import java.math.BigInteger;
import java.util.ArrayList;
import java.util.List;

public class Fibonacci {

    public static List<BigInteger> fibonacci(BigInteger n) {
        List<BigInteger> fibList = new ArrayList<>();
        if (n.compareTo(BigInteger.ZERO) <= 0) {
            return fibList;
        }

        fibList.add(BigInteger.ZERO);
        if (n.equals(BigInteger.ONE)) {
            return fibList;
        }

        fibList.add(BigInteger.ONE);

        for (BigInteger i = BigInteger.valueOf(2); i.compareTo(n) < 0; i = i.add(BigInteger.ONE)) {
            BigInteger fib = fibList.get(i.intValue() - 1).add(fibList.get(i.intValue() - 2));
            fibList.add(fib);
        }

        return fibList;
    }

    public static void main(String[] args) {
        BigInteger n = new BigInteger("10");
        List<BigInteger> fibonacciNumbers = fibonacci(n);
        System.out.println("Fibonacci numbers up to position " + n + " are:");
        for (BigInteger num : fibonacciNumbers) {
            System.out.println(num);
        }
    }
}
