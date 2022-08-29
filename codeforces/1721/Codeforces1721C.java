import java.util.Scanner;

public class Codeforces1721C {
    public static void printList(int[] l) {
        for (int j : l) {
            System.out.print(j);
            System.out.print(' ');
        }
        System.out.println();
    }
    public static boolean ableToFill(int[] list_a, int[] list_b, int a, int b) {
        boolean skipped_a = false;
        boolean skipped_b = false;
        int idx_a = 0;
        int idx_b = 0;
        while (idx_a < list_a.length && idx_b < list_b.length) {
            if ( !skipped_a && a == list_a[idx_a] ) {
                idx_a += 1;
                skipped_a = true;
                continue;
            }
            if ( !skipped_b && b == list_b[idx_b] ) {
                idx_b += 1;
                skipped_b = true;
                continue;
            }
            if (list_a[idx_a] > list_b[idx_b]) {
                return false;
            }
            idx_a += 1;
            idx_b += 1;
        }
        return true;
    }
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);

        int count = sc.nextInt();
        if ( count == 0 ) {
            return;
        }
        for(int i=0; i<count; ++i) {
            int size = sc.nextInt();
            int[] list_a = new int[size];
            int[] list_b = new int[size];
            int[] list_d_min = new int[size];
            int[] list_d_max = new int[size];
            for(int j=0; j<size; ++j) {
                list_a[j] = sc.nextInt();
            }
            for(int j=0; j<size; ++j) {
                list_b[j] = sc.nextInt();
            }

            int prev_a = -1;
            int prev_d = -1;
            for(int idx_a=0; idx_a<list_a.length; ++idx_a) {
                if ( prev_a != -1 && prev_a == list_a[idx_a] ) {
                    list_d_min[idx_a] = prev_d;
                    continue;
                }
                for(int idx_b=0; idx_b<list_b.length; ++idx_b) {
                    if (list_b[idx_b] >= list_a[idx_a]) {
                        list_d_min[idx_a] = list_b[idx_b] - list_a[idx_a];
                        prev_a = list_a[idx_a];
                        prev_d = list_d_min[idx_a];
                        break;
                    }
                }
            }

            prev_a = -1;
            prev_d = -1;
            for(int idx_a=list_a.length-1; idx_a>=0; --idx_a) {
                if ( prev_a != -1 && prev_a == list_a[idx_a] ) {
                    list_d_max[idx_a] = prev_d;
                    continue;
                }
                for(int idx_b=list_b.length-1; idx_b>=0; --idx_b) {
                    if ( Codeforces1721C.ableToFill(list_a, list_b, list_a[idx_a], list_b[idx_b]) ) {
                        list_d_max[idx_a] = list_b[idx_b] - list_a[idx_a];
                        prev_a = list_a[idx_a];
                        prev_d = list_d_max[idx_a];
                        break;
                    }
                }

            }

            // Codeforces1721C.printList(list_a);
            // Codeforces1721C.printList(list_b);
            Codeforces1721C.printList(list_d_min);
            Codeforces1721C.printList(list_d_max);


        }


    }
}
