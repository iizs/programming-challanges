#include <stdio.h>
#include <stdlib.h>
#include <string.h>

// 1: true, 0: false
int testIfPalindrome(char *str, int len) {
    int n = len / 2; 
    for (int i=0; i<n; ++i) {
        if ( str[i] != str[len-i-1] ) {
            return 0;
        }
    }
    return 1;
}

int getMinPalindrome(char *str) {
    int l = strlen(str);
    for (int i=0; i<l+1; ++i) {
        if (testIfPalindrome(str+i, l-i) == 1) {
            return i + l;
        }
    }
    return 2*l;
}

int main(int argc, char**argv) {
    int n;
    char str[100000+1];

    scanf("%d\n", &n);
    for (int i=0; i<n; ++i ) {
        scanf("%s\n", str);
        int r = getMinPalindrome(str);
        printf("%d\n", r);
    }
}

