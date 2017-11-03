#include <stdio.h>
#include <stdlib.h>

void maxsum() {
    int n;
    char buf[10];

    scanf("%d\n", &n);

    int max=0;
    int sum=0;
    for (int i=0; i<n; ++i ) {
        scanf("%s", buf);
        sum += (char) atoi(buf); 
        if ( sum < 0 ) { sum = 0; }
        if ( max < sum ) { max = sum; }
    }

    printf("%d\n", max);
}

int main(int argc, char**argv) {
    int n;

    scanf("%d\n", &n);
    for (int i=0; i<n; ++i ) {
        maxsum();
    }
    
    return 0;
}
