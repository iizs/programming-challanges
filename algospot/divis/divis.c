#include <stdio.h>
#include <stdlib.h>
#include <string.h>

#define MAX_LENGTH 10000

int base64ToInt(char c) {
    if ( c >= '0' && c <= '9' ) { return c - '0'; }
    else if ( c >= 'A' && c <= 'Z' ) { return c - 'A' + 10; }
    else if ( c >= 'a' && c <= 'z' ) { return c - 'a' + 36; }
    return -1;
}

char intToBase64(int i) {
    if ( i >= 0 && i <= 9 ) { return '0' + i; }
    else if ( i >= 10 && i <= 35 ) { return 'A' + (i - 10); }
    else if ( i >= 36 && i <= 61 ) { return 'a' + (i - 36); }
    return '!';
}

char mod_z(char *in) {
    int len = strlen(in);

    if ( len == 1 ) {
        if ( in[0] == 'z' ) { return '0'; }
        return in[0];
    } else if ( len == 2 ) {
        int dividend = 62 * base64ToInt(in[0]) + base64ToInt(in[1]);
        int remains = dividend % 61;
        return intToBase64(remains);
    } else {
        char dividend[3];
        char remains = '0';
        char* p = in;
        while ( *p != '\0' ) {
            int n = base64ToInt(remains) * 62 + base64ToInt(*p);
            int q = n / 62;
            int r = n % 62;
            if ( q > 0 ) {
                dividend[0] = intToBase64(q);
                dividend[1] = intToBase64(r);
                dividend[2] = '\0';
            } else {
                dividend[0] = intToBase64(r);
                dividend[1] = '\0';
            }
            remains = mod_z(dividend);
            ++p;
        }

        return remains;
    }
}

void isDivisible(char *in) {
    if ( mod_z(in) == '0' ) {
        printf("yes\n");
    } else {
        printf("no\n");
    }
}


int main(int argc, char**argv) {
    char buf[MAX_LENGTH + 1];

    while ( 1 ) {
        scanf("%s\n", buf);
        if ( 0 == strcmp(buf, "end") ) {
            break;
        }
        isDivisible(buf);
    }
    
    return 0;
}
