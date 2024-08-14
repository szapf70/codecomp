import java.util.*;
import static java.util.stream.Collectors.toList;

public class GoodVsEvil {
  public static String battle(String goodAmounts, String evilAmounts) {
      int[] gw = new int[] {1,2,3,3,4,10};
      int[] ew = new int[] {1,2,2,2,3,5,10};
      List<Integer> gt = Arrays.stream(goodAmounts.split(" "))
              .map(Integer::parseInt)
              .collect(toList());
      List<Integer> et = Arrays.stream(evilAmounts.split(" "))
              .map(Integer::parseInt)
              .collect(toList());
      int gs = 0;
      int es = 0;
      for (int i = 0; i < 6;i++) {
          gs += gw[i]*gt.get(i);
      }
      for (int i = 0; i < 7;i++) {
          es += ew[i]*et.get(i);
      }
      if (gs>es) {
          return "Battle Result: Good triumphs over Evil";
      }
      if (es>gs) {
          return "Battle Result: Evil eradicates all trace of Good";
      }
      return "Battle Result: No victor on this battle field";
  }
}
