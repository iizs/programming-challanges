import java.util.Scanner;

public class Codeforces1721C {
    public static void printList(int[] l) {
        for (int j : l) {
            System.out.print(j);
            System.out.print(' ');
        }
        System.out.println();
    }

    public static void v1(int size, int[] list_a, int[] list_b) {
        int[] list_able_to_map_from = new int[size];
        int[] list_able_to_map_until = new int[size];
        int[] list_d_min = new int[size];
        int[] list_d_max = new int[size];
        int idx_until = 0;
        for (int idx_a=0; idx_a<list_a.length; ++idx_a) {
            int idx_b = 0;
            while (idx_b<list_b.length && list_a[idx_a] > list_b[idx_b]) {
                ++idx_b;
            }
            list_able_to_map_from[idx_a] = idx_b;
            if (idx_a != 0 && list_able_to_map_from[idx_a] == idx_a) {
                list_able_to_map_until[idx_until] = idx_a;
                ++idx_until;
            }
        }
        if (idx_until < list_able_to_map_until.length) {
            list_able_to_map_until[idx_until] = -1;
        }

        for(int idx_a=0; idx_a<list_a.length; ++idx_a) {
            list_d_min[idx_a] = list_b[list_able_to_map_from[idx_a]] - list_a[idx_a];
            for (idx_until=0; idx_until<list_able_to_map_until.length && list_able_to_map_until[idx_until] != -1; ++idx_until) {
                if (list_able_to_map_until[idx_until] > idx_a) {
                    break;
                }
            }

            if (list_able_to_map_until[idx_until] != -1) {
                list_d_max[idx_a] = list_b[list_able_to_map_until[idx_until] - 1] - list_a[idx_a];
            } else {
                list_d_max[idx_a] = list_b[list_b.length - 1] - list_a[idx_a];
            }
        }

        //Codeforces1721C.printList(list_a);
        //Codeforces1721C.printList(list_b);
        //Codeforces1721C.printList(list_able_to_map_from);
        //Codeforces1721C.printList(list_able_to_map_until);
        Codeforces1721C.printList(list_d_min);
        //Codeforces1721C.printList(list_d_max);
        Codeforces1721C.printList(list_d_max);
        //System.out.println("----");
    }

    public static void v2(int size, int[] list_a, int[] list_b) {

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


            for(int j=0; j<size; ++j) {
                list_a[j] = sc.nextInt();
            }
            for(int j=0; j<size; ++j) {
                list_b[j] = sc.nextInt();
            }

            v1(size, list_a, list_b);
            v2(size, list_a, list_b);


        }


    }
}
