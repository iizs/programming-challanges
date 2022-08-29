import java.util.Map;
import java.util.HashMap;
import java.util.Arrays;
import java.util.Scanner;

//public 

public class AlgospotDice {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        while(sc.hasNext()) {
            int count = sc.nextInt();
            if ( count == 0 ) {
                break;
            }
            System.out.println( String.format( "%.5f", AlgospotDice.dice(count, sc)) );
        }
    }

    public static double dice(int count, Scanner sc) {
        int[] dices = new int[count];
        int[] sums = new int[count];
        cache = new HashMap<>();

        for ( int i=0; i<count; ++i ) {
            dices[i] = Integer.parseInt(sc.next().substring(1));
        }
        int num = sc.nextInt();

        Arrays.sort(dices);
        int sum = 0;
        for ( int i=0; i<count; ++i ) {
            sum += dices[i];
            sums[i] = sum;

        }
        maxTargetNum = sum;

        //System.err.println( Arrays.toString(dices) + " / " + Arrays.toString(sums));

        return rollOne(dices, sums, count, num);
    }

    //private static Map<String,Double> cache;
    private static Map<Integer,Double> cache;
    private static int maxTargetNum = 0;

    public static double rollOne(int[] dices, int[] sums, int index, int targetNum) {
        double odds = 0.0;

        if ( index == 0 ) {
            if ( targetNum == 0 ) {
                return 1.0;
            } else {
                return 0.0;
            }
        }

        if ( targetNum > sums[index-1] ) {
            return 0.0;
        }

        //String key = String.format("%d;%d", index-1, targetNum);
        Integer key = new Integer( maxTargetNum * (index-1) + targetNum );

        if ( cache.containsKey(key) ) {
            return cache.get(key).doubleValue();
        }


        for ( int num=1; num <= dices[index-1]; ++num) {
            odds += rollOne(dices, sums, index - 1, targetNum - num ) / (double) dices[index-1];
        }

        cache.put(key, odds);
        return odds;
    }
}
