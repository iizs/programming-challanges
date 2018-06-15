import java.util.Map;
import java.util.HashMap;
import java.util.List;
import java.util.ArrayList;
import java.util.Scanner;

class Node {
    private String value;
    private Map<String, Node> childs;

    public Node(String s) {
        value = s;
        childs = new HashMap<>();
    }

    public void addValue(String s) {
        if ( value != null ) {
            // leaf
            String k1 = value.substring(0, 1);
            String v1 = value.substring(1);
            Node c1 = new Node(v1);
            childs.put(k1, c1);
            value = null;
        } 

        // non-leaf
        String k = s.substring(0, 1);
        String v = s.substring(1);
        Node child = childs.get(k);
        if ( child == null ) {
            child = new Node(v);
            childs.put(k, child);
        } else {
            child.addValue(v);
        }
    }

    public int getLength(int l) {
        if ( value != null ) {
            return l;
        }

        int v = 0;
        for ( Node n : childs.values() ) {
            v += n.getLength(l + 1);
        }

        return v;
    }

}

public class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int cases = sc.nextInt();
        while(cases-- > 0) {
            Main.solver(sc);
        }
    }

    private static void solver(Scanner sc) {
        int count = sc.nextInt();
        List<String> names = new ArrayList<>();
        for (int i=0; i<count; ++i) {
            names.add(sc.next());
        }

        int min = Integer.MAX_VALUE;
        for (String name: names) {
            List<String> subNames = new ArrayList<>(names);
            subNames.remove(name);
            min = Math.min(min, Main.findMinimumAbbr(subNames));
        }

        System.out.println(min);
    }

    private static int findMinimumAbbr(List<String> names) {
        Node root = null;

        for ( String name: names) {
            if ( root != null ) {
                root.addValue(name);
            } else {
                root = new Node(name);
            }
        }
        return root.getLength(0);
    }
}
