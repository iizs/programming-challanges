import java.util.Scanner;

public class Codeforces1721C {
    public static void printList(int[] l) {
        for (int j : l) {
            System.out.print(j);
            System.out.print(' ');
        }
        System.out.println();
    }

    public static void v2(int size, int[] list_a, int[] list_b) {
        int[] list_d_min = new int[size];
        int[] list_d_max = new int[size];

        int idx_a = 0;
        int idx_b = 0;
        int idx_d_min = 0;

        int b_min = list_b[idx_b];
        while (idx_a < list_a.length && idx_b < list_b.length) {
            if (list_a[idx_a] > list_b[idx_b]) {
                while (idx_d_min < list_d_min.length && idx_d_min<idx_a) {
                    list_d_min[idx_d_min] = b_min - list_a[idx_d_min];
                    ++idx_d_min;
                }
                ++idx_b;
                b_min = list_b[idx_b];
            } else {
                ++idx_a;
            }
        }
        // fill remaining list_d_min
        for (; idx_d_min < list_d_min.length; ++idx_d_min) {
            list_d_min[idx_d_min] = b_min - list_a[idx_d_min];
        }
        idx_a = list_a.length - 1;
        idx_b = list_b.length - 1;
        int idx_d_max = list_d_max.length - 1;
        int b_max = list_b[idx_b];
        while (idx_a >= 0 && idx_b > 0) {
            if (list_a[idx_a] > list_b[idx_b-1]) {
                boolean update_b_max = false;
                while (idx_d_max >= 0 && idx_d_max>=idx_b) {
                    list_d_max[idx_d_max] = b_max - list_a[idx_d_max];
                    --idx_d_max;
                    update_b_max = true;
                }
                if (update_b_max) {
                    b_max = list_b[idx_b - 1];
                }
                --idx_a;
                --idx_b;

            } else {
                --idx_a;
                --idx_b;
            }
        }
        // fill remaining list_d_max
        for (; idx_d_max >= 0; --idx_d_max) {
            list_d_max[idx_d_max] = b_max - list_a[idx_d_max];
        }

        Codeforces1721C.printList(list_d_min);
        Codeforces1721C.printList(list_d_max);
        //System.out.println("----");
    }

    // Porting GargYogesh's C++ code to Java
    public static void v3(int size, int[] list_a, int[] list_b) {
        int[] list_d_min = new int[size];
        int[] list_d_max = new int[size];

        if(size==1)
        {
            list_d_min[0] = list_b[0] - list_a[0];
            list_d_max[0] = list_b[0] - list_a[0];
        }
        else{
            int ind2 = 0;
            int ind1 = 0;

            while(ind2 < size && ind1 < size)
            {
                if(list_b[ind2]>=list_a[ind1])
                {
                    list_d_min[ind1] = list_b[ind2] - list_a[ind1];
                    ind1++;
                }
                else {
                    ind2++;
                }
            }

            ind1 = size - 1;
            ind2 = size - 1;
            while ( ind1 >= 0 )
            {
                if(ind1==size-1)
                {
                    list_d_max[ind1]=list_b[ind2]-list_a[ind1];
                }
                else{
                    if(list_a[ind1+1]>list_b[ind1])
                    {
                        ind2=ind1;
                    }
                    list_d_max[ind1]=list_b[ind2]-list_a[ind1];
                }
                ind1--;
            }
        }
        Codeforces1721C.printList(list_d_min);
        Codeforces1721C.printList(list_d_max);
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

            //v2(size, list_a, list_b);
            v3(size, list_a, list_b);


        }


    }
}
