public class Solution{
    public static String whatCentury(int year) {
      String[] ending = new String[] {"th","st","nd","rd","th","th","th","th","th","th","th","th","th","th"};
      int y = year / 100;
      if (year%100 > 0) {
          y++;
      }
      String estr = Integer.toString(y);
      if (y < 14) {
          estr += ending[y%100];
      } else {
          estr += ending[y%10];
      }
      return estr;
    }
}

