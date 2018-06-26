import java.util.Map;
import java.util.HashMap;
import java.util.Set;
import java.util.HashSet;
import java.util.List;
import java.util.ArrayList;
import java.util.LinkedList;
import java.util.Scanner;
import java.util.Iterator;

public class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        while(sc.hasNext()) {
            int count = sc.nextInt();
            if ( count == 0 ) {
                break;
            }
            Main.censor(count, sc);
        }
    }

    private static void censor(int count, Scanner sc) {
        String text = sc.next();
        List<String> filter = new LinkedList<>();
        Map<String, String> filterMap = new HashMap<>();
        int maxFilterLength = 0;

        for (int i=0; i<count; ++i) {
            String f = sc.next();
            filter.add(f);
            if ( f.length() > maxFilterLength ) {
                maxFilterLength = f.length();
            }
        }

        Map<String, String> cache = new HashMap<>();

        System.out.println( censorReplace(text, filter, cache, maxFilterLength).length() );
    }

    private static String censorReplace(String text, List<String> filter, Map<String, String> cache, int maxFilterLength) {
        String result = text;

        if ( cache.containsKey(text) ) {
            return cache.get(text);
        }

        for ( String f : filter ) {
            int offset = text.indexOf(f);
            while ( offset != -1 ) {
                String a = text.substring(0, offset);
                String b = text.substring(offset + f.length());

                String candidate = text;

                String censor_a = censorReplace(a, filter, cache, maxFilterLength);
                String censor_b = censorReplace(b, filter, cache, maxFilterLength);

                String candidate_full = censorReplace(censor_a + censor_b, filter, cache, maxFilterLength);
                if (candidate_full.length() < candidate.length()) {
                    candidate = candidate_full;
                }

                String candidate_left = censorReplace(censor_a + b , filter, cache, maxFilterLength);
                if (candidate_left.length() < candidate.length()) {
                    candidate = candidate_left;
                }

                String candidate_right = censorReplace(a + censor_b, filter, cache, maxFilterLength);
                if (candidate_right.length() < candidate.length()) {
                    candidate = candidate_right;
                }

                int point1 = Math.max(0, offset - maxFilterLength);
                int point2 = Math.min(b.length(), maxFilterLength);
                String left_mid = a.substring(0, point1);
                String mid = a.substring(point1) + b.substring(0, point2);
                String right_mid = b.substring(point2);
                String candidate_mid = censorReplace(
                    censorReplace(left_mid, filter, cache, maxFilterLength) + mid + censorReplace(right_mid, filter, cache, maxFilterLength),
                    filter, cache, maxFilterLength);
                if (candidate_mid.length() < candidate.length()) {
                    candidate = candidate_mid;
                }

                if ( candidate.length() < result.length() ) {
                    result = candidate;
                    if ( result.length() == 0 ) {
                        cache.put(text, result);
                        return result;
                    }
                }
                offset = text.indexOf(f, offset + 1);
            }
        }

        cache.put(text, result);
        return result;
    }


}
